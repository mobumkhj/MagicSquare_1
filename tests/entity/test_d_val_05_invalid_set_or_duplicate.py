"""D-VAL-05 — invalid set or duplicate returns False."""

from __future__ import annotations

from src.entity.services.magic_square_validator import is_magic_square


class TestDVal05InvalidSetOrDuplicate:
    """FR-04; I4 — grid with 17 or duplicate → False. Domain Mock 금지."""

    def test_d_val_05_is_magic_square_invalid_set_or_duplicate_false(
        self,
    ) -> None:
        """D-VAL-05 — grid containing 17 or duplicate non-zero returns False."""
        # Given: 4×4 grid with value 17
        grid: list[list[int]] = [
            [17, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]

        # When: is_magic_square(grid)
        result = is_magic_square(grid)

        # Then: validation returns False
        assert result is False
