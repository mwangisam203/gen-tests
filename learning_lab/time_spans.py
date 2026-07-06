"""Time span practice examples."""

from __future__ import annotations


def minutes_to_hours(minutes: int) -> tuple[int, int]:
    """Convert minutes to hours and leftover minutes."""
    if minutes < 0:
        raise ValueError("minutes must be non-negative")
    return divmod(minutes, 60)


def format_duration(seconds: int) -> str:
    """Format seconds as MM:SS."""
    if seconds < 0:
        raise ValueError("seconds must be non-negative")
    minutes, leftover = divmod(seconds, 60)
    return f"{minutes:02d}:{leftover:02d}"
