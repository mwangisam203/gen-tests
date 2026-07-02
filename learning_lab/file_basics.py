"""Small file-reading and file-writing helpers."""

from __future__ import annotations

from pathlib import Path


def read_lines(path: str | Path) -> list[str]:
    """Read a text file and remove trailing newlines."""
    return Path(path).read_text(encoding="utf-8").splitlines()


def write_note(path: str | Path, title: str, body: str) -> None:
    """Write a simple two-part note to disk."""
    content = f"# {title}\n\n{body}\n"
    Path(path).write_text(content, encoding="utf-8")


def count_non_empty_lines(path: str | Path) -> int:
    """Count lines that contain visible text."""
    return sum(1 for line in read_lines(path) if line.strip())
