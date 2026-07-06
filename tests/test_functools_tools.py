from learning_lab.functools_tools import pipe, product


def test_product_multiplies_values():
    assert product([2, 3, 4]) == 24


def test_product_returns_one_for_empty_values():
    assert product([]) == 1


def test_pipe_applies_functions_in_order():
    assert pipe(" ada ", [str.strip, str.title]) == "Ada"
