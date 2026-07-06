"""Geometry practice examples."""

from __future__ import annotations

import math


def rectangle_area(width: float, height: float) -> float:
    """Return the area of a rectangle."""
    return width * height


def circle_area(radius: float) -> float:
    """Return the area of a circle."""
    if radius < 0:
        raise ValueError("radius must be non-negative")
    return round(math.pi * radius * radius, 2)


def triangle_area(base: float, height: float) -> float:
    """Return the area of a triangle."""
    return base * height / 2
