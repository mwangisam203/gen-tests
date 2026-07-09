"""Luhn checksum practice."""

from __future__ import annotations


def luhn_total(number: str) -> int:
    """Return the Luhn checksum total for a string of digits."""
    digits = [int(char) for char in number if char.isdigit()]
    total = 0
    parity = len(digits) % 2
    for index, digit in enumerate(digits):
        if index % 2 == parity:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total


def is_luhn_valid(number: str) -> bool:
    """Return True when a number passes the Luhn check."""
    return luhn_total(number) % 10 == 0
