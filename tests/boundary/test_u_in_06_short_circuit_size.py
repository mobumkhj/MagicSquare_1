"""U-IN-06 — short-circuit: size violation before empty count."""

from __future__ import annotations

from src.boundary.input_validator import InputValidator
from src.boundary.schemas import INVALID_SIZE_CODE


class TestUIn06ShortCircuitSize:
    """FR-01 short-circuit; simultaneous size + empty violations → first code only."""

    def test_u_in_06_size_violation_before_empty_count_returns_e001(self) -> None:
        """U-IN-06 — non-4×4 with wrong blank count → size code, not E002."""
        # Given: matrix with row≠4 and zero count ≠ 2
        matrix: list[list[int]] = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
            [1, 2, 3, 4],
        ]
        validator = InputValidator()

        # When: validator.validate(matrix)
        result = validator.validate(matrix)

        # Then: size short-circuit returns INVALID_SIZE (AC-FR anchor)
        assert result is not None
        assert result.code == INVALID_SIZE_CODE
