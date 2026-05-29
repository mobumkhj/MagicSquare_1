"""Boundary domain failure mapping — DOMAIN_NO_SOLUTION."""

from __future__ import annotations

from unittest.mock import MagicMock

from src.boundary.error_response import ErrorResponse
from src.boundary.puzzle_boundary import PuzzleBoundary
from src.boundary.schemas import DOMAIN_NO_SOLUTION_CODE, DOMAIN_NO_SOLUTION_MESSAGE
from src.control.solve_two_blanks_use_case import SolveTwoBlanksUseCase
from src.entity.errors import UnsolvableDomainError
from tests.conftest import G3


class TestDomainNoSolution:
    """Domain failure converts to DOMAIN_NO_SOLUTION ErrorResponse."""

    def test_submit_no_solution_returns_domain_no_solution_error(self) -> None:
        """Valid grid with no completion returns DOMAIN_NO_SOLUTION envelope."""
        # Given: use case raises UnsolvableDomainError
        mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
        mock_use_case.execute.side_effect = UnsolvableDomainError("no solution")
        boundary = PuzzleBoundary(use_case=mock_use_case)

        # When: submit(G3)
        result = boundary.submit(G3)

        # Then: ErrorResponse with fixed code and message
        assert isinstance(result, ErrorResponse)
        assert result.code == DOMAIN_NO_SOLUTION_CODE
        assert result.message == DOMAIN_NO_SOLUTION_MESSAGE
