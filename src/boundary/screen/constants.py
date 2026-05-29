"""GUI display constants for Magic Square screen."""

from __future__ import annotations

from src.entity.constants import BLANK_CELL_VALUE, GRID_SIZE, MAX_CELL_VALUE

WINDOW_TITLE = "Magic Square 4x4 Solver"
SOLVE_BUTTON_LABEL = "Solve"
LOAD_SAMPLE_BUTTON_LABEL = "Load Sample (G1)"
CLEAR_BUTTON_LABEL = "Clear"
RESULT_PLACEHOLDER = "Enter a 4x4 grid (0 = blank) and click Solve."
CELL_MIN_VALUE = BLANK_CELL_VALUE
CELL_MAX_VALUE = MAX_CELL_VALUE
GRID_DIMENSION = GRID_SIZE

SAMPLE_G1: list[list[int]] = [
    [16, 3, 2, 13],
    [5, 0, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 14, 1],
]
