"""Leaderboard practice examples."""

from __future__ import annotations


def add_score(scores: dict[str, int], name: str, score: int) -> dict[str, int]:
    """Keep the highest score for a player."""
    updated = scores.copy()
    updated[name] = max(score, updated.get(name, score))
    return updated


def top_scores(scores: dict[str, int], limit: int = 3) -> list[tuple[str, int]]:
    """Return the highest scores."""
    return sorted(scores.items(), key=lambda item: item[1], reverse=True)[:limit]
