"""Range practice helpers."""

from __future__ import annotations


def inclusive_range(start: int, stop: int) -> list[int]:
    """Return an inclusive integer range."""
    step = 1 if start <= stop else -1
    return list(range(start, stop + step, step))


def chunk_range(start: int, stop: int, size: int) -> list[list[int]]:
    """Return an inclusive range split into chunks."""
    if size <= 0:
        raise ValueError("size must be positive")
    values = inclusive_range(start, stop)
    return [values[index : index + size] for index in range(0, len(values), size)]
