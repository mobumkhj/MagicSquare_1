"""Boundary input validation for puzzle grids."""

from __future__ import annotations

from src.boundary.schemas import (
    INVALID_SIZE_CODE,
    INVALID_SIZE_MESSAGE,
    RESPONSE_TYPE_ERROR,
    FailureResponse,
)

Grid = list[list[int]] | None


class InputValidator:
    """Validates puzzle grid input before domain resolution."""

    def validate(self, grid: Grid) -> FailureResponse:
        """Validate grid input; return failure response when invalid.

        Args:
            grid: 4x4 puzzle grid or None when omitted.

        Returns:
            FailureResponse when grid is None or empty (INVALID_SIZE).
        """
        if grid is None or grid == []:
            return FailureResponse(
                type=RESPONSE_TYPE_ERROR,
                code=INVALID_SIZE_CODE,
                message=INVALID_SIZE_MESSAGE,
            )
        raise NotImplementedError
