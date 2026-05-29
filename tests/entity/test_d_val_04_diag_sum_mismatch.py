"""D-VAL-04 — diagonal sum mismatch returns False."""

from __future__ import annotations

import pytest

# from src.entity.services.magic_square_validator import is_magic_square


class TestDVal04DiagSumMismatch:
    """FR-04; I3, I4 — G0 with diagonal sum ≠ 34 → False. Domain Mock 금지."""

    def test_d_val_04_is_magic_square_diag_sum_mismatch_false(self) -> None:
        """D-VAL-04 — G0 variant with diagonal sum ≠ 34 returns False."""
        # Given: G0 copy with main or anti-diagonal sum altered to ≠ 34
        # When: is_magic_square(grid)
        pytest.fail(
            "RED: D-VAL-04 — diagonal sum mismatch on G0 variant returns False"
        )
