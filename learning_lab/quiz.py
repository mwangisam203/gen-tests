"""Quiz scoring practice."""

from __future__ import annotations


def score_quiz(answers: list[str], key: list[str]) -> int:
    """Return the number of answers that match the answer key."""
    return sum(answer == correct for answer, correct in zip(answers, key))


def quiz_percent(answers: list[str], key: list[str]) -> float:
    """Return a quiz score as a percentage."""
    if not key:
        raise ValueError("key must not be empty")
    return round(score_quiz(answers, key) / len(key) * 100, 2)


def missed_questions(answers: list[str], key: list[str]) -> list[int]:
    """Return one-based question numbers that were missed."""
    return [index + 1 for index, pair in enumerate(zip(answers, key)) if pair[0] != pair[1]]
