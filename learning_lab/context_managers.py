"""Context manager practice examples."""

from __future__ import annotations

from contextlib import contextmanager
from collections.abc import Iterator


@contextmanager
def temporary_value(data: dict[str, str], key: str, value: str) -> Iterator[None]:
    """Temporarily set a dictionary value."""
    original = data.get(key)
    had_key = key in data
    data[key] = value
    try:
        yield
    finally:
        if had_key:
            data[key] = original or ""
        else:
            data.pop(key, None)
