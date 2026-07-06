"""Decimal money practice examples."""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP


CENT = Decimal("0.01")


def money(value: str) -> Decimal:
    """Parse and round a string as money."""
    return Decimal(value).quantize(CENT, rounding=ROUND_HALF_UP)


def split_bill(total: str, people: int) -> Decimal:
    """Split a bill evenly across people."""
    if people <= 0:
        raise ValueError("people must be positive")
    return (money(total) / people).quantize(CENT, rounding=ROUND_HALF_UP)
