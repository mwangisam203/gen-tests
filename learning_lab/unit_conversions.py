"""Unit conversion practice."""

from __future__ import annotations


def miles_to_kilometers(miles: float) -> float:
    """Convert miles to kilometers."""
    return round(miles * 1.60934, 2)


def pounds_to_kilograms(pounds: float) -> float:
    """Convert pounds to kilograms."""
    return round(pounds * 0.45359237, 2)


def inches_to_centimeters(inches: float) -> float:
    """Convert inches to centimeters."""
    return round(inches * 2.54, 2)
