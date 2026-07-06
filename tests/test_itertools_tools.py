from learning_lab.itertools_tools import adjacent_pairs, differences


def test_adjacent_pairs_returns_neighbors():
    assert adjacent_pairs([1, 2, 4]) == [(1, 2), (2, 4)]


def test_differences_subtracts_neighbors():
    assert differences([1, 2, 4]) == [1, 2]
