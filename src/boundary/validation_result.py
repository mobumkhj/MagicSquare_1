"""Boundary input validation outcome (pre-envelope)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ValidationResult:
    """Result of grid input validation before ErrorResponse mapping."""

    is_valid: bool
    code: str | None = None
    message: str | None = None

    @classmethod
    def ok(cls) -> ValidationResult:
        """Return a successful validation result."""
        return cls(is_valid=True)

    @classmethod
    def fail(cls, code: str, message: str) -> ValidationResult:
        """Return a failed validation result with contract code and message."""
        return cls(is_valid=False, code=code, message=message)
