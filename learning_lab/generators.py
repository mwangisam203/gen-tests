"""Generator practice."""

from __future__ import annotations

from collections.abc import Iterable, Iterator


def take(limit: int, values: Iterable[int]) -> list[int]:
    """Take up to limit values from an iterable."""
    result: list[int] = []
    for value in values:
        if len(result) == limit:
            break
        result.append(value)
    return result


def evens_forever(start: int = 0) -> Iterator[int]:
    """Yield even numbers forever."""
    current = start if start % 2 == 0 else start + 1
    while True:
        yield current
        current += 2
