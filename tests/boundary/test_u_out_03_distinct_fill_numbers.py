"""U-OUT-03 — successful solve returns distinct fill numbers."""

from __future__ import annotations

import pytest

# from src.boundary.puzzle_boundary import PuzzleBoundary
# UseCase mock/spy: execute.return_value = [2, 2, 7, 3, 3, 10]


class TestUOut03DistinctFillNumbers:
    """FR-05 output contract — n1 and n2 are distinct values in [1,16]."""

    def test_u_out_03_solve_valid_returns_distinct_fill_numbers(self) -> None:
        """U-OUT-03 — G1 + mock → n1≠n2, both in [1,16]."""
        # Given: G1 grid; UseCase mock → [2, 2, 7, 3, 3, 10]
        # boundary = PuzzleBoundary(use_case=mock_use_case)
        # When: boundary.solve(matrix)
        pytest.fail(
            "RED: U-OUT-03 — solve result n1 and n2 are distinct fill numbers "
            "in [1,16]"
        )
