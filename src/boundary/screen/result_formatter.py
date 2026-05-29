"""Format boundary outcomes for GUI display."""

from __future__ import annotations

from src.boundary.error_response import ErrorResponse

Solution = list[int]


def format_success(solution: Solution) -> str:
    """Format a six-element solution for display.

    Args:
        solution: [r1, c1, n1, r2, c2, n2] with 1-index coordinates.

    Returns:
        Human-readable success message.
    """
    r1, c1, n1, r2, c2, n2 = solution
    return (
        f"Solution: ({r1}, {c1}) = {n1}, ({r2}, {c2}) = {n2} "
        f"[{r1}, {c1}, {n1}, {r2}, {c2}, {n2}]"
    )


def format_error(error: ErrorResponse) -> str:
    """Format an error envelope for display.

    Args:
        error: Boundary validation or domain error response.

    Returns:
        Human-readable error message with code.
    """
    return f"Error [{error.code}]: {error.message}"
