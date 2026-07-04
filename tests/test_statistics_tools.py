import pytest

from learning_lab.statistics_tools import median, mode, range_size


def test_median_handles_odd_and_even_lengths():
    assert median([3, 1, 2]) == 2
    assert median([4, 1, 2, 3]) == 2.5


def test_median_rejects_empty_values():
    with pytest.raises(ValueError):
        median([])


def test_mode_returns_most_common_string():
    assert mode(["red", "blue", "red"]) == "red"


def test_range_size_subtracts_min_from_max():
    assert range_size([10, 3, 8]) == 7
