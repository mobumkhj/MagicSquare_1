"""Serialize solver outcomes for Golden Master comparison."""

from __future__ import annotations

from src.boundary.error_response import ErrorResponse
from src.boundary.puzzle_boundary import PuzzleBoundary
from src.control.solve_two_blanks_use_case import SolveTwoBlanksUseCase
from tests.golden_master.scenarios import GOLDEN_SCENARIOS, GoldenScenario, Grid

Solution = list[int]


def format_grid(grid: Grid) -> str:
    """Format a 4x4 grid as space-separated row lines.

    Args:
        grid: Puzzle input matrix.

    Returns:
        Multi-line text representation of the grid.
    """
    return "\n".join(" ".join(str(cell) for cell in row) for row in grid)


def format_solution(solution: Solution) -> str:
    """Format a six-element solution without spaces.

    Args:
        solution: Solver result array.

    Returns:
        Bracketed comma-separated solution string.
    """
    return "[" + ",".join(str(value) for value in solution) + "]"


def capture_scenario_outcome(scenario: GoldenScenario) -> ErrorResponse | Solution:
    """Run one scenario through PuzzleBoundary and return the raw outcome.

    Args:
        scenario: Named grid scenario.

    Returns:
        ErrorResponse on validation/domain failure, otherwise int[6] solution.
    """
    boundary = PuzzleBoundary(use_case=SolveTwoBlanksUseCase())
    outcome = boundary.submit(scenario.grid)

    if isinstance(outcome, ErrorResponse):
        return outcome

    return list(outcome)


def serialize_scenario_outcome(scenario: GoldenScenario) -> str:
    """Serialize one scenario outcome as Output or Error block text.

    Args:
        scenario: Named grid scenario.

    Returns:
        Output or Error block without the Input header.
    """
    outcome = capture_scenario_outcome(scenario)

    if isinstance(outcome, ErrorResponse):
        return f"Error:\n{outcome.code}"

    return f"Output:\n{format_solution(outcome)}"


def format_scenario_block(scenario: GoldenScenario) -> str:
    """Format one Golden Master scenario block.

    Args:
        scenario: Named grid scenario.

    Returns:
        Full scenario section including input and captured outcome.
    """
    outcome_text = serialize_scenario_outcome(scenario)
    return (
        f"[{scenario.test_id}]\n"
        f"Input:\n{format_grid(scenario.grid)}\n"
        f"{outcome_text}"
    )


def render_golden_master_document() -> str:
    """Render all Golden Master scenarios as one expected document.

    Returns:
        Full baseline text with blank-line separators between scenarios.
    """
    blocks = [format_scenario_block(scenario) for scenario in GOLDEN_SCENARIOS]
    return "\n\n".join(blocks) + "\n"
