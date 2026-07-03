"""Sorting examples."""

from __future__ import annotations


def sort_words_by_length(words: list[str]) -> list[str]:
    """Sort words from shortest to longest."""
    return sorted(words, key=len)


def sort_scores_desc(scores: dict[str, int]) -> list[tuple[str, int]]:
    """Sort name-score pairs from highest score to lowest."""
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)


def unique_sorted(values: list[int]) -> list[int]:
    """Remove duplicates and sort ascending."""
    return sorted(set(values))
