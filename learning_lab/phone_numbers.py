"""Phone number formatting practice."""

from __future__ import annotations


def digits_only(text: str) -> str:
    """Return only digit characters."""
    return "".join(char for char in text if char.isdigit())


def format_us_phone(text: str) -> str:
    """Format ten digits as a US phone number."""
    digits = digits_only(text)
    if len(digits) != 10:
        raise ValueError("phone number must have 10 digits")
    return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"
