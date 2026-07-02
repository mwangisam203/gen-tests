import pytest

np = pytest.importorskip("numpy")

from learning_lab.numpy_basics import describe_array, double_values, make_float_array


def test_make_float_array_sets_dtype():
    array = make_float_array([1, 2, 3])

    assert array.dtype == np.float64


def test_double_values_uses_vectorized_math():
    assert double_values([1, 2, 3]).tolist() == [2.0, 4.0, 6.0]


def test_describe_array_returns_summary_stats():
    assert describe_array([2, 4, 6]) == {"min": 2.0, "max": 6.0, "mean": 4.0}


def test_describe_array_rejects_empty_values():
    with pytest.raises(ValueError):
        describe_array([])
