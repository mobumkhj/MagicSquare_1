"""U-IN-08 — short-circuit: value range before duplicate."""

from __future__ import annotations

import pytest

# from src.boundary.input_validator import InputValidator


class TestUIn08ShortCircuitRange:
    """FR-01 short-circuit; range violation before duplicate."""

    def test_u_in_08_range_before_duplicate_returns_e004(self) -> None:
        """U-IN-08 — out-of-range and duplicate with 2 blanks → E004, not E005."""
        # Given: 4×4, 2 blanks, out-of-range cell, and non-zero duplicate
        # validator = InputValidator()
        # When: validator.validate(matrix)
        pytest.fail(
            "RED: U-IN-08 — short-circuit returns E004 (range) when range and "
            "duplicate both violate"
        )
