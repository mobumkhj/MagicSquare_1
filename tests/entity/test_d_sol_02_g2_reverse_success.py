"""D-SOL-02 — G2 Attempt A fails, Attempt B (reverse) succeeds."""

from __future__ import annotations

from src.control.solver import solution
from tests.conftest import G2


class TestDSol02G2ReverseSuccess:
    """FR-05; I9, I8 — G2 reverse success. Domain Mock 금지."""

    def test_d_sol_02_solution_g2_step_a_fail_step_b_success(self) -> None:
        """D-SOL-02 — G2 reverse attempt succeeds with n1=large, n2=small."""
        # Given: G2 grid
        grid = G2

        # When: solution(grid)
        result = solution(grid)

        # Then: reverse assignment succeeds with n1 > n2
        assert result == [3, 3, 7, 4, 4, 1]
        assert result[2] > result[5]
