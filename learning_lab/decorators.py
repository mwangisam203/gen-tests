"""Decorator practice examples."""

from __future__ import annotations

from collections.abc import Callable
from functools import wraps


def call_counter(function: Callable[..., str]) -> Callable[..., str]:
    """Count how often a function is called."""
    calls = 0

    @wraps(function)
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        wrapper.calls = calls
        return function(*args, **kwargs)

    wrapper.calls = calls
    return wrapper
