"""Small statistics practice examples."""

from __future__ import annotations


def median(values: list[float]) -> float:
    """Return the median value."""
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    middle = len(ordered) // 2
    if len(ordered) % 2 == 1:
        return ordered[middle]
    return (ordered[middle - 1] + ordered[middle]) / 2


def mode(values: list[str]) -> str:
    """Return the most common string."""
    if not values:
        raise ValueError("values must not be empty")
    return max(set(values), key=values.count)


def range_size(values: list[float]) -> float:
    """Return max minus min."""
    if not values:
        raise ValueError("values must not be empty")
    return max(values) - min(values)
