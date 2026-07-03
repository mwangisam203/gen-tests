from learning_lab.dataclass_basics import Student, honor_roll, student_label


def test_student_label_formats_name_and_score():
    assert student_label(Student("Ada", 98)) == "Ada: 98"


def test_honor_roll_filters_by_score():
    students = [Student("Ada", 98), Student("Grace", 85)]

    assert honor_roll(students) == [Student("Ada", 98)]
