"""Present puzzle boundary outcomes for GUI consumption."""

from __future__ import annotations

from dataclasses import dataclass

from src.boundary.error_response import ErrorResponse
from src.boundary.input_validator import Grid
from src.boundary.puzzle_boundary import PuzzleBoundary
from src.boundary.screen.result_formatter import format_error, format_success

Solution = list[int]


@dataclass(frozen=True)
class PresentationResult:
    """GUI-ready outcome from a puzzle solve attempt."""

    is_success: bool
    text: str
    solution: Solution | None = None


class PuzzlePresenter:
    """Orchestrates PuzzleBoundary and formats results for the screen."""

    def __init__(self, boundary: PuzzleBoundary) -> None:
        """Initialize with injected puzzle boundary.

        Args:
            boundary: Validates input and delegates resolution.
        """
        self._boundary = boundary

    def present(self, grid: Grid) -> PresentationResult:
        """Solve grid and return a presentation result.

        Args:
            grid: 4x4 puzzle grid or None.

        Returns:
            Success or error presentation for GUI display.
        """
        outcome = self._boundary.solve(grid)

        if isinstance(outcome, ErrorResponse):
            return PresentationResult(
                is_success=False,
                text=format_error(outcome),
            )

        return PresentationResult(
            is_success=True,
            text=format_success(outcome),
            solution=list(outcome),
        )
