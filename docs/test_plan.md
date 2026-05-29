# MagicSquare 4×4 — 테스트 계획서 (Test Plan)

| 항목 | 내용 |
|------|------|
| 문서 ID | TP-AC-FR-01-01 |
| 대상 AC | **AC-FR-01-01** — 크기 위반 시 `INVALID_SIZE` 반환, Domain Solver **미호출** |
| PRD 요구사항 | **FR-01** Input Verification (Boundary), **§10** Functional Requirements, **§13** Error / Failure Policy |
| 관련 시나리오 | SC-BND-001, SC-BND-002, SC-BND-006 |
| RED Test ID | RED-BND-001, RED-BND-002, RED-BND-006 |
| 기술 스택 | Python 3.14+, pytest, pydantic, unittest.mock |
| ECB Layer | Boundary (`InputValidator`, `PuzzleBoundary`) |
| 작성 기준일 | 2026-05-29 |
| 상태 | 구현 전 — RED 우선 (Dual-Track Track A) |

---

## 1. 목적 및 범위

### 1.1 목적

FR-01의 **첫 번째 Acceptance Criteria(크기 위반 → `INVALID_SIZE`)** 를 pytest 단위·통합 테스트로 검증한다.  
본 계획서는 **AC-FR-01-01 샘플(`grid = None`)** 을 중심으로, Boundary 입력 크기 검증과 Domain 해 결정 진입점 격리를 동시에 보장하는 테스트 범위·우선순위·측정 전략을 정의한다.

### 1.2 In-Scope

| 구분 | 대상 | 설명 |
|------|------|------|
| 단위 (L2) | `InputValidator` | 크기 검증 로직, `ErrorResponse` 반환 |
| 통합 (L2) | `PuzzleBoundary.submit()` | 검증 실패 시 early return, UseCase 미호출 |
| 계약 | `ErrorResponse` (pydantic) | `code`, `message` 필드 및 고정 문자열 일치 |
| 격리 | `SolveTwoBlanksUseCase.execute` | mock/spy로 호출 횟수 0 검증 |

### 1.3 Out-of-Scope (본 AC 범위 외 — 테스트 포함 금지)

| 항목 | 사유 |
|------|------|
| **4×4 정상 입력(유효 partial puzzle)** | AC-FR-01-01은 **크기 위반**만 다룸. 정상 통과는 SC-BND-007 / RED-BND-007 별도 AC |
| 빈칸 개수·값 범위·중복 검증 | FR-01 AC 2~4 (`INVALID_EMPTY_COUNT`, `INVALID_VALUE_RANGE`, `INVALID_DUPLICATE`) — SC-BND-003~005 |
| Domain 불변식(행·열·대각 합 34) | Entity/Control Track B (SC-DOM-003~009) |
| 성공 응답 `int[6]` 포맷 | SC-INT-001~002 |

---

## 2. pytest 기반 단위 테스트 범위 및 우선순위

### 2.1 테스트 디렉터리 구조 (ECB 대응)

```
tests/
├── boundary/
│   ├── test_input_validator.py      ← P1: InputValidator 단위
│   └── test_puzzle_boundary.py       ← P2: PuzzleBoundary + UseCase mock
└── conftest.py                       ← 공통 fixture (ErrorResponse, mock UseCase)
```

### 2.2 우선순위 매트릭스

| 우선순위 | Track | RED ID | 테스트 대상 | 테스트 함수 (스켈레톤) | 검증 포인트 |
|:--------:|-------|--------|-------------|------------------------|-------------|
| **P0** | A | RED-BND-001 | `InputValidator.validate(None)` | `test_validate_none_input_returns_invalid_size` | `code == "INVALID_SIZE"`, message 고정 문자열 |
| **P1** | A | RED-BND-002 | `InputValidator.validate([])` | `test_validate_empty_list_returns_invalid_size` | 0×0 → `INVALID_SIZE` |
| **P1** | A | RED-BND-002 | `InputValidator.validate([[]]*4)` | `test_validate_four_empty_rows_returns_invalid_size` | 행 4, 열 0 → `INVALID_SIZE` |
| **P1** | A | RED-BND-002 | 3×4 / 4×3 / 5×5 | `test_validate_non_4x4_matrix_returns_invalid_size` | `@pytest.mark.parametrize` 3종 |
| **P2** | A | RED-BND-006 | `PuzzleBoundary.submit(invalid)` | `test_submit_invalid_size_does_not_call_use_case` | `mock_use_case.execute.call_count == 0` |
| **P3** | A | RED-BND-002 | jagged 행 (4행 중 1행 길이 3) | `test_validate_jagged_matrix_returns_invalid_size` | Architecture Contract U-02 |

> **TDD 규칙:** P0 RED 실패 확인 후에만 P1 구현·테스트 확장. GREEN 단계에서는 최소 코드만 추가한다.

### 2.3 테스트 패턴 (AAA + pytest 관례)

| 단계 | 내용 |
|------|------|
| **Arrange** | `grid` fixture 또는 `@pytest.mark.parametrize("grid", [...])` 로 입력 준비 |
| **Act** | `result = validator.validate(grid)` 또는 `boundary.submit(grid)` |
| **Assert** | `result.code == "INVALID_SIZE"`, `result.message == EXPECTED_MESSAGE`, `mock.execute.call_count == 0` |

- 테스트 함수명: `test_` 접두사 필수
- fixture scope: **function** (기본)
- assertion: pytest native assert (의미 있는 실패 메시지 포함)

### 2.4 pydantic 모델 검증

`ErrorResponse`는 pydantic BaseModel로 정의한다.

| 필드 | 기대 |
|------|------|
| `code` | `Literal["INVALID_SIZE", ...]` 또는 `ErrorCode` Enum |
| `message` | PRD §13 고정 문자열과 **바이트 동일** |
| `result` | 오류 응답에 **필드 없음** (model에 optional 미포함) |

고정 message (PRD §13 / Architecture Contract):

```
Matrix must be 4x4.
```

---

## 3. 경계값 케이스 목록

AC-FR-01-01 범위 내 **크기 위반** 경계값만 포함한다.  
4×4 정상 입력은 **본 AC 범위 외**이므로 아래 표에 **포함하지 않는다.**

| ID | 입력 (`grid`) | 행×열 (인식) | 기대 `code` | 기대 `message` | RED ID | 비고 |
|----|---------------|:------------:|-------------|----------------|--------|------|
| BV-01 | `None` | N/A (null) | `INVALID_SIZE` | `Matrix must be 4x4.` | RED-BND-001 | **P0 대표 샘플** — 명시적 None |
| BV-02 | `[]` | 0×0 | `INVALID_SIZE` | 동일 | RED-BND-002 | 빈 리스트 (`02.design.md` 경계 케이스) |
| BV-03 | `[[]] * 4` | 4×0 | `INVALID_SIZE` | 동일 | RED-BND-002 | 행 존재, 열 없음 |
| BV-04 | `[[1]*4]*3` | 3×4 | `INVALID_SIZE` | 동일 | RED-BND-002 | 행 수 ≠ 4 |
| BV-05 | `[[1]*3]*4` | 4×3 | `INVALID_SIZE` | 동일 | RED-BND-002 | 열 수 ≠ 4 |
| BV-06 | `[[1]*5]*5` | 5×5 | `INVALID_SIZE` | 동일 | RED-BND-002 | 초과 크기 |

### 3.1 parametrize 권장 형태 (개념)

```text
@pytest.mark.parametrize("grid", [
    None,
    [],
    [[]] * 4,
    [[1] * 4] * 3,
    [[1] * 3] * 4,
    [[1] * 5] * 5,
])
```

> BV-04~06은 하나의 parametrize 테스트(`test_validate_non_4x4_matrix_returns_invalid_size`)로 묶고, BV-01~03은 의도·RED 추적성을 위해 **별도 테스트 함수**로 유지한다.

### 3.2 명시적 제외 케이스

| 입력 | 제외 사유 |
|------|-----------|
| 유효 4×4 partial puzzle (빈칸 2개, 범위·중복 통과) | AC-FR-01-01 **범위 외** — SC-BND-007 / RED-BND-007 |
| 4×4이나 값·빈칸·중복 위반 | 크기는 통과, 다른 AC 담당 (SC-BND-003~005) |

---

## 4. 예외 / 특이 케이스 목록

크기 검증 단계에서 발생 가능한 **비정형·방어적 입력**이다. 모두 `INVALID_SIZE` + Domain 미호출이 기대된다.

| ID | 입력 / 조건 | 기대 동작 | 테스트 함수 (후보) | 비고 |
|----|-------------|-----------|-------------------|------|
| EX-01 | `grid = None` | `INVALID_SIZE`, 예외 **미전파** (ErrorResponse 반환) | `test_validate_none_input_returns_invalid_size` | BV-01과 동일, P0 |
| EX-02 | `grid = [1, 2, 3, ...]` (flat 16원소 단일 리스트) | `INVALID_SIZE` | `test_validate_flat_list_not_2d_returns_invalid_size` | `02.design.md` — 2D 아님 |
| EX-03 | 4행이나 행 길이 불균일 (jagged) | `INVALID_SIZE` | `test_validate_jagged_matrix_returns_invalid_size` | Contract U-02 |
| EX-04 | `grid = [[None]*4]*4` | 구현 정책에 따라 `INVALID_SIZE` 또는 `INVALID_VALUE_RANGE` | **Decision Needed** | None 셀 vs 크기 — **본 AC에서는 크기 검증 선행** 가정 |
| EX-05 | `grid = "not a grid"` (문자열) | `INVALID_SIZE` 또는 타입 거부 | `test_validate_non_sequence_returns_invalid_size` | Boundary 방어 — pydantic/타입 가드 |
| EX-06 | `InputValidator` 내부 예외 (예: `len()` on None 미처리) | **금지** — bare `except:` 사용 금지 (NFR-09) | — | RED에서 None 분기 선구현으로 방지 |
| EX-07 | 검증 실패 후 `PuzzleBoundary`가 UseCase 호출 | **금지** — `call_count == 0` | `test_submit_invalid_size_does_not_call_use_case` | SC-BND-006 |

### 4.1 오류 응답 계약 (특이 케이스 공통)

| 항목 | 규칙 |
|------|------|
| HTTP 의미 (참고) | 400 |
| `result` 필드 | **absent** — 오류 응답에 성공 배열 없음 |
| Domain 호출 | **0회** — FR-01 AC 5항, §13 |
| message | 코드별 고정 문자열 변경 **금지** (회귀 테스트 대상) |

---

## 5. Domain 해 결정 진입점 호출 횟수 검증 전략

### 5.1 검증 대상 (진입점)

| 컴포넌트 | 메서드 | Layer | 역할 |
|----------|--------|-------|------|
| `SolveTwoBlanksUseCase` | `execute(matrix) -> list[int]` | Control | 해 결정 유스케이스 **유일 진입점** |
| `PuzzleBoundary` | `submit(matrix)` | Boundary | 검증 → (성공 시) UseCase 위임 |

Domain Entity (`BlankFinder`, `MissingNumberFinder`, `MagicSquareValidator`, `Solver`)는 UseCase 내부에서 호출되므로, **Boundary 테스트에서는 UseCase mock 1곳만 spy** 하면 Entity 전체 미진입을 간접 보장한다.

### 5.2 Mock / Spy 패턴 (`unittest.mock`)

#### 패턴 A — 생성자 주입 + `MagicMock` (권장)

```text
Arrange:
  mock_use_case = MagicMock(spec=SolveTwoBlanksUseCase)
  mock_use_case.execute.return_value = [2, 3, 7, 4, 1, 9]  # 성공 케이스용 (본 AC 미사용)
  boundary = PuzzleBoundary(use_case=mock_use_case)

Act:
  result = boundary.submit(grid=None)   # 또는 BV-02~06

Assert:
  mock_use_case.execute.assert_not_called()
  # 또는 assert mock_use_case.execute.call_count == 0
```

#### 패턴 B — `patch` (모듈 레벨)

```text
@patch("src.boundary.puzzle_boundary.SolveTwoBlanksUseCase")
def test_submit_none_does_not_instantiate_or_call_use_case(mock_cls):
    ...
```

> **권장:** 패턴 A (DI). ECB 경계 명확, 테스트 독립성·리팩터 내성 우수.

#### 패턴 C — `InputValidator` 단위 (Domain mock 불필요)

`InputValidator.validate()` 는 Control/Entity에 **의존하지 않음**.  
BV-01~06은 **mock 없이** 순수 단위 테스트로 RED→GREEN 가능.

| 테스트 레벨 | Mock 필요 | 검증 |
|-------------|:---------:|------|
| `InputValidator` 단위 | ❌ | `ErrorResponse` 필드만 |
| `PuzzleBoundary` 통합 | ✅ | `execute.call_count == 0` |

### 5.3 SC-BND-006 확장 (4종 입력 오류 일괄)

AC-FR-01-01 완료 후, 동일 mock 전략으로 아래도 **호출 0회** 확인 (별도 AC, 참고):

- `INVALID_EMPTY_COUNT`
- `INVALID_VALUE_RANGE`
- `INVALID_DUPLICATE`

본 계획서 Phase 1에서는 **INVALID_SIZE 계열만** mock spy 적용.

### 5.4 Mock 기본 반환값 (Architecture Contract)

유효 입력 테스트(SC-BND-007, 범위 외)용 기본 stub:

```text
mock_use_case.execute.return_value = [2, 3, 7, 4, 1, 9]
```

---

## 6. 커버리지 목표

| NFR ID | Layer | 대상 패키지 | 목표 | 측정 범위 |
|--------|-------|-------------|:----:|-----------|
| NFR-01 | Entity + Control | `src/entity`, `src/control` | **≥ 95%** | Domain 순수 로직·Solver |
| NFR-02 | Boundary | `src/boundary` | **≥ 85%** | `InputValidator`, `PuzzleBoundary`, `ErrorResponse` |

### 6.1 AC-FR-01-01 Phase 1 최소 커버리지 (Incremental)

| 모듈 | Phase 1 목표 | 근거 |
|------|:------------:|------|
| `InputValidator` (크기 분기) | **100%** (해당 함수/분기) | P0~P1 RED 6케이스 |
| `PuzzleBoundary.submit` (early return) | **≥ 85%** | P2 mock spy 1케이스 + 이후 확장 |
| Entity/Control | 0% (Track B 미착수) | Dual-Track 병렬 — Domain mock으로 Boundary만 RED |

> 전체 프로젝트 **80%** 최소 기준(`.cursor/rules/magicsquare-tdd-testing.mdc`)은 유지하되, NFR-01/02가 Layer별 상한을 정의한다.

### 6.2 커버리지 미달 시 조치

1. `--cov-report=term-missing` 으로 미커버 라인 확인
2. AC-FR-01-01 범위 내 **의미 있는 RED 테스트** 추가 (assertion 약화 금지)
3. dead code / unreachable branch는 REFACTOR 단계에서 제거 검토

---

## 7. pytest-cov 측정 전략

### 7.1 설치

```bash
pip install pytest-cov
```

### 7.2 기본 실행 (전체)

```bash
pytest --cov=src --cov-report=term-missing
```

### 7.3 AC-FR-01-01 Phase 1 — Boundary 집중 측정

```bash
pytest tests/boundary/test_input_validator.py tests/boundary/test_puzzle_boundary.py \
  --cov=src/boundary \
  --cov-report=term-missing \
  --cov-fail-under=85
```

### 7.4 Layer별 분리 측정 (CI 권장)

```bash
# Boundary (NFR-02)
pytest tests/boundary/ --cov=src/boundary --cov-report=term-missing --cov-fail-under=85

# Domain (NFR-01) — Track B 착수 후
pytest tests/entity/ tests/control/ --cov=src/entity --cov=src/control \
  --cov-report=term-missing --cov-fail-under=95
```

### 7.5 HTML 리포트 (로컬 분석)

```bash
pytest --cov=src --cov-report=html
# 산출물: htmlcov/index.html
```

### 7.6 측정 시 주의사항

| 항목 | 규칙 |
|------|------|
| 측정 대상 | `src/` 패키지만 (`--cov=src`) |
| 테스트 코드 | `--cov` 에 `tests/` **포함 금지** |
| RED 단계 | 커버리지 fail-under로 GREEN **강제 금지** — RED 확인 후 GREEN에서 fail-under 활성화 |
| REFACTOR | 기능·계약 불변, 커버리지 **하락 금지** |

---

## 8. 추적성 (Traceability)

| AC ID | User Story | Scenario | RED ID | Test Module | Boundary Case |
|-------|------------|----------|--------|-------------|---------------|
| AC-FR-01-01 | US-001 | SC-BND-001 | RED-BND-001 | `test_input_validator.py` | BV-01 |
| AC-FR-01-01 | US-001 | SC-BND-002 | RED-BND-002 | `test_input_validator.py` | BV-02~06, EX-02~03 |
| AC-FR-01-01 (격리) | US-001 | SC-BND-006 | RED-BND-006 | `test_puzzle_boundary.py` | BV-01~06 (parametrize) |

---

## 9. 실행 순서 (TDD Phase 1)

```
1. P0  RED-BND-001  test_validate_none_input_returns_invalid_size     → RED 확인
2. P0  GREEN         None 분기 → ErrorResponse(INVALID_SIZE)          → GREEN
3. P1  RED-BND-002  BV-02~06 + EX-02~03                               → RED 확인
4. P1  GREEN         _check_size() 최소 구현                            → GREEN
5. P2  RED-BND-006  test_submit_invalid_size_does_not_call_use_case    → RED 확인
6. P2  GREEN         PuzzleBoundary early return + DI                  → GREEN
7.      pytest-cov   boundary ≥ 85% 확인
8.      REFACTOR     ErrorCode Enum + ERROR_MESSAGES dict (계약 불변)
```

---

## 10. 완료 기준 (Exit Criteria)

- [ ] BV-01~06 전 케이스에서 `code == "INVALID_SIZE"`, message 고정 문자열 일치
- [ ] 4×4 정상 입력 테스트가 **본 AC 테스트 스위트에 포함되지 않음**
- [ ] `PuzzleBoundary.submit(invalid)` 에서 `SolveTwoBlanksUseCase.execute` **호출 0회**
- [ ] RED → GREEN → REFACTOR 사이클 준수 (RED 미확인 구현 금지)
- [ ] `src/boundary` 커버리지 **≥ 85%** (`pytest --cov=src/boundary --cov-fail-under=85`)
- [ ] 테스트 약화·skip·삭제 없이 전체 pytest 통과

---

## 문서 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | AC-FR-01-01 (`grid=None → INVALID_SIZE`) 기반 테스트 계획서 초판 |
