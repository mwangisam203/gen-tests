import pytest

from learning_lab.range_tools import chunk_range, inclusive_range


def test_inclusive_range_includes_stop_value():
    assert inclusive_range(1, 3) == [1, 2, 3]
    assert inclusive_range(3, 1) == [3, 2, 1]


def test_chunk_range_splits_values():
    assert chunk_range(1, 5, 2) == [[1, 2], [3, 4], [5]]


def test_chunk_range_rejects_bad_size():
    with pytest.raises(ValueError):
        chunk_range(1, 5, 0)
