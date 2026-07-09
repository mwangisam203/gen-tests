"""Matrix math practice helpers."""

from __future__ import annotations


Matrix = list[list[int]]


def add_matrices(left: Matrix, right: Matrix) -> Matrix:
    """Add two same-shaped matrices."""
    return [
        [left_value + right_value for left_value, right_value in zip(left_row, right_row)]
        for left_row, right_row in zip(left, right)
    ]


def scalar_multiply(matrix: Matrix, factor: int) -> Matrix:
    """Multiply every matrix cell by a factor."""
    return [[cell * factor for cell in row] for row in matrix]
