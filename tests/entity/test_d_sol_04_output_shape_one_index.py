"""D-SOL-04 — successful solution output shape and 1-index contract."""

from __future__ import annotations

from src.control.solver import solution
from src.entity.constants import GRID_SIZE, MAX_CELL_VALUE, MIN_CELL_VALUE
from tests.conftest import G1


class TestDSol04OutputShapeOneIndex:
    """FR-05; I8, I6 — G1 output len=6, coords ∈ [1,4], n1≠n2. Domain Mock 금지."""

    def test_d_sol_04_solution_success_output_shape_one_index(self) -> None:
        """D-SOL-04 — G1 solution has len 6, 1-index coords, distinct n1/n2."""
        # Given: G1 grid
        grid = G1

        # When: solution(grid)
        result = solution(grid)

        # Then: output shape and coordinate contract hold
        assert len(result) == 6
        r1, c1, n1, r2, c2, n2 = result
        assert MIN_CELL_VALUE <= r1 <= GRID_SIZE
        assert MIN_CELL_VALUE <= c1 <= GRID_SIZE
        assert MIN_CELL_VALUE <= r2 <= GRID_SIZE
        assert MIN_CELL_VALUE <= c2 <= GRID_SIZE
        assert MIN_CELL_VALUE <= n1 <= MAX_CELL_VALUE
        assert MIN_CELL_VALUE <= n2 <= MAX_CELL_VALUE
        assert n1 != n2
