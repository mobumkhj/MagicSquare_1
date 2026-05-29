"""Screen result formatter — boundary outcomes to display text."""

from __future__ import annotations

from src.boundary.error_response import ErrorResponse
from src.boundary.schemas import INVALID_SIZE_CODE, INVALID_SIZE_MESSAGE, RESPONSE_TYPE_ERROR
from src.boundary.screen.result_formatter import format_error, format_success


class TestResultFormatter:
    """Format success and error outcomes for GUI display."""

    def test_format_success_shows_coordinates_and_values(self) -> None:
        """Six-element solution renders readable success text."""
        # Given: valid solution array
        solution = [2, 2, 10, 3, 3, 7]

        # When: format_success(solution)
        text = format_success(solution)

        # Then: coordinates and fill numbers appear
        assert "2, 2" in text
        assert "10" in text
        assert "3, 3" in text
        assert "7" in text

    def test_format_error_shows_code_and_message(self) -> None:
        """ErrorResponse renders code and fixed message."""
        # Given: validation error envelope
        error = ErrorResponse(
            type=RESPONSE_TYPE_ERROR,
            code=INVALID_SIZE_CODE,
            message=INVALID_SIZE_MESSAGE,
        )

        # When: format_error(error)
        text = format_error(error)

        # Then: code and message are visible
        assert INVALID_SIZE_CODE in text
        assert INVALID_SIZE_MESSAGE in text
