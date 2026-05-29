"""AC-FR-01-01, PRD §8.1 INVALID_SIZE — 정상 실패 반환 (Happy Path of Failure)."""

from __future__ import annotations

from typing import Any

from tests.boundary.conftest import INVALID_SIZE_CODE, INVALID_SIZE_MESSAGE


class TestAcFr0101NormalFailureReturn:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — grid=None 정상 실패 반환."""

    def test_none_grid_returns_invalid_size_code(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: 호출자가 grid를 전달하지 않음 (None)
        grid = None

        # When: Boundary 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: code는 INVALID_SIZE이다
        assert result.code == INVALID_SIZE_CODE

    def test_none_grid_returns_invalid_size_message(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=None
        grid = None

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: message는 PRD §8.1 고정 문구이다
        assert result.message == INVALID_SIZE_MESSAGE

    def test_none_grid_returns_error_response_not_exception(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=None
        grid = None

        # When: 입력 검증을 수행한다
        from src.boundary.error_response import ErrorResponse

        result = input_validator.validate(grid)

        # Then: 예외가 아닌 ErrorResponse 구조체를 반환한다
        assert isinstance(result, ErrorResponse)

    def test_none_grid_failure_has_no_result_field(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=None
        grid = None

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: 성공 배열 result 필드가 없다
        assert not hasattr(result, "result")

    def test_none_grid_validate_does_not_mark_success(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=None
        grid = None

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: 성공 플래그가 True가 아니다 (오류 응답)
        assert getattr(result, "is_valid", False) is not True
