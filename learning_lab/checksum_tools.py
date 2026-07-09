"""Checksum practice helpers."""

from __future__ import annotations


def digit_sum(text: str) -> int:
    """Return the sum of digit characters in text."""
    return sum(int(char) for char in text if char.isdigit())


def mod10_check_digit(text: str) -> int:
    """Return a simple mod-10 check digit."""
    return (10 - digit_sum(text) % 10) % 10
