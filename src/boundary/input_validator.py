"""Boundary input validation for puzzle grids."""

from __future__ import annotations

from src.boundary.error_response import ErrorResponse
from src.boundary.schemas import (
    E002_CODE,
    E002_MESSAGE,
    E004_CODE,
    E004_MESSAGE,
    E005_CODE,
    E005_MESSAGE,
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
    RESPONSE_TYPE_ERROR,
)
from src.entity.constants import (
    BLANK_CELL_VALUE,
    GRID_SIZE,
    MAX_CELL_VALUE,
    MIN_CELL_VALUE,
)

Grid = list[list[int]] | None


class InputValidator:
    """Validates puzzle grid input before domain resolution."""

    def validate(self, grid: Grid) -> ErrorResponse | None:
        """Validate grid input; return failure response when invalid.

        Args:
            grid: 4x4 puzzle grid or None when omitted.

        Returns:
            ErrorResponse when validation fails; None when valid.
        """
        if grid is None or grid == []:
            return ErrorResponse(
                type=RESPONSE_TYPE_ERROR,
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
            )

        if not self._is_valid_size(grid):
            return ErrorResponse(
                type=RESPONSE_TYPE_ERROR,
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
            )

        blank_count = sum(
            1 for row in grid for cell in row if cell == BLANK_CELL_VALUE
        )
        if blank_count != 2:
            return ErrorResponse(
                type=RESPONSE_TYPE_ERROR,
                code=E002_CODE,
                message=E002_MESSAGE,
            )

        for row in grid:
            for cell in row:
                if cell != BLANK_CELL_VALUE and (
                    cell < MIN_CELL_VALUE or cell > MAX_CELL_VALUE
                ):
                    return ErrorResponse(
                        type=RESPONSE_TYPE_ERROR,
                        code=E004_CODE,
                        message=E004_MESSAGE,
                    )

        seen_non_zero: set[int] = set()
        for row in grid:
            for cell in row:
                if cell == BLANK_CELL_VALUE:
                    continue
                if cell in seen_non_zero:
                    return ErrorResponse(
                        type=RESPONSE_TYPE_ERROR,
                        code=E005_CODE,
                        message=E005_MESSAGE,
                    )
                seen_non_zero.add(cell)

        return None

    def _is_valid_size(self, grid: list[list[int]]) -> bool:
        """Return whether grid has exactly GRID_SIZE rows and columns."""
        if len(grid) != GRID_SIZE:
            return False
        return all(len(row) == GRID_SIZE for row in grid)
