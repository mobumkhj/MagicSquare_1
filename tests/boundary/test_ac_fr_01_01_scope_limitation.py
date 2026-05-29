"""AC-FR-01-01 — 범위 제한 (AC-FR-01-02~05, FR-02~05 케이스 포함 금지)."""

from __future__ import annotations

import ast
from pathlib import Path
from typing import Any

import pytest

from tests.boundary.conftest import (
    AC_FR_01_01_ID,
    INVALID_SIZE_CODE,
    OUT_OF_SCOPE_ERROR_CODES,
    OUT_OF_SCOPE_VALID_4X4_PARTIAL,
)


class TestAcFr0101ScopeLimitation:
    """AC-FR-01-01, PRD §8.1 INVALID_SIZE — 본 RED 스위트 범위 제한."""

    def test_none_grid_does_not_return_invalid_empty_count(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=None (크기 위반만 검증, AC-FR-01-02 아님)
        grid = None

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: INVALID_EMPTY_COUNT가 아닌 INVALID_SIZE이다
        assert result.code == INVALID_SIZE_CODE
        assert result.code != "INVALID_EMPTY_COUNT"

    def test_none_grid_does_not_return_invalid_value_range(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=None
        grid = None

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: AC-FR-01-03 범위 오류 코드가 아니다
        assert result.code not in OUT_OF_SCOPE_ERROR_CODES
        assert result.code == INVALID_SIZE_CODE

    def test_none_grid_does_not_return_invalid_duplicate(
        self, input_validator: Any
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: grid=None
        grid = None

        # When: 입력 검증을 수행한다
        result = input_validator.validate(grid)

        # Then: AC-FR-01-04 중복 오류 코드가 아니다
        assert result.code != "INVALID_DUPLICATE"

    def test_valid_4x4_partial_not_in_ac_fr_01_01_red_parametrize(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: AC-FR-01-01 경계값 모듈 소스
        boundary_dir = Path(__file__).resolve().parent
        sources = list(boundary_dir.glob("test_ac_fr_01_01_*.py"))

        # When: parametrize/grid fixture에 유효 4×4 partial이 없는지 확인한다
        valid_repr = repr(OUT_OF_SCOPE_VALID_4X4_PARTIAL)
        found_in_parametrize = False
        for source_path in sources:
            tree = ast.parse(source_path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if isinstance(node, ast.Call) and getattr(
                    node.func, "attr", None
                ) == "parametrize":
                    for arg in node.args:
                        if valid_repr in ast.unparse(arg):
                            found_in_parametrize = True

        # Then: 유효 4×4 partial은 본 RED 스위트 parametrize에 없다
        assert found_in_parametrize is False

    def test_ac_fr_01_01_module_filenames_exclude_fr_02_to_05(
        self,
    ) -> None:
        """AC-FR-01-01, PRD §8.1 INVALID_SIZE."""
        # AC-FR-01-01
        # Given: boundary 테스트 디렉터리
        boundary_dir = Path(__file__).resolve().parent
        ac_fr_01_01_files = list(
            boundary_dir.glob("test_ac_fr_01_01_*.py")
        )

        # When: 파일명이 AC-FR-01-01 전용인지 확인한다
        forbidden_suffixes = (
            "blank",
            "duplicate",
            "value_range",
            "domain_solver",
            "fr_02",
            "fr_03",
            "fr_04",
            "fr_05",
        )

        # Then: FR-02~05 전용 RED 파일이 이 커밋에 없다
        for path in ac_fr_01_01_files:
            name_lower = path.stem.lower()
            assert AC_FR_01_01_ID.replace("-", "_").lower() in name_lower
            assert not any(suffix in name_lower for suffix in forbidden_suffixes)
