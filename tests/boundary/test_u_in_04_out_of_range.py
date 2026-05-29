"""U-IN-04 — value range validation returns E004."""

from __future__ import annotations

from src.boundary.input_validator import InputValidator
from src.boundary.schemas import E004_CODE, E004_MESSAGE


class TestUIn04OutOfRange:
    """FR-01; AC-FR-01-03; short-circuit after size and empty count."""

    def test_u_in_04_out_of_range_returns_e004(self) -> None:
        """U-IN-04 — -1 or 17 in 4×4 with 2 blanks, no duplicate → E004."""
        # Given: 4×4 matrix containing 17, exactly 2 zeros, no non-zero duplicate
        matrix: list[list[int]] = [
            [17, 2, 3, 4],
            [5, 6, 0, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 0],
        ]
        validator = InputValidator()

        # When: validator.validate(matrix)
        result = validator.validate(matrix)

        # Then: E004 envelope is returned
        assert result is not None
        assert result.code == E004_CODE
        assert result.message == E004_MESSAGE
