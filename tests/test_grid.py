from learning_lab.grid import flatten_grid, grid_shape, transpose


def test_grid_shape_counts_rows_and_columns():
    assert grid_shape([[1, 2], [3, 4], [5, 6]]) == (3, 2)
    assert grid_shape([]) == (0, 0)


def test_flatten_grid_returns_cells_in_row_order():
    assert flatten_grid([[1, 2], [3, 4]]) == [1, 2, 3, 4]


def test_transpose_swaps_rows_and_columns():
    assert transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]
