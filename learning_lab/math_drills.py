"""Math drill helpers."""

from __future__ import annotations


def multiplication_table(number: int, upto: int = 10) -> list[str]:
    """Return a multiplication table as readable lines."""
    if upto < 1:
        raise ValueError("upto must be at least 1")
    return [f"{number} x {factor} = {number * factor}" for factor in range(1, upto + 1)]


def clamp(value: int, low: int, high: int) -> int:
    """Keep a value inside a low-high range."""
    if low > high:
        raise ValueError("low must be less than or equal to high")
    return max(low, min(value, high))


def percent(part: float, whole: float) -> float:
    """Return part as a percentage of whole."""
    if whole == 0:
        raise ValueError("whole must not be zero")
    return round((part / whole) * 100, 2)
