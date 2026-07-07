"""Schedule practice helpers."""

from __future__ import annotations

from datetime import time


def overlaps(start: time, end: time, other_start: time, other_end: time) -> bool:
    """Return True when two time ranges overlap."""
    return start < other_end and other_start < end


def minutes_since_midnight(value: time) -> int:
    """Return minutes since 00:00."""
    return value.hour * 60 + value.minute
