# MagicSquare — 결함 목록 (Defect List)

| 항목 | 내용 |
|------|------|
| 문서 ID | DEF-LIST-001 |
| 기준 AC | AC-FR-01-01 (FR-01, PRD §10 / §13) |
| 테스트 스위트 | `tests/boundary/test_ac_fr_01_01_*.py` (25건) |
| 최종 검증 실행 | `python -m pytest tests/boundary/ -v --tb=short` |
| 검증 일자 | 2026-05-29 |
| 상태 | **OPEN 4건** / CLOSED 0건 / INFO 1건 |

---

## 실행 요약

| 결과 | 건수 |
|------|:----:|
| ERROR (setup) | 23 |
| PASSED | 2 |
| FAILED (assertion) | 0 |

> 23건 ERROR는 본문 assertion 미도달 — fixture import 단계에서 중단.

---

## 결함 등록표

| ID | Severity | AC ID | 재현 절차 | 기대값 | 실제값 | 근본 원인 | 수정 요약 |
|----|----------|--------|-----------|--------|--------|-----------|-----------|
| DEF-001 | **Critical** | AC-FR-01-01 | 1. 프로젝트 루트에서 `python -m pytest tests/boundary/test_ac_fr_01_01_normal_failure_return.py -v` 실행<br>2. `input_validator` fixture 로딩 | `InputValidator` import 성공 → `validate(None)` → `code="INVALID_SIZE"` | `ModuleNotFoundError: No module named 'src.boundary'`<br>(`tests/boundary/conftest.py:37`) | `src/boundary/` 패키지 및 `InputValidator` **미구현** | `src/boundary/__init__.py`, `error_response.py`, `input_validator.py` 추가. `grid is None` 및 4×4 크기 위반 시 `ErrorResponse(INVALID_SIZE, "Grid must be 4x4.")` 반환 |
| DEF-002 | **Critical** | AC-FR-01-01 | 1. `python -m pytest tests/boundary/test_ac_fr_01_01_isolation.py -v` 실행<br>2. `mock_resolve_use_case` fixture 로딩 | `SolveTwoBlanksUseCase` import 성공 → `PuzzleBoundary.submit(None)` 후 `execute` **0회** | `ModuleNotFoundError: No module named 'src.control'`<br>(`tests/boundary/conftest.py:45`) | `src/control/` 패키지 및 `SolveTwoBlanksUseCase` **미구현** | `src/control/solve_two_blanks_use_case.py`에 클래스·`execute` 시그니처만 추가 (FR-05 로직 금지). mock `spec` 충족용 |
| DEF-003 | **Critical** | AC-FR-01-01 | 1. DEF-001 해결 후에도 `grid is None` 분기 없이 `len(grid)` 등 접근 시<br>2. `InputValidator.validate(None)` 호출 | `ErrorResponse(code="INVALID_SIZE", message="Grid must be 4x4.")` (예외 미전파) | *(잠재)* `TypeError` / `AttributeError` (예: `'NoneType' has no len`) | None 입력 시 **선행 가드 분기 누락** (GREEN 구현 시 회귀 위험) | `validate()` 최상단에 `if grid is None: return ErrorResponse(...)` 추가. `len(grid)` 호출 전에만 처리 |
| DEF-004 | **Critical** | AC-FR-01-01 | 1. DEF-001·002 해결 후 `python -m pytest tests/boundary/test_ac_fr_01_01_isolation.py -v`<br>2. `PuzzleBoundary.submit(grid=None)` 호출 | `INVALID_SIZE` 반환, `mock_use_case.execute.call_count == 0` | *(잠재)* 검증 생략 시 Domain `execute` 호출 또는 미구현 `submit` | `PuzzleBoundary` 미구현 또는 검증 실패 시 **early return 미적용** | `src/boundary/puzzle_boundary.py` 추가. `validate` 결과 `code=="INVALID_SIZE"`이면 `execute` 호출 없이 `ErrorResponse` 반환 |
| DEF-005 | **Major** | AC-FR-01-01 | 1. DEF-001 해결 후 경계값 테스트 실행<br>2. `validate([])`, `validate([[]]*4)`, `validate(3×4)` 각각 호출 | 모든 크기 위반 입력 → `code="INVALID_SIZE"` | *(잠재)* `code` 누락·다른 오류 코드·통과 | `_check_size()` (행=4, 열=4) **미구현** | `_is_valid_size()` / `_check_size()` 최소 구현. AC-FR-01-02~05(빈칸·범위·중복) 분기 **추가 금지** |
| DEF-006 | **Info** | AC-FR-01-01 | 1. PRD §13·Architecture Contract vs `tests/boundary/conftest.py` 비교 | 단일 고정 message 문자열 | 테스트: `"Grid must be 4x4."`<br>PRD §13 표: `"Matrix must be 4x4."` | 요구사항 문서와 RED 테스트 **문구 불일치** | GREEN 시 **테스트 계약(`conftest.py:13`) 우선** 적용. PRD 정합은 별도 Decision/문서 개정으로 처리 |

---

## 영향 받는 테스트 (DEF-001 · DEF-002)

### DEF-001 — `src.boundary` 미구현 (18건 ERROR)

| RED Test ID | 테스트 함수 |
|-------------|-------------|
| RED-BND-001 | `test_none_grid_returns_invalid_size_code` 외 Normal Failure 5건 |
| RED-BND-002 | `test_empty_list_grid_returns_invalid_size_code` 외 Boundary 5건 |
| — | Message Identity 5건 |
| — | Scope Limitation 3건 (`input_validator` 사용) |

### DEF-002 — `src.control` 미구현 (5건 ERROR)

| RED Test ID | 테스트 함수 |
|-------------|-------------|
| RED-BND-006 | `test_none_grid_submit_resolve_execute_not_called` 외 Isolation 5건 |

### 통과 (결함 아님 — 범위 정적 검증)

| 테스트 | 비고 |
|--------|------|
| `test_valid_4x4_partial_not_in_ac_fr_01_01_red_parametrize` | AC-FR-01-01 스위트에 유효 4×4 미포함 확인 |
| `test_ac_fr_01_01_module_filenames_exclude_fr_02_to_05` | FR-02~05 전용 파일 미포함 확인 |

---

## 수정 우선순위 (GREEN)

```
1. DEF-001  →  src/boundary (ErrorResponse + InputValidator)
2. DEF-003  →  None 선행 분기 (DEF-001 구현 시 동시 적용)
3. DEF-005  →  크기 검증 분기
4. DEF-004  →  PuzzleBoundary early return
5. DEF-002  →  SolveTwoBlanksUseCase 스텁
6. DEF-006  →  문서 정합 (Info, 코드 변경 불필요 시)
```

---

## GREEN 확인 절차 (결함 수정 후)

```powershell
cd c:\DEV\MagicSquare_xx
.\.venv\Scripts\Activate.ps1   # 가상환경 사용 시

python -m pytest tests/boundary/ -v
# 기대: 25 passed

python -m pytest tests/ -v
# 기대: boundary 25 + entity 4 passed

python -m pytest tests/boundary/ --cov=src/boundary --cov-report=term-missing --cov-fail-under=85
```

수정 완료 시 본 문서 각 DEF 행 **Status**를 CLOSED로 갱신하고, README **「모든 결함 수정 후 회귀 테스트 통과 확인」** 체크박스를 완료 처리합니다.

---

## 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | AC-FR-01-01 RED 실행 결과 기반 초판 — DEF-001~006 등록 |
