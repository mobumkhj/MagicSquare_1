"""AC-FR-01-01, PRD §8.1 INVALID_SIZE — message 문자 단위 동일성."""

from __future__ import annotations

from typing import Any

import pytest

from tests.boundary.conftest import INVALID_SIZE_MESSAGE


class TestAcFr0101MessageIdentity:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — PRD §8.1 문구와 바이트 동일."""

    def test_none_grid_message_exact_match_prd_section_8_1(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=None, PRD §8.1 기대 문구
        expected = "Grid must be 4x4."
        grid = None

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: message가 문자 단위로 동일하다
        assert result.message == expected
        assert result.message is not None
        assert len(result.message) == len(expected)

    def test_empty_list_message_exact_match_prd_section_8_1(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=[]
        grid: list[list[int]] = []

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: PRD §8.1 message와 완전 일치
        assert result.message == INVALID_SIZE_MESSAGE

    def test_four_empty_rows_message_exact_match_prd_section_8_1(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=[[]]*4
        grid: list[list[int]] = [[]] * 4

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: message 바이트 동일
        assert bytes(result.message, "utf-8") == bytes(
            INVALID_SIZE_MESSAGE, "utf-8"
        )

    def test_three_by_four_message_exact_match_prd_section_8_1(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: 3×4 grid
        grid: list[list[int]] = [[1] * 4 for _ in range(3)]

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: message가 상수와 동일 (repr 비교로 공백·구두점 검증)
        assert repr(result.message) == repr(INVALID_SIZE_MESSAGE)

    def test_none_grid_message_not_matrix_variant_typo(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=None, 잘못된 변형 문구 목록
        wrong_messages = (
            "Matrix must be 4x4.",
            "Grid must be 4 x 4.",
            "grid must be 4x4.",
        )
        grid = None

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: PRD §8.1 'Grid must be 4x4.'만 허용, 변형 문구는 아니다
        assert result.message == INVALID_SIZE_MESSAGE
        assert result.message not in wrong_messages
