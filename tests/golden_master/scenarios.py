"""Golden Master input scenarios for solver regression."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Final

from src.boundary.schemas import (
    DOMAIN_NO_SOLUTION_CODE,
    E002_CODE,
    E005_CODE,
)
from tests.conftest import G3

Grid = list[list[int]]


class ScenarioKind(str, Enum):
    """Golden Master scenario classification."""

    SUCCESS_SMALL_FIRST = "success_small_first"
    SUCCESS_REVERSE = "success_reverse"
    ERROR_BLANK_COUNT = "error_blank_count"
    ERROR_DUPLICATE = "error_duplicate"
    ERROR_NO_SOLUTION = "error_no_solution"


@dataclass(frozen=True)
class GoldenScenario:
    """Named puzzle scenario for Golden Master capture."""

    test_id: str
    name: str
    grid: Grid
    kind: ScenarioKind
    expected_error_code: str | None = None


NORMAL_SUCCESS_GRID: Final[Grid] = [
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 0, 12],
    [4, 15, 0, 1],
]

REVERSE_SUCCESS_GRID: Final[Grid] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 0, 12],
    [4, 14, 15, 0],
]

INVALID_BLANK_COUNT_GRID: Final[Grid] = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

DUPLICATE_NUMBER_GRID: Final[Grid] = [
    [1, 2, 3, 4],
    [5, 5, 0, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0],
]

GM_TC_01: Final[GoldenScenario] = GoldenScenario(
    test_id="GM-TC-01",
    name="normal_success",
    grid=NORMAL_SUCCESS_GRID,
    kind=ScenarioKind.SUCCESS_SMALL_FIRST,
)

GM_TC_02: Final[GoldenScenario] = GoldenScenario(
    test_id="GM-TC-02",
    name="reverse_success",
    grid=REVERSE_SUCCESS_GRID,
    kind=ScenarioKind.SUCCESS_REVERSE,
)

GM_TC_03: Final[GoldenScenario] = GoldenScenario(
    test_id="GM-TC-03",
    name="invalid_blank_count",
    grid=INVALID_BLANK_COUNT_GRID,
    kind=ScenarioKind.ERROR_BLANK_COUNT,
    expected_error_code=E002_CODE,
)

GM_TC_04: Final[GoldenScenario] = GoldenScenario(
    test_id="GM-TC-04",
    name="duplicate_number",
    grid=DUPLICATE_NUMBER_GRID,
    kind=ScenarioKind.ERROR_DUPLICATE,
    expected_error_code=E005_CODE,
)

GM_TC_05: Final[GoldenScenario] = GoldenScenario(
    test_id="GM-TC-05",
    name="no_valid_magic_square",
    grid=G3,
    kind=ScenarioKind.ERROR_NO_SOLUTION,
    expected_error_code=DOMAIN_NO_SOLUTION_CODE,
)

GOLDEN_SCENARIOS: Final[tuple[GoldenScenario, ...]] = (
    GM_TC_01,
    GM_TC_02,
    GM_TC_03,
    GM_TC_04,
    GM_TC_05,
)

SCENARIO_BY_TEST_ID: Final[dict[str, GoldenScenario]] = {
    scenario.test_id: scenario for scenario in GOLDEN_SCENARIOS
}
