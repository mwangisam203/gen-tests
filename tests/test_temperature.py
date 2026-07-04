from learning_lab.temperature import celsius_to_fahrenheit, comfort_label, fahrenheit_to_celsius


def test_fahrenheit_to_celsius_converts_freezing():
    assert fahrenheit_to_celsius(32) == 0.0


def test_celsius_to_fahrenheit_converts_freezing():
    assert celsius_to_fahrenheit(0) == 32.0


def test_comfort_label_uses_ranges():
    assert comfort_label(45) == "cold"
    assert comfort_label(72) == "comfortable"
    assert comfort_label(90) == "hot"
