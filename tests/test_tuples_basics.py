from learning_lab.tuples_basics import midpoint, move_point, swap_pair


def test_move_point_offsets_coordinates():
    assert move_point((2, 3), dx=4, dy=-1) == (6, 2)


def test_midpoint_averages_coordinates():
    assert midpoint((0, 0), (4, 6)) == (2.0, 3.0)


def test_swap_pair_reverses_two_values():
    assert swap_pair(("left", "right")) == ("right", "left")
