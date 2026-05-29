"""AC-FR-01-01, PRD §8.1 INVALID_SIZE — Domain 진입점 격리 (resolve/execute 0회)."""

from __future__ import annotations

from typing import Any
from unittest.mock import MagicMock

import pytest

from tests.boundary.conftest import INVALID_SIZE_CODE


class TestAcFr0101IsolationVerification:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — grid=None 시 resolve() 0회 호출."""

    def test_none_grid_submit_resolve_execute_not_called(
        self, puzzle_boundary: Any, mock_resolve_use_case: MagicMock
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=None, Domain UseCase mock 주입
        grid = None

        # When: PuzzleBoundary.submit을 호출한다
        puzzle_boundary.submit(grid)

        # Then: resolve(execute) 진입점이 0회 호출된다
        mock_resolve_use_case.execute.assert_not_called()

    def test_empty_list_grid_submit_resolve_execute_not_called(
        self, puzzle_boundary: Any, mock_resolve_use_case: MagicMock
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=[]
        grid: list[list[int]] = []

        # When: submit을 호출한다
        puzzle_boundary.submit(grid)

        # Then: resolve(execute) 0회
        assert mock_resolve_use_case.execute.call_count == 0

    def test_four_empty_rows_grid_submit_resolve_execute_not_called(
        self, puzzle_boundary: Any, mock_resolve_use_case: MagicMock
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=[[]]*4
        grid: list[list[int]] = [[]] * 4

        # When: submit을 호출한다
        puzzle_boundary.submit(grid)

        # Then: resolve(execute) 0회
        mock_resolve_use_case.execute.assert_not_called()

    def test_three_by_four_grid_submit_resolve_execute_not_called(
        self, puzzle_boundary: Any, mock_resolve_use_case: MagicMock
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: 3×4 grid
        grid: list[list[int]] = [[1] * 4 for _ in range(3)]

        # When: submit을 호출한다
        puzzle_boundary.submit(grid)

        # Then: resolve(execute) 0회
        assert mock_resolve_use_case.execute.call_count == 0

    def test_none_grid_submit_returns_invalid_size_before_resolve(
        self, puzzle_boundary: Any, mock_resolve_use_case: MagicMock
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=None
        grid = None

        # When: submit이 INVALID_SIZE를 반환한다
        result = puzzle_boundary.submit(grid)

        # Then: 오류 코드가 INVALID_SIZE이고 resolve는 호출되지 않는다
        assert result.code == INVALID_SIZE_CODE
        mock_resolve_use_case.execute.assert_not_called()
