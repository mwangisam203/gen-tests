"""Pathlib practice examples."""

from __future__ import annotations

from pathlib import Path


def file_extension(path: str | Path) -> str:
    """Return a file extension without the leading dot."""
    return Path(path).suffix.removeprefix(".")


def sibling_path(path: str | Path, sibling_name: str) -> Path:
    """Return a path next to another path."""
    return Path(path).with_name(sibling_name)


def ensure_folder(path: str | Path) -> Path:
    """Create a folder if needed and return it."""
    folder = Path(path)
    folder.mkdir(parents=True, exist_ok=True)
    return folder
