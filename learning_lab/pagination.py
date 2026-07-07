"""Pagination practice helpers."""

from __future__ import annotations

import math


def page_count(total_items: int, page_size: int) -> int:
    """Return how many pages are needed."""
    if page_size <= 0:
        raise ValueError("page_size must be positive")
    return math.ceil(total_items / page_size)


def page_slice(page: int, page_size: int) -> slice:
    """Return a slice for one-based page numbers."""
    if page < 1:
        raise ValueError("page must be positive")
    start = (page - 1) * page_size
    return slice(start, start + page_size)
