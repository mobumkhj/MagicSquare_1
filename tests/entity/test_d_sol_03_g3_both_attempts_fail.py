"""D-SOL-03 — G3 both attempts fail with UnsolvableDomainError."""

from __future__ import annotations

import pytest

from src.control.solver import solution
from src.entity.errors import UnsolvableDomainError
from tests.conftest import G3


class TestDSol03G3BothAttemptsFail:
    """FR-05; I10, I7 — G3 unsolvable. Domain Mock 금지."""

    def test_d_sol_03_solution_g3_both_attempts_fail(self) -> None:
        """D-SOL-03 — G3 raises UnsolvableDomainError; result len ≠ 6."""
        # Given: G3 grid
        grid = G3

        # When / Then: solution raises UnsolvableDomainError
        with pytest.raises(UnsolvableDomainError):
            solution(grid)
