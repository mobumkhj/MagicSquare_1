"""Domain errors for Magic Square resolution."""

from __future__ import annotations


class UnsolvableDomainError(Exception):
    """Raised when no valid magic square completion exists."""
