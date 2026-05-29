"""Missing number discovery (FR-03)."""

from __future__ import annotations

from src.entity.constants import BLANK_CELL_VALUE, PUZZLE_CELL_COUNT

Grid = list[list[int]]


def find_not_exist_nums(grid: Grid) -> tuple[int, int]:
    """Return missing puzzle values in ascending order.

    Args:
        grid: 4x4 puzzle grid with 0 marking blank cells.

    Returns:
        Tuple (small, large) of values in 1..PUZZLE_CELL_COUNT not present
        in non-blank cells.
    """
    present = {
        cell
        for row in grid
        for cell in row
        if cell != BLANK_CELL_VALUE
    }
    missing = sorted(
        value for value in range(1, PUZZLE_CELL_COUNT + 1) if value not in present
    )
    return (missing[0], missing[1])
