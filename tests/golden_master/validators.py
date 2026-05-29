"""Golden Master contract validators for solver outcomes."""

from __future__ import annotations

from src.boundary.error_response import ErrorResponse
from src.boundary.schemas import RESPONSE_TYPE_ERROR
from src.entity.constants import GRID_SIZE, MAX_CELL_VALUE, MIN_CELL_VALUE
from src.entity.services.blank_finder import find_blank_coords
from tests.golden_master.scenarios import Grid, ScenarioKind

Solution = list[int]
SOLUTION_LENGTH = 6


def validate_int6_output_format(solution: Solution) -> None:
    """Validate successful output is a six-element integer list.

    Args:
        solution: Solver result array.

    Raises:
        AssertionError: When shape or element types violate the int[6] contract.
    """
    assert len(solution) == SOLUTION_LENGTH
    assert all(isinstance(value, int) for value in solution)


def validate_one_index_coordinates(solution: Solution) -> None:
    """Validate coordinate fields use 1-index values in grid bounds.

    Args:
        solution: Solver result array.

    Raises:
        AssertionError: When coordinates fall outside 1..GRID_SIZE.
    """
    r1, c1, _, r2, c2, _ = solution
    for row, col in ((r1, c1), (r2, c2)):
        assert MIN_CELL_VALUE <= row <= GRID_SIZE
        assert MIN_CELL_VALUE <= col <= GRID_SIZE


def validate_row_major_blank_order(grid: Grid, solution: Solution) -> None:
    """Validate solution coordinates follow row-major blank discovery order.

    Args:
        grid: Input puzzle grid.
        solution: Solver result array.

    Raises:
        AssertionError: When coordinate ordering differs from row-major blanks.
    """
    blanks = find_blank_coords(grid)
    r1, c1, _, r2, c2, _ = solution
    assert (r1, c1) == blanks[0]
    assert (r2, c2) == blanks[1]


def validate_fill_value_contract(solution: Solution) -> None:
    """Validate fill numbers are distinct values within puzzle range.

    Args:
        solution: Solver result array.

    Raises:
        AssertionError: When fill values violate domain range or distinctness.
    """
    _, _, n1, _, _, n2 = solution
    assert MIN_CELL_VALUE <= n1 <= MAX_CELL_VALUE
    assert MIN_CELL_VALUE <= n2 <= MAX_CELL_VALUE
    assert n1 != n2


def validate_small_first_rule(solution: Solution) -> None:
    """Validate Attempt 1 success assigns smaller fill to the first blank.

    Args:
        solution: Solver result array.

    Raises:
        AssertionError: When n1 is not the smaller fill value.
    """
    _, _, n1, _, _, n2 = solution
    assert n1 < n2


def validate_reverse_fallback_rule(solution: Solution) -> None:
    """Validate Attempt 2 success assigns larger fill to the first blank.

    Args:
        solution: Solver result array.

    Raises:
        AssertionError: When n1 is not the larger fill value.
    """
    _, _, n1, _, _, n2 = solution
    assert n1 > n2


def validate_success_contract(
    grid: Grid,
    solution: Solution,
    *,
    kind: ScenarioKind,
) -> None:
    """Validate all success-path Golden Master contracts for one scenario.

    Args:
        grid: Input puzzle grid.
        solution: Solver result array.
        kind: Expected success ordering rule.

    Raises:
        AssertionError: When any success contract is violated.
    """
    validate_int6_output_format(solution)
    validate_one_index_coordinates(solution)
    validate_row_major_blank_order(grid, solution)
    validate_fill_value_contract(solution)

    if kind == ScenarioKind.SUCCESS_SMALL_FIRST:
        validate_small_first_rule(solution)
        return

    if kind == ScenarioKind.SUCCESS_REVERSE:
        validate_reverse_fallback_rule(solution)
        return

    msg = f"Unsupported success scenario kind: {kind}"
    raise AssertionError(msg)


def validate_error_contract(error: ErrorResponse, expected_code: str) -> None:
    """Validate boundary error envelope matches the Golden Master contract.

    Args:
        error: Boundary error response.
        expected_code: Expected error code string.

    Raises:
        AssertionError: When type or code differs from the contract.
    """
    assert error.type == RESPONSE_TYPE_ERROR
    assert error.code == expected_code
