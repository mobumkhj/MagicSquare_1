"""U-OUT-02 — successful solve returns 1-indexed coordinates."""

from __future__ import annotations

import pytest

# from src.boundary.puzzle_boundary import PuzzleBoundary
# UseCase mock/spy: execute.return_value = [2, 2, 7, 3, 3, 10]


class TestUOut02OneIndexedCoordinates:
    """FR-05; BR-12; I6, I8 — r1,c1,r2,c2 ∈ [1,4]."""

    def test_u_out_02_solve_valid_returns_one_indexed_coordinates(self) -> None:
        """U-OUT-02 — G1 + mock → all coordinates in [1,4]."""
        # Given: G1 grid; UseCase mock → [2, 2, 7, 3, 3, 10]
        # boundary = PuzzleBoundary(use_case=mock_use_case)
        # When: boundary.solve(matrix)
        pytest.fail(
            "RED: U-OUT-02 — solve result coordinates r1,c1,r2,c2 are 1-indexed "
            "in [1,4]"
        )
