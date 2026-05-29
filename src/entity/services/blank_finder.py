"""Blank coordinate discovery (FR-02)."""

from __future__ import annotations

from src.entity.constants import BLANK_CELL_VALUE, GRID_SIZE

Grid = list[list[int]]


def find_blank_coords(grid: Grid) -> list[tuple[int, int]]:
    """Return 1-index blank coordinates in row-major order.

    Args:
        grid: 4x4 puzzle grid with 0 marking blank cells.

    Returns:
        List of (row, col) tuples in 1-index row-major scan order.
    """
    blanks: list[tuple[int, int]] = []
    for row_index in range(GRID_SIZE):
        for col_index in range(GRID_SIZE):
            if grid[row_index][col_index] == BLANK_CELL_VALUE:
                blanks.append((row_index + 1, col_index + 1))
    return blanks
