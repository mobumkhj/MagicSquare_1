"""U-IN-06 — short-circuit: size violation before empty count."""

from __future__ import annotations

import pytest

# from src.boundary.input_validator import InputValidator


class TestUIn06ShortCircuitSize:
    """FR-01 short-circuit; simultaneous size + empty violations → first code only."""

    def test_u_in_06_size_violation_before_empty_count_returns_e001(self) -> None:
        """U-IN-06 — non-4×4 with wrong blank count → E001, not E002."""
        # Given: matrix with row≠4 or col≠4 AND zero count ≠ 2
        # validator = InputValidator()
        # When: validator.validate(matrix)
        pytest.fail(
            "RED: U-IN-06 — short-circuit returns E001 (size) when size and "
            "empty-count both violate"
        )
