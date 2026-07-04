import pytest

from learning_lab.recursion import factorial, sum_nested


def test_factorial_handles_base_cases():
    assert factorial(0) == 1
    assert factorial(1) == 1


def test_factorial_multiplies_down_to_one():
    assert factorial(5) == 120


def test_factorial_rejects_negative_numbers():
    with pytest.raises(ValueError):
        factorial(-1)


def test_sum_nested_walks_inner_lists():
    assert sum_nested([1, [2, 3], 4]) == 10
