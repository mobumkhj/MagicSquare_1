"""Screen puzzle presenter — orchestrates boundary solve for GUI."""

from __future__ import annotations

from unittest.mock import MagicMock

from src.boundary.error_response import ErrorResponse
from src.boundary.puzzle_boundary import PuzzleBoundary
from src.boundary.schemas import RESPONSE_TYPE_ERROR
from src.boundary.screen.puzzle_presenter import PuzzlePresenter
from src.control.solve_two_blanks_use_case import SolveTwoBlanksUseCase
from src.entity.errors import UnsolvableDomainError
from tests.conftest import G1, G3


class TestPuzzlePresenter:
    """Presenter converts boundary outcomes to GUI-friendly results."""

    def test_present_success_returns_formatted_solution(self) -> None:
        """Valid grid returns success presentation with solution text."""
        # Given: boundary mock returning six-element solution
        mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
        mock_use_case.execute.return_value = [2, 2, 10, 3, 3, 7]
        presenter = PuzzlePresenter(boundary=PuzzleBoundary(use_case=mock_use_case))

        # When: present(G1)
        result = presenter.present(G1)

        # Then: success with formatted text
        assert result.is_success is True
        assert "10" in result.text

    def test_present_validation_error_returns_error_text(self) -> None:
        """Invalid grid returns error presentation without calling use case."""
        # Given: boundary with mock use case
        mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
        presenter = PuzzlePresenter(boundary=PuzzleBoundary(use_case=mock_use_case))

        # When: present(None)
        result = presenter.present(None)

        # Then: error text; execute not called
        assert result.is_success is False
        assert "INVALID_SIZE" in result.text
        mock_use_case.execute.assert_not_called()

    def test_present_domain_failure_returns_no_solution_message(self) -> None:
        """Unsolvable puzzle returns DOMAIN_NO_SOLUTION presentation."""
        # Given: use case raises UnsolvableDomainError for G3
        mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
        mock_use_case.execute.side_effect = UnsolvableDomainError("no solution")
        presenter = PuzzlePresenter(boundary=PuzzleBoundary(use_case=mock_use_case))

        # When: present(G3)
        result = presenter.present(G3)

        # Then: domain no-solution message
        assert result.is_success is False
        assert "DOMAIN_NO_SOLUTION" in result.text
        assert "No valid magic square completion exists." in result.text

    def test_present_integration_g1_end_to_end(self) -> None:
        """Real use case resolves G1 through presenter."""
        # Given: wired boundary with real use case
        boundary = PuzzleBoundary(use_case=SolveTwoBlanksUseCase())
        presenter = PuzzlePresenter(boundary=boundary)

        # When: present(G1)
        result = presenter.present(G1)

        # Then: success with expected solution values
        assert result.is_success is True
        assert result.solution == [2, 2, 10, 3, 3, 7]
