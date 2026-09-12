import json
import sys
from pathlib import Path
from zipfile import ZipFile
import pytest
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from installer import ArchiveError, inspect_archive, install_archive


def make_archive(path, metadata, files=()):
    with ZipFile(path, 'w') as archive:
        archive.writestr('metadata.json', json.dumps(metadata))
        for name, content in files:
            archive.writestr(name, content)


def test_inspects_and_installs_valid_archive(tmp_path):
    archive = tmp_path / 'sample.zip'
    make_archive(archive, {'uuid': 'sample@example', 'name': 'Sample', 'shell-version': ['49']}, [('extension.js', 'export default null;')])
    extension = inspect_archive(archive)
    installed = install_archive(extension, tmp_path / 'extensions')
    assert extension.uuid == 'sample@example'
    assert installed.joinpath('extension.js').read_text() == 'export default null;'


def test_rejects_path_traversal(tmp_path):
    archive = tmp_path / 'unsafe.zip'
    make_archive(archive, {'uuid': 'sample@example', 'name': 'Sample'}, [('../outside', 'bad')])
    with pytest.raises(ArchiveError, match='Unsafe archive path'):
        inspect_archive(archive)


def test_refuses_existing_destination(tmp_path):
    archive = tmp_path / 'sample.zip'
    make_archive(archive, {'uuid': 'sample@example', 'name': 'Sample'})
    extension = inspect_archive(archive)
    (tmp_path / 'extensions' / extension.uuid).mkdir(parents=True)
    with pytest.raises(ArchiveError, match='already exists'):
        install_archive(extension, tmp_path / 'extensions')


def test_rejects_nested_metadata(tmp_path):
    archive = tmp_path / 'nested.zip'
    with ZipFile(archive, 'w') as output:
        output.writestr('nested/metadata.json', json.dumps({'uuid': 'sample@example', 'name': 'Sample'}))
    with pytest.raises(ArchiveError, match='at its root'):
        inspect_archive(archive)
