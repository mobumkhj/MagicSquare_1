"""D-MIS-01 — find missing numbers in ascending order."""

from __future__ import annotations

import pytest

# from src.entity.services.missing_number_finder import find_not_exist_nums


class TestDMis01MissingNumbers:
    """FR-03; I11, I1 — G1 → (7, 10) ascending. Domain Mock 금지."""

    def test_d_mis_01_find_not_exist_nums_g1_ascending(self) -> None:
        """D-MIS-01 — G1 missing numbers returned as (7, 10) ascending."""
        # Given: G1 grid
        # When: find_not_exist_nums(grid)
        pytest.fail(
            "RED: D-MIS-01 — G1 missing numbers are (7, 10) in ascending order"
        )
