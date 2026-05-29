"""D-VAL-01 — complete magic square validation (G0 true)."""

from __future__ import annotations

from src.entity.services.magic_square_validator import is_magic_square
from tests.conftest import G0


class TestDVal01MagicSquareG0:
    """FR-04; I1~I5, I4 — G0 complete grid → True. Domain Mock 금지."""

    def test_d_val_01_is_magic_square_g0_complete_true(self) -> None:
        """D-VAL-01 — G0 is a valid complete magic square."""
        # Given: G0 complete magic square grid
        grid = G0

        # When: is_magic_square(grid)
        result = is_magic_square(grid)

        # Then: validation returns True
        assert result is True
