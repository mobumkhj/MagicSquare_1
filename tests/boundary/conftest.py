"""Shared fixtures for Boundary RED tests (AC-FR-01-01)."""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock

import pytest

# AC-FR-01-01, PRD §8.1 INVALID_SIZE — 고정 계약 문자열
AC_FR_01_01_ID = "AC-FR-01-01"
INVALID_SIZE_CODE = "INVALID_SIZE"
INVALID_SIZE_MESSAGE = "Grid must be 4x4."

# AC-FR-01-02~05, FR-02~05 — 본 RED 스위트에 포함 금지 (범위 제한 검증용)
OUT_OF_SCOPE_ERROR_CODES = frozenset(
    {
        "INVALID_EMPTY_COUNT",
        "INVALID_VALUE_RANGE",
        "INVALID_DUPLICATE",
        "DOMAIN_NO_SOLUTION",
    }
)

# 4×4 정상 partial puzzle — AC-FR-01-01 범위 외
OUT_OF_SCOPE_VALID_4X4_PARTIAL: list[list[int]] = [
    [1, 2, 3, 4],
    [5, 6, 0, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 0],
]


@pytest.fixture
def input_validator() -> Any:
    """InputValidator 인스턴스 (RED: 미구현 시 ImportError)."""
    from src.boundary.input_validator import InputValidator

    return InputValidator()


@pytest.fixture
def mock_resolve_use_case() -> MagicMock:
    """Domain 해 결정 진입점 mock (SolveTwoBlanksUseCase.execute)."""
    from src.control.solve_two_blanks_use_case import SolveTwoBlanksUseCase

    mock = MagicMock(spec=SolveTwoBlanksUseCase)
    mock.execute.return_value = [2, 3, 7, 4, 1, 9]
    return mock


@pytest.fixture
def puzzle_boundary(mock_resolve_use_case: MagicMock) -> Any:
    """PuzzleBoundary with injected UseCase mock (RED: 미구현 시 ImportError)."""
    from src.boundary.puzzle_boundary import PuzzleBoundary

    return PuzzleBoundary(use_case=mock_resolve_use_case)
