"""Grid and matrix practice examples."""

from __future__ import annotations


Grid = list[list[int]]


def grid_shape(grid: Grid) -> tuple[int, int]:
    """Return row and column counts."""
    rows = len(grid)
    columns = len(grid[0]) if rows else 0
    return rows, columns


def flatten_grid(grid: Grid) -> list[int]:
    """Flatten a grid into one list."""
    return [cell for row in grid for cell in row]


def transpose(grid: Grid) -> Grid:
    """Swap rows and columns."""
    if not grid:
        return []
    return [list(column) for column in zip(*grid)]
