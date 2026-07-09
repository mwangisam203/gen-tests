"""Histogram practice helpers."""

from __future__ import annotations


def histogram(values: list[str]) -> dict[str, int]:
    """Count values in a list."""
    counts: dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1
    return counts


def histogram_lines(counts: dict[str, int]) -> list[str]:
    """Return text lines for a small histogram."""
    return [f"{key}: {'#' * counts[key]}" for key in sorted(counts)]
