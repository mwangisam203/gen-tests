"""Itertools practice examples."""

from __future__ import annotations

from itertools import pairwise


def adjacent_pairs(values: list[int]) -> list[tuple[int, int]]:
    """Return neighboring pairs from a list."""
    return list(pairwise(values))


def differences(values: list[int]) -> list[int]:
    """Return differences between neighboring values."""
    return [right - left for left, right in adjacent_pairs(values)]
