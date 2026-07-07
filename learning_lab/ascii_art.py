"""ASCII art practice helpers."""

from __future__ import annotations


def box(text: str) -> str:
    """Draw a small text box."""
    border = "+" + "-" * (len(text) + 2) + "+"
    return f"{border}\n| {text} |\n{border}"


def staircase(steps: int) -> str:
    """Draw a right-aligned staircase."""
    if steps < 1:
        raise ValueError("steps must be positive")
    return "\n".join("#" * step for step in range(1, steps + 1))
