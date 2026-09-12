"""Local, bounded storage for manually captured clipboard text."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Iterable

MAX_ITEMS = 100


def state_path() -> Path:
    base = Path(os.environ.get("XDG_STATE_HOME", Path.home() / ".local" / "state"))
    return base / "clip-shelf" / "items.json"


def load(path: Path | None = None) -> list[str]:
    path = path or state_path()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return []
    if not isinstance(payload, list):
        return []
    return [item for item in payload if isinstance(item, str)]


def save(items: Iterable[str], path: Path | None = None) -> list[str]:
    path = path or state_path()
    cleaned: list[str] = []
    for item in items:
        if isinstance(item, str) and item and item not in cleaned:
            cleaned.append(item)
    cleaned = cleaned[:MAX_ITEMS]
    path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(cleaned, ensure_ascii=False), encoding="utf-8")
    temporary.replace(path)
    try:
        path.chmod(0o600)
    except OSError:
        pass
    return cleaned


def prepend(item: str, items: Iterable[str]) -> list[str]:
    return save([item, *items])
