"""D-SOL-04 — successful solution output shape and 1-index contract."""

from __future__ import annotations

import pytest

# from src.control.solver import solution


class TestDSol04OutputShapeOneIndex:
    """FR-05; I8, I6 — G1 output len=6, coords ∈ [1,4], n1≠n2. Domain Mock 금지."""

    def test_d_sol_04_solution_success_output_shape_one_index(self) -> None:
        """D-SOL-04 — G1 solution has len 6, 1-index coords, distinct n1/n2."""
        # Given: G1 grid
        # When: solution(grid)
        pytest.fail(
            "RED: D-SOL-04 — G1 solution len=6, coords in [1,4], n1≠n2"
        )
