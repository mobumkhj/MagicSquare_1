"""U-IN-05 — non-zero duplicate validation returns E005."""

from __future__ import annotations

from src.boundary.input_validator import InputValidator
from src.boundary.schemas import E005_CODE, E005_MESSAGE


class TestUIn05Duplicate:
    """FR-01; AC-FR-01-04; short-circuit after size, empty count, and range."""

    def test_u_in_05_duplicate_non_zero_returns_e005(self) -> None:
        """U-IN-05 — non-zero duplicate with 2 blanks → E005."""
        # Given: duplicate non-zero with exactly two blanks
        matrix: list[list[int]] = [
            [1, 2, 3, 4],
            [5, 5, 0, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0],
        ]
        validator = InputValidator()

        # When: validator.validate(matrix)
        result = validator.validate(matrix)

        # Then: E005 envelope is returned
        assert result is not None
        assert result.code == E005_CODE
        assert result.message == E005_MESSAGE
