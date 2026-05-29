"""D-SOL-01 — G1 Attempt A (small-first) success."""

from __future__ import annotations

import pytest

# from src.control.solver import solution


class TestDSol01G1StepASuccess:
    """FR-05; I8, I6 — G1 → [2,2,7,3,3,10] exact. Domain Mock 금지."""

    def test_d_sol_01_solution_g1_step_a_success(self) -> None:
        """D-SOL-01 — G1 small-first attempt returns exact solution array."""
        # Given: G1 grid
        # When: solution(grid)
        pytest.fail(
            "RED: D-SOL-01 — G1 Attempt A returns [2,2,7,3,3,10] exactly"
        )
