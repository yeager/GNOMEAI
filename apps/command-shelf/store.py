"""Bounded local storage for named command snippets."""
from __future__ import annotations
import json
import os
from pathlib import Path

MAX_ITEMS = 100


def state_path() -> Path:
    base = Path(os.environ.get('XDG_STATE_HOME', Path.home() / '.local' / 'state'))
    return base / 'command-shelf' / 'items.json'


def load(path: Path | None = None) -> list[dict[str, str]]:
    path = path or state_path()
    try:
        value = json.loads(path.read_text(encoding='utf-8'))
    except (FileNotFoundError, OSError, json.JSONDecodeError):
        return []
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, dict) and isinstance(item.get('name'), str) and isinstance(item.get('command'), str)]


def save(items: list[dict[str, str]], path: Path | None = None) -> list[dict[str, str]]:
    clean: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for item in items:
        name, command = item.get('name', '').strip(), item.get('command', '').strip()
        key = (name, command)
        if name and command and key not in seen:
            clean.append({'name': name, 'command': command})
            seen.add(key)
    clean = clean[:MAX_ITEMS]
    path = path or state_path()
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(clean, ensure_ascii=False), encoding='utf-8')
    temporary.replace(path)
    path.chmod(0o600)
    return clean
