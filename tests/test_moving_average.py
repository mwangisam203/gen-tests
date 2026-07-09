import pytest

from learning_lab.moving_average import moving_average


def test_moving_average_calculates_windows():
    assert moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]


def test_moving_average_returns_empty_when_window_is_too_large():
    assert moving_average([1, 2], 3) == []


def test_moving_average_rejects_bad_window():
    with pytest.raises(ValueError):
        moving_average([1, 2], 0)
