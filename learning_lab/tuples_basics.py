"""Tuple practice examples."""

from __future__ import annotations


Point = tuple[int, int]


def move_point(point: Point, dx: int, dy: int) -> Point:
    """Move a 2D point by dx and dy."""
    x, y = point
    return x + dx, y + dy


def midpoint(left: Point, right: Point) -> tuple[float, float]:
    """Return the midpoint between two points."""
    return (left[0] + right[0]) / 2, (left[1] + right[1]) / 2


def swap_pair(pair: tuple[str, str]) -> tuple[str, str]:
    """Swap the two values in a pair."""
    first, second = pair
    return second, first
