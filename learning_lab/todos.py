"""Todo list practice examples."""

from __future__ import annotations


Todo = dict[str, str | bool]


def add_todo(todos: list[Todo], title: str) -> list[Todo]:
    """Return a new todo list with one item added."""
    return [*todos, {"title": title, "done": False}]


def complete_todo(todos: list[Todo], title: str) -> list[Todo]:
    """Return a new todo list with a matching title completed."""
    return [{**todo, "done": True} if todo["title"] == title else todo for todo in todos]


def open_todos(todos: list[Todo]) -> list[Todo]:
    """Return todos that are not complete."""
    return [todo for todo in todos if not todo["done"]]
