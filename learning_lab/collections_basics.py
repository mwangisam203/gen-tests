"""List and dictionary practice examples."""

from __future__ import annotations


def only_passing(scores: list[int], passing_score: int = 70) -> list[int]:
    """Return scores that are at least the passing score."""
    return [score for score in scores if score >= passing_score]


def count_words(words: list[str]) -> dict[str, int]:
    """Count how often each word appears."""
    counts: dict[str, int] = {}
    for word in words:
        key = word.lower()
        counts[key] = counts.get(key, 0) + 1
    return counts


def top_student(scores: dict[str, int]) -> tuple[str, int]:
    """Return the student with the highest score."""
    if not scores:
        raise ValueError("scores must not be empty")
    return max(scores.items(), key=lambda item: item[1])
