"""Dice probability practice helpers."""

from __future__ import annotations


def two_die_totals(sides: int = 6) -> dict[int, int]:
    """Return outcome counts for rolling two dice."""
    if sides < 1:
        raise ValueError("sides must be positive")
    counts: dict[int, int] = {}
    for left in range(1, sides + 1):
        for right in range(1, sides + 1):
            total = left + right
            counts[total] = counts.get(total, 0) + 1
    return counts


def probability_of_total(total: int, sides: int = 6) -> float:
    """Return the probability of a two-die total."""
    counts = two_die_totals(sides)
    return counts.get(total, 0) / (sides * sides)
