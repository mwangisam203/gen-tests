from learning_lab.parsing_tools import parse_key_value, parse_tags


def test_parse_key_value_reads_lines():
    assert parse_key_value("name=Ada\nlanguage=Python") == {
        "name": "Ada",
        "language": "Python",
    }


def test_parse_tags_strips_empty_values():
    assert parse_tags("python, tests, , practice") == ["python", "tests", "practice"]
