"""Dataclass examples."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Student:
    name: str
    score: int


def honor_roll(students: list[Student], minimum_score: int = 90) -> list[Student]:
    """Return students at or above the minimum score."""
    return [student for student in students if student.score >= minimum_score]


def student_label(student: Student) -> str:
    """Return a readable label for a student."""
    return f"{student.name}: {student.score}"
