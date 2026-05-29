"""AC-FR-01-01, PRD §8.1 INVALID_SIZE — 경계값 (크기 위반)."""

from __future__ import annotations

from typing import Any

from tests.boundary.conftest import INVALID_SIZE_CODE


class TestAcFr0101BoundaryValues:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 경계값 크기 위반."""

    def test_empty_list_grid_returns_invalid_size_code(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: 빈 리스트 grid (0×0)
        grid: list[list[int]] = []

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: INVALID_SIZE를 반환한다
        assert result.code == INVALID_SIZE_CODE

    def test_four_empty_rows_grid_returns_invalid_size_code(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: 행 4개, 각 행 열 0개 (4×0)
        grid: list[list[int]] = [[]] * 4

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: INVALID_SIZE를 반환한다
        assert result.code == INVALID_SIZE_CODE

    def test_three_by_four_grid_returns_invalid_size_code(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: 3×4 격자 (행 수 ≠ 4)
        grid: list[list[int]] = [[1] * 4 for _ in range(3)]

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: INVALID_SIZE를 반환한다
        assert result.code == INVALID_SIZE_CODE

    def test_four_by_three_grid_returns_invalid_size_code(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: 4×3 격자 (열 수 ≠ 4)
        grid: list[list[int]] = [[1] * 3 for _ in range(4)]

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: INVALID_SIZE를 반환한다
        assert result.code == INVALID_SIZE_CODE

    def test_five_by_five_grid_returns_invalid_size_code(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: 5×5 격자 (크기 초과)
        grid: list[list[int]] = [[1] * 5 for _ in range(5)]

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: INVALID_SIZE를 반환한다
        assert result.code == INVALID_SIZE_CODE
