from learning_lab.sorting_basics import sort_scores_desc, sort_words_by_length, unique_sorted


def test_sort_words_by_length():
    assert sort_words_by_length(["tests", "I", "write"]) == ["I", "tests", "write"]


def test_sort_scores_desc():
    assert sort_scores_desc({"Ada": 98, "Grace": 95}) == [("Ada", 98), ("Grace", 95)]


def test_unique_sorted_removes_duplicates():
    assert unique_sorted([3, 1, 3, 2]) == [1, 2, 3]
