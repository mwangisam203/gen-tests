"""Configuration parsing practice."""

from __future__ import annotations


def parse_bool(value: str) -> bool:
    """Parse common boolean strings."""
    normalized = value.strip().lower()
    if normalized in {"1", "true", "yes", "on"}:
        return True
    if normalized in {"0", "false", "no", "off"}:
        return False
    raise ValueError(f"unknown boolean value: {value}")


def parse_int_setting(settings: dict[str, str], key: str, default: int) -> int:
    """Read an integer setting from a dictionary."""
    return int(settings.get(key, default))
