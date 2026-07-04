"""Search algorithm practice."""

from __future__ import annotations


def linear_search(values: list[str], target: str) -> int:
    """Return the index of target or -1."""
    for index, value in enumerate(values):
        if value == target:
            return index
    return -1


def binary_search(sorted_values: list[int], target: int) -> int:
    """Return the index of target in a sorted list or -1."""
    low = 0
    high = len(sorted_values) - 1
    while low <= high:
        middle = (low + high) // 2
        if sorted_values[middle] == target:
            return middle
        if sorted_values[middle] < target:
            low = middle + 1
        else:
            high = middle - 1
    return -1
