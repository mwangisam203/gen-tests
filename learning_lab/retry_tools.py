"""Retry logic practice helpers."""

from __future__ import annotations

from collections.abc import Callable


def retry(function: Callable[[], str], attempts: int = 3) -> str:
    """Call a function until it succeeds or attempts run out."""
    if attempts < 1:
        raise ValueError("attempts must be positive")
    last_error: Exception | None = None
    for _ in range(attempts):
        try:
            return function()
        except Exception as error:
            last_error = error
    assert last_error is not None
    raise last_error
