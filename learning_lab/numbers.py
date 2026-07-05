"""Number-focused examples for practicing functions."""

from __future__ import annotations


def add_tax(price: float, tax_rate: float) -> float:
    """Return a price after adding tax."""
    if price < 0:
        raise ValueError("price must be non-negative")
    if tax_rate < 0:
        raise ValueError("tax_rate must be non-negative")
    return round(price * (1 + tax_rate), 2)


def average(values: list[float]) -> float:
    """Return the average of a non-empty list."""
    if not values:
        raise ValueError("values must not be empty")
    return sum(values) / len(values)


def is_even(number: int) -> bool:
    """Return True when a number is divisible by 2."""
    return number % 2 == 0


def difference(left: float, right: float) -> float:
    """Return the absolute difference between two numbers."""
    return abs(left - right)
