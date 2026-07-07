"""Payroll practice helpers."""

from __future__ import annotations


def regular_pay(hours: float, rate: float) -> float:
    """Return pay without overtime."""
    return round(hours * rate, 2)


def weekly_pay(hours: float, rate: float) -> float:
    """Return weekly pay with time-and-a-half overtime."""
    regular_hours = min(hours, 40)
    overtime_hours = max(hours - 40, 0)
    return round(regular_hours * rate + overtime_hours * rate * 1.5, 2)
