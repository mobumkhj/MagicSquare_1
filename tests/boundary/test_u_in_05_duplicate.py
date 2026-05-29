"""U-IN-05 — non-zero duplicate validation returns E005."""

from __future__ import annotations

import pytest

# from src.boundary.input_validator import InputValidator


class TestUIn05Duplicate:
    """FR-01; AC-FR-01-04; short-circuit after size, empty count, and range."""

    def test_u_in_05_duplicate_non_zero_returns_e005(self) -> None:
        """U-IN-05 — non-zero duplicate with 2 blanks → E005."""
        # Given: e.g. [[1,2,3,4],[5,5,0,8],[9,10,11,12],[13,14,15,0]]
        # validator = InputValidator()
        # When: validator.validate(matrix)
        pytest.fail(
            "RED: U-IN-05 — non-zero duplicate returns code E005 "
            "with message 'Non-zero values must not duplicate.'"
        )
