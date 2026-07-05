import pytest

from learning_lab.shopping_cart import cart_total, item_names, line_total, most_expensive_item


ITEMS = [
    {"name": "Notebook", "price": 3.5, "quantity": 2},
    {"name": "Pen", "price": 1.25, "quantity": 4},
]


def test_line_total_multiplies_price_and_quantity():
    assert line_total(ITEMS[0]) == 7.0


def test_cart_total_sums_all_lines():
    assert cart_total(ITEMS) == 12.0


def test_item_names_preserves_order():
    assert item_names(ITEMS) == ["Notebook", "Pen"]


def test_most_expensive_item_returns_item_name():
    assert most_expensive_item(ITEMS) == "Notebook"


def test_most_expensive_item_rejects_empty_cart():
    with pytest.raises(ValueError):
        most_expensive_item([])
