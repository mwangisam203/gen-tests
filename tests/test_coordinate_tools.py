from learning_lab.coordinate_tools import distance, manhattan_distance


def test_distance_uses_euclidean_distance():
    assert distance((0, 0), (3, 4)) == 5


def test_manhattan_distance_adds_axis_gaps():
    assert manhattan_distance((0, 0), (3, 4)) == 7
