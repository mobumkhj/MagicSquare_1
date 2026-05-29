"""D-VAL-04 — diagonal sum mismatch returns False."""

from __future__ import annotations

from copy import deepcopy

from src.entity.services.magic_square_validator import is_magic_square
from tests.conftest import G0


class TestDVal04DiagSumMismatch:
    """FR-04; I3, I4 — G0 with diagonal sum ≠ 34 → False. Domain Mock 금지."""

    def test_d_val_04_is_magic_square_diag_sum_mismatch_false(self) -> None:
        """D-VAL-04 — G0 variant with diagonal sum ≠ 34 returns False."""
        # Given: G0 copy with main diagonal sum altered to ≠ 34
        grid = deepcopy(G0)
        grid[0][0] = 17

        # When: is_magic_square(grid)
        result = is_magic_square(grid)

        # Then: validation returns False
        assert result is False
