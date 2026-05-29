"""U-FLOW-02 — invalid input never invokes Domain execute (expanded)."""

from __future__ import annotations

import pytest

# from src.boundary.puzzle_boundary import PuzzleBoundary
# from src.control.solve_two_blanks_use_case import SolveTwoBlanksUseCase
# UseCase mock/spy: MagicMock(spec=SolveTwoBlanksUseCase)


class TestUFlow02InvalidNeverCallsExecute:
    """AC-FR-01-*; UX-1; I7 — invalid → execute.call_count == 0."""

    def test_u_flow_02_invalid_size_never_calls_execute(self) -> None:
        """U-FLOW-02a — non-4×4 input → execute not called."""
        # Given: invalid size matrix; execute spy on UseCase mock
        # boundary = PuzzleBoundary(use_case=mock_use_case)
        # When: boundary.solve(invalid_matrix)
        pytest.fail(
            "RED: U-FLOW-02 — invalid size input never calls execute "
            "(call_count == 0)"
        )

    def test_u_flow_02_invalid_empty_count_never_calls_execute(self) -> None:
        """U-FLOW-02b — blank count ≠ 2 → execute not called."""
        # Given: 4×4 with zero count ≠ 2; execute spy
        # When: boundary.solve(invalid_matrix)
        pytest.fail(
            "RED: U-FLOW-02 — invalid empty count never calls execute "
            "(call_count == 0)"
        )

    def test_u_flow_02_invalid_range_never_calls_execute(self) -> None:
        """U-FLOW-02c — out-of-range value → execute not called."""
        # Given: 4×4 with -1 or 17; execute spy
        # When: boundary.solve(invalid_matrix)
        pytest.fail(
            "RED: U-FLOW-02 — invalid value range never calls execute "
            "(call_count == 0)"
        )

    def test_u_flow_02_invalid_duplicate_never_calls_execute(self) -> None:
        """U-FLOW-02d — non-zero duplicate → execute not called."""
        # Given: 4×4 with duplicate non-zero; execute spy
        # When: boundary.solve(invalid_matrix)
        pytest.fail(
            "RED: U-FLOW-02 — invalid duplicate never calls execute "
            "(call_count == 0)"
        )
