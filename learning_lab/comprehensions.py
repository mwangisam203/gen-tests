"""List and dictionary comprehension practice."""

from __future__ import annotations


def squares(values: list[int]) -> list[int]:
    """Return every value squared."""
    return [value * value for value in values]


def index_by_first_letter(names: list[str]) -> dict[str, list[str]]:
    """Group names by their first letter."""
    grouped: dict[str, list[str]] = {}
    for name in names:
        key = name[0].upper()
        grouped.setdefault(key, []).append(name)
    return grouped


def invert_lookup(data: dict[str, str]) -> dict[str, str]:
    """Swap keys and values in a dictionary."""
    return {value: key for key, value in data.items()}
