"""Date and time examples."""

from __future__ import annotations

from datetime import date, timedelta


def days_until(target: date, today: date | None = None) -> int:
    """Return whole days from today until target."""
    current = today or date.today()
    return (target - current).days


def add_week(start: date) -> date:
    """Return the date one week after start."""
    return start + timedelta(days=7)


def is_weekend(day: date) -> bool:
    """Return True for Saturday or Sunday."""
    return day.weekday() >= 5
