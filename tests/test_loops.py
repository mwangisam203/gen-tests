import pytest

from learning_lab.loops import countdown, find_first_long_word, running_totals


def test_countdown_includes_zero():
    assert countdown(3) == [3, 2, 1, 0]


def test_countdown_rejects_negative_start():
    with pytest.raises(ValueError):
        countdown(-1)


def test_running_totals_tracks_each_step():
    assert running_totals([2, 3, 5]) == [2, 5, 10]


def test_find_first_long_word_returns_none_when_missing():
    assert find_first_long_word(["hi", "there"], 6) is None
    assert find_first_long_word(["hi", "there"], 5) == "there"
