"""Simple parsing practice examples."""

from __future__ import annotations


def parse_key_value(text: str) -> dict[str, str]:
    """Parse lines like key=value into a dictionary."""
    result: dict[str, str] = {}
    for line in text.splitlines():
        if not line.strip():
            continue
        key, value = line.split("=", maxsplit=1)
        result[key.strip()] = value.strip()
    return result


def parse_tags(text: str) -> list[str]:
    """Parse comma-separated tags."""
    return [tag.strip() for tag in text.split(",") if tag.strip()]
