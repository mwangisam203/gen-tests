"""Regular expression practice."""

from __future__ import annotations

import re


def find_numbers(text: str) -> list[int]:
    """Return every whole number in text."""
    return [int(match) for match in re.findall(r"\d+", text)]


def mask_email(email: str) -> str:
    """Mask the visible part of an email address."""
    name, domain = email.split("@", maxsplit=1)
    if len(name) <= 2:
        masked = name[0] + "*"
    else:
        masked = name[0] + "*" * (len(name) - 2) + name[-1]
    return f"{masked}@{domain}"


def has_zip_code(text: str) -> bool:
    """Return True when text contains a five-digit zip code."""
    return re.search(r"\b\d{5}\b", text) is not None
