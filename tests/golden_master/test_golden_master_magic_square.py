"""GM-2 — Golden Master regression tests for Magic Square Solver."""

from __future__ import annotations

from pathlib import Path

import pytest

from src.boundary.error_response import ErrorResponse
from tests.golden_master.approve import (
    assert_matches_golden_master,
    assert_scenario_matches_golden_master,
)
from tests.golden_master.scenarios import (
    GM_TC_01,
    GM_TC_02,
    GM_TC_03,
    GM_TC_04,
    GM_TC_05,
    GoldenScenario,
    ScenarioKind,
)
from tests.golden_master.serializer import capture_scenario_outcome
from tests.golden_master.validators import (
    validate_error_contract,
    validate_success_contract,
)

EXPECTED_PATH = Path("tests/golden_master_expected.txt")
pytestmark = pytest.mark.golden_master


def _run_golden_master_case(scenario: GoldenScenario) -> None:
    """Execute one Golden Master scenario with contract and baseline checks.

    Args:
        scenario: Scenario under test.
    """
    outcome = capture_scenario_outcome(scenario)

    if scenario.kind in {ScenarioKind.SUCCESS_SMALL_FIRST, ScenarioKind.SUCCESS_REVERSE}:
        assert isinstance(outcome, list)
        validate_success_contract(scenario.grid, outcome, kind=scenario.kind)
    else:
        assert isinstance(outcome, ErrorResponse)
        assert scenario.expected_error_code is not None
        validate_error_contract(outcome, scenario.expected_error_code)

    assert_scenario_matches_golden_master(scenario, EXPECTED_PATH)


class TestGoldenMasterMagicSquare:
    """Approval-pattern Golden Master suite for Magic Square Solver."""

    def test_gm_tc_01_normal_success(self) -> None:
        """GM-TC-01 — small-first combination succeeds with int[6] contract."""
        # Given: normal success grid with Attempt 1 path
        # When/Then: contract validation + baseline approve/compare
        _run_golden_master_case(GM_TC_01)

    def test_gm_tc_02_reverse_success(self) -> None:
        """GM-TC-02 — reverse fallback succeeds after Attempt 1 failure."""
        # Given: reverse-only success grid
        # When/Then: reverse ordering contract + baseline approve/compare
        _run_golden_master_case(GM_TC_02)

    def test_gm_tc_03_invalid_blank_count(self) -> None:
        """GM-TC-03 — blank count violation returns INVALID_EMPTY_COUNT (E002)."""
        # Given: grid with zero blank cells
        # When/Then: error contract + baseline approve/compare
        _run_golden_master_case(GM_TC_03)

    def test_gm_tc_04_duplicate_number(self) -> None:
        """GM-TC-04 — duplicate non-zero values return E005."""
        # Given: grid with duplicated non-zero value
        # When/Then: error contract + baseline approve/compare
        _run_golden_master_case(GM_TC_04)

    def test_gm_tc_05_no_valid_magic_square(self) -> None:
        """GM-TC-05 — unsolvable puzzle returns DOMAIN_NO_SOLUTION."""
        # Given: G3 grid with no valid completion
        # When/Then: error contract + baseline approve/compare
        _run_golden_master_case(GM_TC_05)

    def test_gm_document_matches_baseline(self) -> None:
        """GM-2 — full baseline document matches approved golden master file."""
        # Given: all Golden Master scenarios
        # When/Then: full-document approve/compare
        assert_matches_golden_master(EXPECTED_PATH)
