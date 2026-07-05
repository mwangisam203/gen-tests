"""Loop practice with small counting tasks."""

from __future__ import annotations


def countdown(start: int) -> list[int]:
    """Count down from start to zero."""
    if start < 0:
        raise ValueError("start must be non-negative")
    return list(range(start, -1, -1))


def running_totals(values: list[int]) -> list[int]:
    """Return the total after each item is added."""
    totals: list[int] = []
    current = 0
    for value in values:
        current += value
        totals.append(current)
    return totals


def find_first_long_word(words: list[str], min_length: int) -> str | None:
    """Return the first word with at least min_length characters."""
    for word in words:
        if len(word) >= min_length:
            return word
    return None


def repeat_until_stop(words: list[str]) -> list[str]:
    """Return words until the word stop appears."""
    collected: list[str] = []
    for word in words:
        if word.lower() == "stop":
            break
        collected.append(word)
    return collected
