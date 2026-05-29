"""U-OUT-02 — successful solve returns 1-indexed coordinates."""

from __future__ import annotations

from unittest.mock import MagicMock

from src.boundary.puzzle_boundary import PuzzleBoundary
from src.control.solve_two_blanks_use_case import SolveTwoBlanksUseCase
from src.entity.constants import GRID_SIZE, MIN_CELL_VALUE
from tests.conftest import G1


class TestUOut02OneIndexedCoordinates:
    """FR-05; BR-12; I6, I8 — r1,c1,r2,c2 ∈ [1,4]."""

    def test_u_out_02_solve_valid_returns_one_indexed_coordinates(self) -> None:
        """U-OUT-02 — G1 + mock → all coordinates in [1,4]."""
        # Given: G1 grid; UseCase mock → [2, 2, 7, 3, 3, 10]
        mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
        mock_use_case.execute.return_value = [2, 2, 7, 3, 3, 10]
        boundary = PuzzleBoundary(use_case=mock_use_case)

        # When: boundary.solve(matrix)
        result = boundary.solve(G1)

        # Then: coordinates are 1-indexed within grid bounds
        r1, c1, _, r2, c2, _ = result
        for coordinate in (r1, c1, r2, c2):
            assert MIN_CELL_VALUE <= coordinate <= GRID_SIZE
