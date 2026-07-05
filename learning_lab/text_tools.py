"""Text cleanup examples."""

from __future__ import annotations

import string


def normalize_name(name: str) -> str:
    """Trim extra spaces and title-case a person's name."""
    return " ".join(name.split()).title()


def slugify(text: str) -> str:
    """Turn text into a URL-friendly slug."""
    allowed = string.ascii_lowercase + string.digits + " "
    cleaned = "".join(char for char in text.lower() if char in allowed)
    return "-".join(cleaned.split())


def initials(name: str) -> str:
    """Return uppercase initials for each part of a name."""
    return "".join(part[0].upper() for part in name.split() if part)


def reverse_words(text: str) -> str:
    """Return words in reverse order."""
    return " ".join(reversed(text.split()))
