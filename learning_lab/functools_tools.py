"""Functools practice examples."""

from __future__ import annotations

from functools import reduce


def product(values: list[int]) -> int:
    """Multiply all values together."""
    return reduce(lambda left, right: left * right, values, 1)


def pipe(value: str, functions: list) -> str:
    """Send a value through a list of single-argument functions."""
    return reduce(lambda current, function: function(current), functions, value)
