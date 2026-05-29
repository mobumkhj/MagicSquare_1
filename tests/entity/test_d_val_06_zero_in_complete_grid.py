"""D-VAL-06 — zero in complete grid returns False."""

from __future__ import annotations

from copy import deepcopy

from src.entity.services.magic_square_validator import is_magic_square
from tests.conftest import G0


class TestDVal06ZeroInCompleteGrid:
    """FR-04; I4 — G0 with one zero inserted → False. Domain Mock 금지."""

    def test_d_val_06_is_magic_square_with_zero_in_complete_grid_false(
        self,
    ) -> None:
        """D-VAL-06 — G0 with a zero cell returns False."""
        # Given: G0 copy with one cell replaced by 0
        grid = deepcopy(G0)
        grid[0][0] = 0

        # When: is_magic_square(grid)
        result = is_magic_square(grid)

        # Then: validation returns False
        assert result is False
