"""Stack practice helpers."""

from __future__ import annotations


def push(stack: list[str], item: str) -> list[str]:
    """Return a stack with an item pushed."""
    return [*stack, item]


def pop(stack: list[str]) -> tuple[str, list[str]]:
    """Pop an item from a stack copy."""
    if not stack:
        raise IndexError("pop from empty stack")
    return stack[-1], stack[:-1]
