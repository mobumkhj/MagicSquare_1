"""U-IN-08 — short-circuit: value range before duplicate."""

from __future__ import annotations

from src.boundary.input_validator import InputValidator
from src.boundary.schemas import E004_CODE, E004_MESSAGE


class TestUIn08ShortCircuitRange:
    """FR-01 short-circuit; range violation before duplicate."""

    def test_u_in_08_range_before_duplicate_returns_e004(self) -> None:
        """U-IN-08 — out-of-range and duplicate with 2 blanks → E004, not E005."""
        # Given: 4×4, 2 blanks, out-of-range cell, and non-zero duplicate
        matrix: list[list[int]] = [
            [17, 2, 3, 4],
            [5, 5, 0, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0],
        ]
        validator = InputValidator()

        # When: validator.validate(matrix)
        result = validator.validate(matrix)

        # Then: range short-circuit returns E004
        assert result is not None
        assert result.code == E004_CODE
        assert result.message == E004_MESSAGE
