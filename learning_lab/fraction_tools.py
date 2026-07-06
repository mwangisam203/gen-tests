"""Fraction practice examples."""

from __future__ import annotations

from fractions import Fraction


def simplify_fraction(numerator: int, denominator: int) -> Fraction:
    """Return a simplified fraction."""
    return Fraction(numerator, denominator)


def add_fractions(left: tuple[int, int], right: tuple[int, int]) -> Fraction:
    """Add two fractions represented as numerator-denominator pairs."""
    return Fraction(*left) + Fraction(*right)
