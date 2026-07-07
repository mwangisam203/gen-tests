from learning_lab.payroll import regular_pay, weekly_pay


def test_regular_pay_multiplies_hours_and_rate():
    assert regular_pay(10, 15) == 150


def test_weekly_pay_uses_overtime_after_forty_hours():
    assert weekly_pay(45, 10) == 475
