"""Magic square validation (FR-04)."""

from __future__ import annotations

from src.entity.constants import (
    BLANK_CELL_VALUE,
    GRID_SIZE,
    MAGIC_CONSTANT,
    MAX_CELL_VALUE,
    MIN_CELL_VALUE,
    PUZZLE_CELL_COUNT,
)

Grid = list[list[int]]


def is_magic_square(grid: Grid) -> bool:
    """Return whether a complete 4x4 grid satisfies magic square invariants.

    Args:
        grid: Complete 4x4 grid without blank cells.

    Returns:
        True when row, column, diagonal sums equal MAGIC_CONSTANT and the
        cell set is exactly 1..PUZZLE_CELL_COUNT with no zeros.
    """
    if len(grid) != GRID_SIZE or any(len(row) != GRID_SIZE for row in grid):
        return False

    values = [cell for row in grid for cell in row]
    if BLANK_CELL_VALUE in values:
        return False
    if len(set(values)) != PUZZLE_CELL_COUNT:
        return False
    if sorted(values) != list(range(MIN_CELL_VALUE, MAX_CELL_VALUE + 1)):
        return False

    for row_index in range(GRID_SIZE):
        if sum(grid[row_index]) != MAGIC_CONSTANT:
            return False

    for col_index in range(GRID_SIZE):
        if sum(grid[row][col_index] for row in range(GRID_SIZE)) != MAGIC_CONSTANT:
            return False

    if sum(grid[index][index] for index in range(GRID_SIZE)) != MAGIC_CONSTANT:
        return False
    if (
        sum(grid[index][GRID_SIZE - 1 - index] for index in range(GRID_SIZE))
        != MAGIC_CONSTANT
    ):
        return False

    return True
