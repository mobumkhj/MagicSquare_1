"""D-VAL-05 — invalid set or duplicate returns False."""

from __future__ import annotations

import pytest

# from src.entity.services.magic_square_validator import is_magic_square


class TestDVal05InvalidSetOrDuplicate:
    """FR-04; I4 — grid with 17 or duplicate → False. Domain Mock 금지."""

    def test_d_val_05_is_magic_square_invalid_set_or_duplicate_false(
        self,
    ) -> None:
        """D-VAL-05 — grid containing 17 or duplicate non-zero returns False."""
        # Given: 4×4 grid with value 17 or duplicated non-zero entry
        # When: is_magic_square(grid)
        pytest.fail(
            "RED: D-VAL-05 — invalid number set or duplicate returns False"
        )
