"""ISBN-10 practice helpers."""

from __future__ import annotations


def normalize_isbn10(isbn: str) -> str:
    """Remove separators and uppercase an ISBN-10."""
    return isbn.replace("-", "").replace(" ", "").upper()


def is_valid_isbn10(isbn: str) -> bool:
    """Return True when an ISBN-10 checksum is valid."""
    normalized = normalize_isbn10(isbn)
    if len(normalized) != 10:
        return False
    total = 0
    for index, char in enumerate(normalized, start=1):
        if char == "X" and index == 10:
            value = 10
        elif char.isdigit():
            value = int(char)
        else:
            return False
        total += index * value
    return total % 11 == 0
