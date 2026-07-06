from decimal import Decimal

import pytest

from learning_lab.decimal_money import money, split_bill


def test_money_rounds_half_up_to_cents():
    assert money("10.235") == Decimal("10.24")


def test_split_bill_rounds_each_share():
    assert split_bill("10.00", 3) == Decimal("3.33")


def test_split_bill_rejects_non_positive_people():
    with pytest.raises(ValueError):
        split_bill("10.00", 0)
