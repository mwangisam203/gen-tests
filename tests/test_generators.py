from learning_lab.generators import evens_forever, take


def test_take_limits_iterable_values():
    assert take(3, [1, 2, 3, 4, 5]) == [1, 2, 3]


def test_evens_forever_starts_on_even_number():
    assert take(4, evens_forever(3)) == [4, 6, 8, 10]
