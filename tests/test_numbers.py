import pytest

from learning_lab.numbers import add_tax, average, difference, is_even


def test_add_tax_rounds_to_cents():
    assert add_tax(19.99, 0.06) == 21.19


def test_add_tax_rejects_negative_price():
    with pytest.raises(ValueError):
        add_tax(-1, 0.06)


def test_average_uses_all_values():
    assert average([10, 20, 30]) == 20


def test_average_rejects_empty_list():
    with pytest.raises(ValueError):
        average([])


def test_is_even():
    assert is_even(8)
    assert not is_even(9)


def test_difference_returns_absolute_gap():
    assert difference(10, 3) == 7
    assert difference(3, 10) == 7
