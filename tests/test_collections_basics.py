import pytest

from learning_lab.collections_basics import count_words, flatten_once, only_passing, top_student


def test_only_passing_filters_scores():
    assert only_passing([55, 70, 88, 69]) == [70, 88]


def test_count_words_ignores_case():
    assert count_words(["Python", "python", "Tests"]) == {"python": 2, "tests": 1}


def test_top_student_returns_highest_score():
    assert top_student({"Ada": 98, "Grace": 95}) == ("Ada", 98)


def test_top_student_rejects_empty_scores():
    with pytest.raises(ValueError):
        top_student({})


def test_flatten_once_combines_nested_lists():
    assert flatten_once([["a", "b"], ["c"]]) == ["a", "b", "c"]
