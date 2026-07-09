"""Binary number practice helpers."""

from __future__ import annotations


def int_to_binary(number: int) -> str:
    """Convert a non-negative integer to binary digits."""
    if number < 0:
        raise ValueError("number must be non-negative")
    return bin(number).removeprefix("0b")


def binary_to_int(bits: str) -> int:
    """Convert binary digits to an integer."""
    if not bits or any(bit not in "01" for bit in bits):
        raise ValueError("bits must contain only 0 and 1")
    return int(bits, 2)
