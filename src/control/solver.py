"""Two-blank magic square solver (FR-05)."""

from __future__ import annotations

from copy import deepcopy

from src.entity.constants import MAGIC_CONSTANT
from src.entity.errors import UnsolvableDomainError
from src.entity.services.blank_finder import find_blank_coords
from src.entity.services.magic_square_validator import Grid, is_magic_square
from src.entity.services.missing_number_finder import find_not_exist_nums

Solution = list[int]


def solution(grid: Grid) -> Solution:
    """Solve a two-blank puzzle using small-first then reverse attempts.

    Args:
        grid: Validated 4x4 puzzle grid with exactly two blank cells.

    Returns:
        Six-element list [r1, c1, n1, r2, c2, n2] with 1-index coordinates.

    Raises:
        UnsolvableDomainError: When neither assignment yields a magic square.
    """
    blanks = find_blank_coords(grid)
    small, large = find_not_exist_nums(grid)
    first_row, first_col = blanks[0]
    second_row, second_col = blanks[1]

    for first_value, second_value in ((small, large), (large, small)):
        candidate = deepcopy(grid)
        candidate[first_row - 1][first_col - 1] = first_value
        candidate[second_row - 1][second_col - 1] = second_value
        if is_magic_square(candidate):
            return [
                first_row,
                first_col,
                first_value,
                second_row,
                second_col,
                second_value,
            ]

    raise UnsolvableDomainError(
        f"No valid completion for puzzle with magic constant {MAGIC_CONSTANT}."
    )
