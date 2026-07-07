import pytest

from learning_lab.pagination import page_count, page_slice


def test_page_count_rounds_up():
    assert page_count(21, 10) == 3


def test_page_count_rejects_bad_page_size():
    with pytest.raises(ValueError):
        page_count(10, 0)


def test_page_slice_returns_offsets_for_one_based_page():
    values = list(range(10))

    assert values[page_slice(2, 3)] == [3, 4, 5]
