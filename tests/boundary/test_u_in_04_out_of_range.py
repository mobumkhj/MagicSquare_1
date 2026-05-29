"""U-IN-04 — value range validation returns E004."""

from __future__ import annotations

import pytest

# from src.boundary.input_validator import InputValidator


class TestUIn04OutOfRange:
    """FR-01; AC-FR-01-03; short-circuit after size and empty count."""

    def test_u_in_04_out_of_range_returns_e004(self) -> None:
        """U-IN-04 — -1 or 17 in 4×4 with 2 blanks, no duplicate → E004."""
        # Given: 4×4 matrix containing -1 or 17, exactly 2 zeros, no non-zero duplicate
        # matrix: list[list[int]] = ...
        # validator = InputValidator()
        # When: validator.validate(matrix)
        pytest.fail(
            "RED: U-IN-04 — out-of-range cell returns code E004 "
            "with message 'Each cell must be 0 or an integer from 1 to 16.'"
        )
