from learning_lab.matrix_math import add_matrices, scalar_multiply


def test_add_matrices_adds_cells():
    assert add_matrices([[1, 2], [3, 4]], [[10, 20], [30, 40]]) == [[11, 22], [33, 44]]


def test_scalar_multiply_scales_cells():
    assert scalar_multiply([[1, 2], [3, 4]], 3) == [[3, 6], [9, 12]]
