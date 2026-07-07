import pytest

from learning_lab.ascii_art import box, staircase


def test_box_wraps_text_with_border():
    assert box("Hi") == "+----+\n| Hi |\n+----+"


def test_staircase_draws_steps():
    assert staircase(3) == "#\n##\n###"


def test_staircase_rejects_non_positive_steps():
    with pytest.raises(ValueError):
        staircase(0)
