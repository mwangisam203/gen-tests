import pytest

from learning_lab.inventory import add_stock, low_stock, remove_stock, total_units


def test_add_stock_returns_updated_copy():
    original = {"pens": 2}

    assert add_stock(original, "pens", 3) == {"pens": 5}
    assert original == {"pens": 2}


def test_add_stock_rejects_negative_amount():
    with pytest.raises(ValueError):
        add_stock({}, "pens", -1)


def test_low_stock_finds_items_at_threshold():
    assert low_stock({"pens": 2, "paper": 10}, threshold=2) == ["pens"]


def test_total_units_sums_counts():
    assert total_units({"pens": 2, "paper": 10}) == 12


def test_remove_stock_returns_updated_copy():
    original = {"pens": 5}

    assert remove_stock(original, "pens", 2) == {"pens": 3}
    assert original == {"pens": 5}


def test_remove_stock_rejects_missing_units():
    with pytest.raises(ValueError):
        remove_stock({"pens": 1}, "pens", 2)
