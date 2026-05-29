"""Use case: resolve a 4x4 puzzle with exactly two blank cells."""

from __future__ import annotations

from src.control.solver import Solution, solution

Grid = list[list[int]]


class SolveTwoBlanksUseCase:
    """Resolves two-blank magic square puzzles via domain logic."""

    def execute(self, grid: Grid) -> Solution:
        """Run domain resolution for a validated puzzle grid.

        Args:
            grid: Validated 4x4 puzzle grid.

        Returns:
            Six-element solution list.
        """
        return solution(grid)
