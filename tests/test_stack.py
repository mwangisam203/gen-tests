import pytest

from learning_lab.stack import pop, push


def test_push_appends_item():
    assert push(["a"], "b") == ["a", "b"]


def test_pop_returns_top_and_remaining_stack():
    assert pop(["a", "b"]) == ("b", ["a"])


def test_pop_rejects_empty_stack():
    with pytest.raises(IndexError):
        pop([])
