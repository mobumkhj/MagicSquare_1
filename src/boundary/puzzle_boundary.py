"""Boundary orchestration for puzzle submission."""

from __future__ import annotations

from typing import Any

from src.boundary.error_response import ErrorResponse
from src.boundary.input_validator import Grid, InputValidator


class PuzzleBoundary:
    """Submits puzzles after validation; delegates resolution to control layer."""

    def __init__(self, use_case: Any) -> None:
        """Initialize with injected resolve use case.

        Args:
            use_case: SolveTwoBlanksUseCase (or test double).
        """
        self._use_case = use_case
        self._validator = InputValidator()

    def submit(self, grid: Grid) -> ErrorResponse | Any:
        """Validate grid; on failure return error without calling use case.

        Args:
            grid: Puzzle grid or None.

        Returns:
            ErrorResponse when validation fails; otherwise use case result.
        """
        validation = self._validator.validate(grid)
        if validation is not None:
            return validation
        return self._use_case.execute(grid)

    def solve(self, grid: Grid) -> ErrorResponse | Any:
        """Validate and resolve a puzzle grid.

        Args:
            grid: Puzzle grid or None.

        Returns:
            ErrorResponse when validation fails; otherwise use case result.
        """
        return self.submit(grid)
