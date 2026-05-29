"""U-FLOW-02 — invalid input never invokes Domain execute (expanded)."""

from __future__ import annotations

from unittest.mock import MagicMock

from src.boundary.puzzle_boundary import PuzzleBoundary
from src.boundary.schemas import E002_CODE, E004_CODE, E005_CODE, INVALID_SIZE_CODE
from src.control.solve_two_blanks_use_case import SolveTwoBlanksUseCase


class TestUFlow02InvalidNeverCallsExecute:
    """AC-FR-01-*; UX-1; I7 — invalid → execute.call_count == 0."""

    def test_u_flow_02_invalid_size_never_calls_execute(self) -> None:
        """U-FLOW-02a — non-4×4 input → execute not called."""
        # Given: invalid size matrix; execute spy on UseCase mock
        mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
        boundary = PuzzleBoundary(use_case=mock_use_case)
        invalid_matrix: list[list[int]] = [[1] * 3 for _ in range(3)]

        # When: boundary.solve(invalid_matrix)
        result = boundary.solve(invalid_matrix)

        # Then: size failure and execute not called
        assert result.code == INVALID_SIZE_CODE
        mock_use_case.execute.assert_not_called()

    def test_u_flow_02_invalid_empty_count_never_calls_execute(self) -> None:
        """U-FLOW-02b — blank count ≠ 2 → execute not called."""
        # Given: 4×4 with zero count ≠ 2; execute spy
        mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
        boundary = PuzzleBoundary(use_case=mock_use_case)
        invalid_matrix: list[list[int]] = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]

        # When: boundary.solve(invalid_matrix)
        result = boundary.solve(invalid_matrix)

        # Then: empty-count failure and execute not called
        assert result.code == E002_CODE
        mock_use_case.execute.assert_not_called()

    def test_u_flow_02_invalid_range_never_calls_execute(self) -> None:
        """U-FLOW-02c — out-of-range value → execute not called."""
        # Given: 4×4 with -1 or 17; execute spy
        mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
        boundary = PuzzleBoundary(use_case=mock_use_case)
        invalid_matrix: list[list[int]] = [
            [17, 2, 3, 4],
            [5, 6, 0, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0],
        ]

        # When: boundary.solve(invalid_matrix)
        result = boundary.solve(invalid_matrix)

        # Then: range failure and execute not called
        assert result.code == E004_CODE
        mock_use_case.execute.assert_not_called()

    def test_u_flow_02_invalid_duplicate_never_calls_execute(self) -> None:
        """U-FLOW-02d — non-zero duplicate → execute not called."""
        # Given: 4×4 with duplicate non-zero; execute spy
        mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
        boundary = PuzzleBoundary(use_case=mock_use_case)
        invalid_matrix: list[list[int]] = [
            [1, 2, 3, 4],
            [5, 5, 0, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0],
        ]

        # When: boundary.solve(invalid_matrix)
        result = boundary.solve(invalid_matrix)

        # Then: duplicate failure and execute not called
        assert result.code == E005_CODE
        mock_use_case.execute.assert_not_called()
