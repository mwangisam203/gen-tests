import pytest

from learning_lab.bank_account import apply_interest, deposit, withdraw


def test_deposit_adds_money():
    assert deposit(10.0, 2.5) == 12.5


def test_deposit_rejects_non_positive_amounts():
    with pytest.raises(ValueError):
        deposit(10.0, 0)


def test_withdraw_subtracts_money():
    assert withdraw(10.0, 2.5) == 7.5


def test_withdraw_rejects_overdraft():
    with pytest.raises(ValueError):
        withdraw(10.0, 20.0)


def test_apply_interest_adds_rate():
    assert apply_interest(100.0, 0.05) == 105.0
