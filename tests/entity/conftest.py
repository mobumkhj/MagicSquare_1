"""Entity-layer grid fixture placeholders (G0~G3)."""

from __future__ import annotations

import pytest

# G0 complete magic square — activate in GREEN phase via tests/conftest.py SSOT
# G1 partial puzzle — blanks (2,2), (3,3) 1-index; missing numbers {7, 10}


@pytest.fixture
def grid_g0() -> None:
    """G0 complete magic square placeholder (RED: not wired)."""
    # return G0 from tests.conftest when fixtures are activated
    return None


@pytest.fixture
def grid_g1() -> None:
    """G1 partial puzzle placeholder (RED: not wired)."""
    # return G1 from tests.conftest when fixtures are activated
    return None


@pytest.fixture
def grid_g2() -> None:
    """G2 reverse-success placeholder (RED: TBD)."""
    return None


@pytest.fixture
def grid_g3() -> None:
    """G3 unsolvable placeholder (RED: TBD)."""
    return None
