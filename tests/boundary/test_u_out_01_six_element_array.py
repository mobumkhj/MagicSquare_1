"""U-OUT-01 — successful solve returns six-element result array."""

from __future__ import annotations

from unittest.mock import MagicMock

from src.boundary.error_response import ErrorResponse
from src.boundary.puzzle_boundary import PuzzleBoundary
from src.control.solve_two_blanks_use_case import SolveTwoBlanksUseCase
from tests.conftest import G1


class TestUOut01SixElementArray:
    """FR-05; BR-13; I8 — success envelope with len(result)==6."""

    def test_u_out_01_solve_valid_returns_six_element_array(self) -> None:
        """U-OUT-01 — G1 + mock [2,2,7,3,3,10] → len(result)==6, not Failure."""
        # Given: G1 grid; UseCase mock → [2, 2, 7, 3, 3, 10]
        mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
        mock_use_case.execute.return_value = [2, 2, 7, 3, 3, 10]
        boundary = PuzzleBoundary(use_case=mock_use_case)

        # When: boundary.solve(matrix)
        result = boundary.solve(G1)

        # Then: six-element success array is returned
        assert not isinstance(result, ErrorResponse)
        assert len(result) == 6
