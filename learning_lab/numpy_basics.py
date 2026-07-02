"""NumPy practice examples."""

from __future__ import annotations

import numpy as np


def make_float_array(values: list[int | float]) -> np.ndarray:
    """Create a NumPy array using float values."""
    return np.array(values, dtype=float)


def double_values(values: list[int | float]) -> np.ndarray:
    """Use vectorized math to double every value."""
    return make_float_array(values) * 2


def describe_array(values: list[int | float]) -> dict[str, float]:
    """Return a few summary stats for a list of numbers."""
    array = make_float_array(values)
    if array.size == 0:
        raise ValueError("values must not be empty")
    return {
        "min": float(array.min()),
        "max": float(array.max()),
        "mean": float(array.mean()),
    }
