"""Safe local installation for GNOME Shell extension archives."""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from zipfile import BadZipFile, ZipFile


class ArchiveError(ValueError):
    pass


@dataclass(frozen=True)
class ExtensionArchive:
    path: Path
    uuid: str
    name: str
    shell_versions: tuple[str, ...]


def _safe_member(name: str) -> PurePosixPath:
    member = PurePosixPath(name)
    if member.is_absolute() or '..' in member.parts or not member.parts:
        raise ArchiveError(f'Unsafe archive path: {name}')
    return member


def inspect_archive(path: str | Path) -> ExtensionArchive:
    path = Path(path)
    try:
        with ZipFile(path) as archive:
            members = [item for item in archive.infolist() if not item.is_dir()]
            for item in members:
                _safe_member(item.filename)
            metadata_members = [item for item in members
                                if item.filename == 'metadata.json']
            if len(metadata_members) != 1:
                raise ArchiveError('Archive must contain metadata.json at its root')
            raw = archive.read(metadata_members[0])
    except (OSError, BadZipFile) as error:
        raise ArchiveError(f'Cannot read archive: {error}') from error
    try:
        metadata = json.loads(raw)
        uuid = metadata['uuid']
        name = metadata['name']
    except (json.JSONDecodeError, KeyError, TypeError) as error:
        raise ArchiveError('metadata.json must contain string uuid and name values') from error
    if not isinstance(uuid, str) or not uuid or '/' in uuid or uuid in {'.', '..'}:
        raise ArchiveError('Extension UUID is invalid')
    if not isinstance(name, str) or not name:
        raise ArchiveError('Extension name is invalid')
    versions = metadata.get('shell-version', [])
    if not isinstance(versions, list) or not all(isinstance(value, str) for value in versions):
        raise ArchiveError('shell-version must be a list of strings')
    return ExtensionArchive(path, uuid, name, tuple(versions))


def install_archive(extension: ExtensionArchive, destination_root: str | Path) -> Path:
    destination = Path(destination_root) / extension.uuid
    if destination.exists():
        raise ArchiveError(f'Destination already exists: {destination}')
    destination.mkdir(parents=True)
    try:
        with ZipFile(extension.path) as archive:
            for item in archive.infolist():
                if item.is_dir():
                    continue
                member = _safe_member(item.filename)
                target = destination.joinpath(*member.parts)
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(item) as source, target.open('wb') as output:
                    output.write(source.read())
    except Exception:
        for child in sorted(destination.rglob('*'), reverse=True):
            if child.is_file() or child.is_symlink():
                child.unlink()
            else:
                child.rmdir()
        destination.rmdir()
        raise
    return destination
