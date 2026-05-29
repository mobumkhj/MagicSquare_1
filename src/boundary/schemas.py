"""Boundary response schemas."""

from __future__ import annotations

from dataclasses import dataclass

RESPONSE_TYPE_ERROR = "ERROR"
INVALID_SIZE_CODE = "INVALID_SIZE"
INVALID_SIZE_MESSAGE = "Grid must be 4x4."


@dataclass(frozen=True)
class FailureResponse:
    """Failure envelope returned when input validation fails."""

    type: str
    code: str
    message: str
