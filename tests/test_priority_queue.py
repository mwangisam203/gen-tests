import pytest

from learning_lab.priority_queue import add_task, next_task


def test_add_task_keeps_tasks_sorted_by_priority():
    assert add_task([(2, "later")], 1, "now") == [(1, "now"), (2, "later")]


def test_next_task_returns_lowest_priority_number():
    assert next_task([(3, "low"), (1, "high")]) == "high"


def test_next_task_rejects_empty_tasks():
    with pytest.raises(ValueError):
        next_task([])
