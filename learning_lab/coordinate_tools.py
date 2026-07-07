"""Coordinate practice helpers."""

from __future__ import annotations

import math


Point = tuple[float, float]


def distance(left: Point, right: Point) -> float:
    """Return Euclidean distance between two points."""
    return round(math.dist(left, right), 2)


def manhattan_distance(left: Point, right: Point) -> float:
    """Return grid distance between two points."""
    return abs(left[0] - right[0]) + abs(left[1] - right[1])
