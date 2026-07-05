import pytest

from learning_lab.math_drills import clamp, is_prime, multiplication_table, percent


def test_multiplication_table_returns_readable_lines():
    assert multiplication_table(3, upto=3) == ["3 x 1 = 3", "3 x 2 = 6", "3 x 3 = 9"]


def test_multiplication_table_rejects_small_limit():
    with pytest.raises(ValueError):
        multiplication_table(3, upto=0)


def test_clamp_keeps_value_in_range():
    assert clamp(12, 1, 10) == 10
    assert clamp(-5, 1, 10) == 1
    assert clamp(5, 1, 10) == 5


def test_percent_rounds_to_two_places():
    assert percent(1, 3) == 33.33


def test_is_prime_detects_prime_numbers():
    assert is_prime(2)
    assert is_prime(13)
    assert not is_prime(1)
    assert not is_prime(12)
