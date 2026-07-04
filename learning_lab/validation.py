"""Input validation examples."""

from __future__ import annotations


def require_non_empty(text: str, field_name: str) -> str:
    """Return stripped text or raise a friendly error."""
    cleaned = text.strip()
    if not cleaned:
        raise ValueError(f"{field_name} must not be empty")
    return cleaned


def require_between(value: int, low: int, high: int) -> int:
    """Return value when it is inside the inclusive range."""
    if not low <= value <= high:
        raise ValueError(f"value must be between {low} and {high}")
    return value
