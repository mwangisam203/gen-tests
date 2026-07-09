"""Priority queue practice helpers."""

from __future__ import annotations


Task = tuple[int, str]


def add_task(tasks: list[Task], priority: int, name: str) -> list[Task]:
    """Return tasks with a new priority task added."""
    return sorted([*tasks, (priority, name)])


def next_task(tasks: list[Task]) -> str:
    """Return the highest-priority task name."""
    if not tasks:
        raise ValueError("tasks must not be empty")
    return sorted(tasks)[0][1]
