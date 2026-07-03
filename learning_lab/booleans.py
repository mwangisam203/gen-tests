"""Boolean logic practice."""

from __future__ import annotations


def can_drive(age: int, has_license: bool) -> bool:
    """Return True when a person is old enough and licensed."""
    return age >= 16 and has_license


def should_wear_coat(temperature_f: int, is_raining: bool) -> bool:
    """Return True for chilly or rainy weather."""
    return temperature_f < 50 or is_raining


def exclusive_choice(left: bool, right: bool) -> bool:
    """Return True when exactly one choice is selected."""
    return left != right
