import pytest

from learning_lab.quiz import missed_questions, quiz_percent, score_quiz


def test_score_quiz_counts_matches():
    assert score_quiz(["A", "B", "C"], ["A", "C", "C"]) == 2


def test_quiz_percent_uses_answer_key_length():
    assert quiz_percent(["A", "B"], ["A", "C"]) == 50.0


def test_quiz_percent_rejects_empty_key():
    with pytest.raises(ValueError):
        quiz_percent([], [])


def test_missed_questions_returns_one_based_numbers():
    assert missed_questions(["A", "B", "C"], ["A", "C", "C"]) == [2]
