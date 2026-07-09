"""Moving average practice helpers."""

from __future__ import annotations


def moving_average(values: list[float], window: int) -> list[float]:
    """Return simple moving averages."""
    if window <= 0:
        raise ValueError("window must be positive")
    if window > len(values):
        return []
    return [
        sum(values[index : index + window]) / window
        for index in range(len(values) - window + 1)
    ]
