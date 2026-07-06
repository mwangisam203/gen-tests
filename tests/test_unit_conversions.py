from learning_lab.unit_conversions import inches_to_centimeters, miles_to_kilometers, pounds_to_kilograms


def test_miles_to_kilometers_rounds_result():
    assert miles_to_kilometers(1) == 1.61


def test_pounds_to_kilograms_rounds_result():
    assert pounds_to_kilograms(10) == 4.54


def test_inches_to_centimeters_rounds_result():
    assert inches_to_centimeters(12) == 30.48
