"""JSON reading examples."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def read_json(path: str | Path) -> dict[str, Any]:
    """Read a JSON object from disk."""
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("JSON root must be an object")
    return data


def profile_summary(profile: dict[str, Any]) -> str:
    """Create a short summary from a profile dictionary."""
    name = profile.get("name", "Unknown")
    language = profile.get("favorite_language", "Python")
    return f"{name} is practicing {language}."
