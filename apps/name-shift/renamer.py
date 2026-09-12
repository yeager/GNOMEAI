"""Safe, deterministic file-name preview and rename helpers."""
from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Preview:
    source: Path
    target: Path
    error: str | None = None


def target_name(path: Path, find: str, replace: str, prefix: str, suffix: str) -> str:
    """Return a changed basename, keeping all suffixes attached to the stem."""
    stem = path.stem.replace(find, replace) if find else path.stem
    return f"{prefix}{stem}{suffix}{path.suffix}"


def preview(paths: list[Path], find: str = '', replace: str = '',
            prefix: str = '', suffix: str = '') -> list[Preview]:
    """Build a rename plan and reject collisions or no-op names."""
    plans = [Preview(path, path.with_name(target_name(path, find, replace, prefix, suffix)))
             for path in paths]
    targets: dict[Path, int] = {}
    for item in plans:
        targets[item.target] = targets.get(item.target, 0) + 1
    result: list[Preview] = []
    sources = {item.source for item in plans}
    for item in plans:
        error = None
        if item.target == item.source:
            error = 'Name is unchanged'
        elif item.target.name in {'', '.', '..'} or '/' in item.target.name:
            error = 'Invalid file name'
        elif targets[item.target] > 1:
            error = 'Two selected files would use this name'
        elif item.target.exists() and item.target not in sources:
            error = 'A file with this name already exists'
        elif item.target.exists():
            error = 'Target is another selected file'
        result.append(Preview(item.source, item.target, error))
    return result


def apply(plans: list[Preview]) -> list[Path]:
    """Rename a validated plan. Refuse the entire operation if any plan is invalid."""
    if not plans or any(plan.error for plan in plans):
        raise ValueError('Rename plan is not valid')
    renamed: list[Path] = []
    for plan in plans:
        plan.source.rename(plan.target)
        renamed.append(plan.target)
    return renamed
