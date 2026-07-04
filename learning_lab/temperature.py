"""Temperature conversion practice."""

from __future__ import annotations


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return round((fahrenheit - 32) * 5 / 9, 2)


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return round(celsius * 9 / 5 + 32, 2)


def comfort_label(fahrenheit: float) -> str:
    """Return a simple comfort label for a temperature."""
    if fahrenheit < 50:
        return "cold"
    if fahrenheit > 80:
        return "hot"
    return "comfortable"
