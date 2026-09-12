"""Persist Focus Block settings in the XDG state directory."""
from __future__ import annotations
import json
import os
from pathlib import Path

DEFAULT = {'focus_minutes': 25, 'break_minutes': 5}


def state_path() -> Path:
    base = Path(os.environ.get('XDG_STATE_HOME', Path.home() / '.local' / 'state'))
    return base / 'focus-block' / 'settings.json'


def load(path: Path | None = None) -> dict[str, int]:
    path = path or state_path()
    try:
        value = json.loads(path.read_text(encoding='utf-8'))
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        return DEFAULT.copy()
    if not isinstance(value, dict):
        return DEFAULT.copy()
    result = DEFAULT.copy()
    for key in result:
        candidate = value.get(key)
        if isinstance(candidate, int) and 1 <= candidate <= 240:
            result[key] = candidate
    return result


def save(value: dict[str, int], path: Path | None = None) -> dict[str, int]:
    result = {key: int(value[key]) for key in DEFAULT if isinstance(value.get(key), int) and 1 <= value[key] <= 240}
    result = DEFAULT | result
    path = path or state_path()
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(result), encoding='utf-8')
    temporary.replace(path)
    path.chmod(0o600)
    return result
