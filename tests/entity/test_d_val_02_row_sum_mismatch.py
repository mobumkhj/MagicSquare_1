"""D-VAL-02 — row sum mismatch returns False."""

from __future__ import annotations

import pytest

# from src.entity.services.magic_square_validator import is_magic_square


class TestDVal02RowSumMismatch:
    """FR-04; I1, I4 — G0 with one row sum ≠ 34 → False. Domain Mock 금지."""

    def test_d_val_02_is_magic_square_row_sum_mismatch_false(self) -> None:
        """D-VAL-02 — G0 variant with row sum ≠ 34 returns False."""
        # Given: G0 copy with one row sum altered to ≠ 34
        # When: is_magic_square(grid)
        pytest.fail(
            "RED: D-VAL-02 — row sum mismatch on G0 variant returns False"
        )
