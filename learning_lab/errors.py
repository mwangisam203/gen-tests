"""Examples for raising and handling errors."""

from __future__ import annotations


def divide(left: float, right: float) -> float:
    """Divide two numbers with a friendly zero check."""
    if right == 0:
        raise ZeroDivisionError("right must not be zero")
    return left / right


def parse_int(text: str, default: int | None = None) -> int:
    """Parse an integer, optionally returning a default."""
    try:
        return int(text)
    except ValueError:
        if default is not None:
            return default
        raise


def require_key(data: dict[str, str], key: str) -> str:
    """Read a required dictionary key."""
    if key not in data:
        raise KeyError(f"missing required key: {key}")
    return data[key]
