"""U-IN-07 — short-circuit: empty count before value range."""

from __future__ import annotations

from src.boundary.input_validator import InputValidator
from src.boundary.schemas import E002_CODE, E002_MESSAGE


class TestUIn07ShortCircuitEmpty:
    """FR-01 short-circuit; empty count violation before range."""

    def test_u_in_07_empty_count_before_range_returns_e002(self) -> None:
        """U-IN-07 — blank count ≠ 2 with out-of-range value → E002, not E004."""
        # Given: valid 4×4 size, zero count ≠ 2, and a cell outside 0..16
        matrix: list[list[int]] = [
            [17, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
        validator = InputValidator()

        # When: validator.validate(matrix)
        result = validator.validate(matrix)

        # Then: empty-count short-circuit returns E002
        assert result is not None
        assert result.code == E002_CODE
        assert result.message == E002_MESSAGE
