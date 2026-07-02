"""CSV examples using Python's standard library."""

from __future__ import annotations

import csv
from pathlib import Path


def read_score_rows(path: str | Path) -> list[dict[str, str]]:
    """Read score rows from a CSV file."""
    with Path(path).open(newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def student_average(path: str | Path) -> float:
    """Return the average score from a CSV with a score column."""
    rows = read_score_rows(path)
    scores = [int(row["score"]) for row in rows]
    if not scores:
        raise ValueError("CSV must include at least one score")
    return sum(scores) / len(scores)
