from learning_lab.chessboard import is_valid_square, square_color


def test_square_color_returns_known_colors():
    assert square_color("a1") == "dark"
    assert square_color("h1") == "light"


def test_is_valid_square_checks_file_and_rank():
    assert is_valid_square("e4")
    assert not is_valid_square("i4")
    assert not is_valid_square("e9")
