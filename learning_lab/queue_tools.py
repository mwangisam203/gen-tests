"""Queue practice helpers."""

from __future__ import annotations


def enqueue(queue: list[str], item: str) -> list[str]:
    """Return a queue with an item added to the back."""
    return [*queue, item]


def dequeue(queue: list[str]) -> tuple[str, list[str]]:
    """Remove an item from the front of a queue copy."""
    if not queue:
        raise IndexError("dequeue from empty queue")
    return queue[0], queue[1:]
