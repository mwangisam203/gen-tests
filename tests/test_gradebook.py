import pytest

from learning_lab.gradebook import class_average, letter_grade, passing_students


def test_letter_grade_uses_common_cutoffs():
    assert letter_grade(95) == "A"
    assert letter_grade(82) == "B"
    assert letter_grade(73) == "C"
    assert letter_grade(61) == "D"
    assert letter_grade(40) == "F"


def test_class_average_uses_all_scores():
    assert class_average({"Ada": 100, "Grace": 80}) == 90


def test_class_average_rejects_empty_scores():
    with pytest.raises(ValueError):
        class_average({})


def test_passing_students_returns_names():
    assert passing_students({"Ada": 100, "Grace": 55}) == ["Ada"]
