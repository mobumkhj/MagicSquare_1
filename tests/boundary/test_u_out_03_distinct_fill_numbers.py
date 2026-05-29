"""U-OUT-03 — successful solve returns distinct fill numbers."""

from __future__ import annotations

from unittest.mock import MagicMock

from src.boundary.puzzle_boundary import PuzzleBoundary
from src.control.solve_two_blanks_use_case import SolveTwoBlanksUseCase
from src.entity.constants import MAX_CELL_VALUE, MIN_CELL_VALUE
from tests.conftest import G1


class TestUOut03DistinctFillNumbers:
    """FR-05 output contract — n1 and n2 are distinct values in [1,16]."""

    def test_u_out_03_solve_valid_returns_distinct_fill_numbers(self) -> None:
        """U-OUT-03 — G1 + mock → n1≠n2, both in [1,16]."""
        # Given: G1 grid; UseCase mock → [2, 2, 7, 3, 3, 10]
        mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
        mock_use_case.execute.return_value = [2, 2, 7, 3, 3, 10]
        boundary = PuzzleBoundary(use_case=mock_use_case)

        # When: boundary.solve(matrix)
        result = boundary.solve(G1)

        # Then: fill numbers are distinct and in range
        _, _, n1, _, _, n2 = result
        assert MIN_CELL_VALUE <= n1 <= MAX_CELL_VALUE
        assert MIN_CELL_VALUE <= n2 <= MAX_CELL_VALUE
        assert n1 != n2
