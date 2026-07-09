from learning_lab.histogram import histogram, histogram_lines


def test_histogram_counts_values():
    assert histogram(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_histogram_lines_sorts_keys():
    assert histogram_lines({"b": 1, "a": 2}) == ["a: ##", "b: #"]
