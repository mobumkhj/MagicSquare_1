"""D-LOC-01 — find blank coordinates in row-major order (1-index)."""

from __future__ import annotations

import pytest

# from src.entity.services.blank_finder import find_blank_coords


class TestDLoc01BlankCoords:
    """FR-02; I6 — G1 → (2,2), (3,3) 1-index. Domain Mock 금지."""

    def test_d_loc_01_find_blank_coords_g1_row_major(self) -> None:
        """D-LOC-01 — G1 row-major scan returns 1-index blank coordinates."""
        # Given: G1 grid
        # When: find_blank_coords(grid)
        pytest.fail(
            "RED: D-LOC-01 — G1 row-major blank coords are (2,2) and (3,3) "
            "1-indexed"
        )
