"""Simple cache practice."""

from __future__ import annotations


def remember(cache: dict[str, str], key: str, value: str) -> str:
    """Store and return a value."""
    cache[key] = value
    return value


def get_or_remember(cache: dict[str, str], key: str, fallback: str) -> str:
    """Return an existing cached value or store a fallback."""
    if key not in cache:
        remember(cache, key, fallback)
    return cache[key]
