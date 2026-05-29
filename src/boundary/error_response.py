"""Boundary error response contract (pydantic)."""

from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class ErrorResponse(BaseModel):
    """Failure envelope returned when input validation fails."""

    model_config = ConfigDict(extra="forbid")

    type: str
    code: str
    message: str
