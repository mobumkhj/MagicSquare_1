"""Convert UI cell values into puzzle grid contract."""

from __future__ import annotations

from src.entity.constants import GRID_SIZE

Grid = list[list[int]]


def read_grid_from_cell_values(cells: list[list[int]]) -> Grid:
    """Read a 4x4 grid from UI cell values.

    Args:
        cells: 4x4 matrix of cell values (0 = blank, 1-16 = filled).

    Returns:
        Puzzle grid as list[list[int]].

    Raises:
        ValueError: When cells is not exactly 4x4.
    """
    if len(cells) != GRID_SIZE:
        raise ValueError(f"Grid must be 4x4, got {len(cells)} rows.")
    for row_index, row in enumerate(cells):
        if len(row) != GRID_SIZE:
            raise ValueError(
                f"Grid must be 4x4, row {row_index + 1} has {len(row)} columns."
            )
    return [list(row) for row in cells]
