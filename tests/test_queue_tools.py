import pytest

from learning_lab.queue_tools import dequeue, enqueue


def test_enqueue_adds_to_back():
    assert enqueue(["a"], "b") == ["a", "b"]


def test_dequeue_removes_from_front():
    assert dequeue(["a", "b"]) == ("a", ["b"])


def test_dequeue_rejects_empty_queue():
    with pytest.raises(IndexError):
        dequeue([])
