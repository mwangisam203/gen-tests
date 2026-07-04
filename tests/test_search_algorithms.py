from learning_lab.search_algorithms import binary_search, linear_search


def test_linear_search_returns_index_or_minus_one():
    assert linear_search(["a", "b", "c"], "b") == 1
    assert linear_search(["a", "b", "c"], "z") == -1


def test_binary_search_returns_index_for_sorted_values():
    assert binary_search([1, 3, 5, 7], 5) == 2


def test_binary_search_returns_minus_one_when_missing():
    assert binary_search([1, 3, 5, 7], 4) == -1
