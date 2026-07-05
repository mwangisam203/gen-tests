"""Gradebook practice examples."""

from __future__ import annotations


def letter_grade(score: int) -> str:
    """Convert a numeric score to a letter grade."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def class_average(scores: dict[str, int]) -> float:
    """Return the average score for a gradebook."""
    if not scores:
        raise ValueError("scores must not be empty")
    return sum(scores.values()) / len(scores)


def passing_students(scores: dict[str, int]) -> list[str]:
    """Return names of students with passing scores."""
    return [name for name, score in scores.items() if score >= 60]


def grade_counts(scores: dict[str, int]) -> dict[str, int]:
    """Count how many students earned each letter grade."""
    counts: dict[str, int] = {}
    for score in scores.values():
        grade = letter_grade(score)
        counts[grade] = counts.get(grade, 0) + 1
    return counts
