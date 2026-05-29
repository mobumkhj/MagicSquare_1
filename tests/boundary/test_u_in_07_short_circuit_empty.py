"""U-IN-07 — short-circuit: empty count before value range."""

from __future__ import annotations

import pytest

# from src.boundary.input_validator import InputValidator


class TestUIn07ShortCircuitEmpty:
    """FR-01 short-circuit; empty count violation before range."""

    def test_u_in_07_empty_count_before_range_returns_e002(self) -> None:
        """U-IN-07 — blank count ≠ 2 with out-of-range value → E002, not E004."""
        # Given: valid 4×4 size, zero count ≠ 2, and a cell outside 0..16
        # validator = InputValidator()
        # When: validator.validate(matrix)
        pytest.fail(
            "RED: U-IN-07 — short-circuit returns E002 (empty count) when empty "
            "count and range both violate"
        )
