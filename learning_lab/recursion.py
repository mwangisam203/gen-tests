"""Recursion practice examples."""

from __future__ import annotations


def factorial(number: int) -> int:
    """Return number factorial using recursion."""
    if number < 0:
        raise ValueError("number must be non-negative")
    if number in (0, 1):
        return 1
    return number * factorial(number - 1)


def sum_nested(values: list[int | list[int]]) -> int:
    """Return the sum of integers inside a one-level nested list."""
    total = 0
    for value in values:
        if isinstance(value, list):
            total += sum_nested(value)
        else:
            total += value
    return total
