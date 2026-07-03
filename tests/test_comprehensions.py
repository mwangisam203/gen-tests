from learning_lab.comprehensions import index_by_first_letter, invert_lookup, squares


def test_squares_maps_each_value():
    assert squares([1, 2, 3, 4]) == [1, 4, 9, 16]


def test_index_by_first_letter_groups_names():
    assert index_by_first_letter(["Ada", "Alan", "Grace"]) == {
        "A": ["Ada", "Alan"],
        "G": ["Grace"],
    }


def test_invert_lookup_swaps_keys_and_values():
    assert invert_lookup({"ky": "Kentucky", "tn": "Tennessee"}) == {
        "Kentucky": "ky",
        "Tennessee": "tn",
    }
