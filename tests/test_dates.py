from datetime import date

from learning_lab.dates import add_week, days_until, is_weekend


def test_days_until_uses_given_today():
    assert days_until(date(2026, 7, 10), today=date(2026, 7, 3)) == 7


def test_add_week_moves_forward_seven_days():
    assert add_week(date(2026, 7, 3)) == date(2026, 7, 10)


def test_is_weekend_detects_saturday_and_sunday():
    assert is_weekend(date(2026, 7, 4))
    assert is_weekend(date(2026, 7, 5))
    assert not is_weekend(date(2026, 7, 6))
