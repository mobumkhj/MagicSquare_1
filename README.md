# MagicSquare 4x4 TDD Practice

> **4×4 Magic Square — Dual-Track UI + Logic TDD 훈련 프로젝트**  
> PRD 기반 계약 고정 · ECB 분리 · Concept-to-Code Traceability

**Repository:** [github.com/mobumkhj/MagicSquare_1](https://github.com/mobumkhj/MagicSquare_1)

---

## 1. Project Start Declaration

**이 프로젝트는 4×4 Magic Square를 "풀어내는 알고리즘"이 아니라, 불변식 기반 사고와 입력/출력 계약을 구현 전에 고정하고, Dual-Track TDD로 검증하는 TDD 훈련을 시작합니다.**

현재 단계는 **Dual-Track RED 확정 · GREEN 단계 진행 중**입니다.  
`AC-FR-01-01` Boundary RED(25건)는 기착수되었고, FR-01~FR-05 확장 RED(`U-*`, `D-*`)와 **최소 Boundary GREEN**(`InputValidator` `None`/`[]` 분기)이 진행 중입니다.

### RED의 의미

**RED는 "실패하는 테스트를 작성하고, 테스트 실패 상태를 확인하는 단계"입니다.**  
구현 없이 테스트를 실행했을 때 **의도한 이유로** 실패하는지 반드시 확인한 뒤에만 GREEN(최소 구현)으로 진행합니다.

### 이 README의 역할

이 문서는 프로젝트 소개가 아니라 **구현 전에 개발 방향과 추적 구조를 고정하는 개발 가이드**입니다.  
모든 작업은 아래 추적 체인을 따릅니다.

```
Scenario → Acceptance Criteria → RED Test ID → Test Skeleton
→ Run Test → Confirm Failure(RED) → GREEN Task → REFACTOR Candidate
```

---

## 2. PRD Summary

### 프로젝트 목적

4×4 Magic Square 문제를 통해 **검증 가능한 불변식**, **고정된 입출력 계약**, **Boundary/Domain 분리**, **RED-GREEN-REFACTOR 흐름**, **Concept-to-Code Traceability**를 훈련합니다.

### 학습 목표

| 목표 | 설명 |
|------|------|
| 불변식 사고 | "항상 참이어야 하는 규칙"을 테스트 가능한 문장으로 고정 |
| 계약 기반 개발 | 입력/출력/오류 스키마를 구현 전에 확정 |
| Dual-Track TDD | Track A(Boundary 계약)와 Track B(Domain 규칙)를 병렬 RED 진행 |
| ECB 아키텍처 | boundary → control → entity 의존 방향 준수 |
| 회귀 보호 | 계약·불변식 테스트를 변경 방어선으로 유지 |

### 핵심 도메인 규칙

| 규칙 | 내용 |
|------|------|
| 격자 크기 | 4×4 int 행렬 |
| 빈칸 | `0` = 빈칸, **정확히 2개** |
| 값 범위 | `0` 또는 `1~16` |
| 중복 | `0`을 제외한 값은 중복 불가 |
| Magic Constant | 4×4 마방진 합 = **34** |
| 빈칸 순서 | row-major(행 1→4, 열 1→4) 스캔, 첫 `0` = 첫 번째 빈칸 |
| 조합 시도 | Attempt1: small→첫 빈칸, large→둘째 빈칸 → 실패 시 Attempt2: 반대 |
| 출력 | `int[6] = [r1, c1, n1, r2, c2, n2]`, 좌표 **1-index** |

### 입력 계약

| 필드 | 규칙 | 오류 코드 |
|------|------|-----------|
| `matrix` | 4×4 (행=4, 각 행 열=4) | `INVALID_SIZE` |
| `cell value` | `0` 또는 `1~16` | `INVALID_VALUE_RANGE` |
| blanks | `0` 개수 = 2 | `INVALID_EMPTY_COUNT` |
| duplicates | 비0 값 중복 금지 | `INVALID_DUPLICATE` |

입력 검증 실패 시 **Domain Solver를 호출하지 않습니다.**

### 출력 계약

**성공**

| 필드 | 규칙 |
|------|------|
| `result` | `int[6]`, `[r1, c1, n1, r2, c2, n2]` |
| 좌표 | `r1,c1,r2,c2` ∈ [1, 4] (1-index) |
| 숫자 | `n1, n2` ∈ [1, 16], `n1 ≠ n2` |
| 순서 | Attempt1 성공: `n1=small`; Attempt2 성공: `n1=large` |

**오류**

| 조건 | 코드 | 메시지 |
|------|------|--------|
| 4×4 아님 | `INVALID_SIZE` | `Grid must be 4x4.` (AC-FR-01-01 테스트 계약; PRD §13은 `Matrix must be 4x4.` — [defect_list.md](defect_list.md) DEF-006) |
| 빈칸 ≠ 2 | `INVALID_EMPTY_COUNT` | `Exactly 2 empty cells (0) are required.` |
| 범위 위반 | `INVALID_VALUE_RANGE` | `Each cell must be 0 or an integer from 1 to 16.` |
| 중복 | `INVALID_DUPLICATE` | `Non-zero values must not duplicate.` |
| 두 조합 실패 | `DOMAIN_NO_SOLUTION` | `No valid magic square completion exists.` |

### 성공 기준

- 유효 입력에 대해 **결정적(deterministic)** 결과 반환
- Boundary 검증 실패 시 표준 오류 + Domain 미호출
- Domain 두 조합 시도 규칙(I8) 준수
- 입력 행렬 **부작용 없음**(원본 변경 금지)
- Domain Logic 커버리지 **95%+**, Boundary Validation 커버리지 **85%+**
- 모든 테스트 pytest + AAA 패턴, 테스트 약화 없이 통과

---

## 3. TDD Development Flow

```
Scenario
  → Acceptance Criteria
  → RED Test ID
  → Test Skeleton
  → Run Test
  → Confirm Failure = RED
  → Minimal Implementation = GREEN
  → Structure Improvement = REFACTOR
```

| 단계 | 의미 |
|------|------|
| **Scenario** | 사용자·시스템 관점의 구체적 상황을 Gherkin 스타일(Given-When-Then)로 정의합니다. |
| **Acceptance Criteria** | Scenario를 **측정 가능한 한 문장**으로 변환합니다. 테스트 assertion의 직접 근거가 됩니다. |
| **RED Test ID** | 추적성을 위해 각 AC에 고유 ID(예: `RED-BND-001`)를 부여합니다. |
| **Test Skeleton** | pytest 테스트 함수·파일 **골격**을 작성합니다. AAA 구조만 갖추고 구현은 아직 없습니다. |
| **Run Test** | `pytest`로 테스트를 실행합니다. |
| **Confirm Failure = RED** | 테스트가 **의도한 이유로** 실패하는지 확인합니다. RED 확인 없이 구현을 시작하지 않습니다. |
| **Minimal Implementation = GREEN** | RED 실패를 통과시키기 위한 **최소 구현 작업 후보**만 적용합니다. 이 단계에서 리팩터링하지 않습니다. |
| **Structure Improvement = REFACTOR** | GREEN 이후, 계약·기능 변경 없이 구조만 개선하는 **후보**를 검토합니다. 테스트는 계속 통과해야 합니다. |

---

## 4. Development Methodology

### Dual-Track UI + Logic TDD

| Track | 대상 | RED 범위 |
|-------|------|----------|
| **Track A — Boundary RED** | 입력 검증, 오류 응답, 출력 형식, Domain 미호출 | `InputValidator`, `PuzzleBoundary` |
| **Track B — Logic RED** | 빈칸/누락/판정/조합 시도 | `BlankFinder`, `MissingNumberFinder`, `MagicSquareValidator`, `Solver` |

두 Track은 **Mock으로 분리**하여 병렬 RED가 가능합니다. Domain 전부 완료 후 Boundary 연결하는 순차 방식은 금지합니다.

### Boundary RED와 Logic RED의 분리

- Boundary 테스트: Domain을 **Mock** — 계약(입력/출력/오류)만 검증
- Logic 테스트: Boundary를 **참조하지 않음** — 순수 도메인 규칙만 검증
- Integration RED: Mock 없이 end-to-end 경로 검증 (양 Track GREEN 이후)

### ECB 역할 분리

의존 방향: **boundary → control → entity** (역방향 금지)

### Concept-to-Code Traceability

모든 Concept/Invariant는 User Story → Scenario → AC → RED Test ID → Test Skeleton → Code Target까지 **1:1 추적** 가능해야 합니다.

### RED → GREEN → REFACTOR 원칙

| 단계 | 규칙 |
|------|------|
| RED | 테스트 먼저, **실패 상태 확인** 후에만 진행 |
| GREEN | 테스트 통과에 필요한 **최소 코드**만, 리팩터링 금지 |
| REFACTOR | 기능·계약 불변, 구조 개선만, 테스트 약화/삭제 금지 |

---

## 5. ECB Role Separation

| ECB Layer | Responsibility | Example Component |
|-----------|----------------|-------------------|
| **Entity** | Board 상태와 순수 도메인 규칙을 표현한다. 마방진 판정, 빈칸/누락 탐색 등 I/O 없는 순수 로직. UI·DB·Web·파일 시스템에 **의존하지 않는다.** | `MagicBoard`, `BlankFinder`, `MissingNumberFinder`, `MagicSquareValidator`, `MagicConstant` |
| **Control** | Boundary와 Entity 사이에서 검증 통과 후 해 결정 **흐름을 조정**한다. 두 조합 시도 순서, UseCase 오케스트레이션. | `Solver`, `SolveTwoBlanksUseCase` |
| **Boundary** | 입력 검증, 출력 형식, 오류 정책, Control 호출을 담당한다. Domain Invariant를 **직접 구현하지 않는다.** | `InputValidator`, `PuzzleBoundary`, `DomainErrorMapper` |

---

## 6. Scenario → AC → RED → GREEN Tracking Board

| Status | Scenario ID | Scenario Summary | Acceptance Criteria | RED Test ID | Test Skeleton Candidate | Expected RED Failure | GREEN Task Candidate | REFACTOR Candidate | ECB Layer | Code Target |
|--------|-------------|------------------|---------------------|-------------|-------------------------|----------------------|----------------------|----------------------|-----------|-------------|
| - [ ] | SC-BND-001 | `None` 입력 | `None` 입력 시 `INVALID_SIZE` 오류 반환, Domain Solver 미호출 | RED-BND-001 | `tests/boundary/test_input_validator.py::test_validate_none_input_returns_invalid_size` | `InputValidator` 미구현 → `ImportError` 또는 assertion 실패 | `None` 감지 후 `ErrorResponse(code="INVALID_SIZE")` 반환 최소 분기 | `ErrorCode` Enum + `ERROR_MESSAGES` 상수 dict 추출 | Boundary | `InputValidator`, `PuzzleBoundary` |
| - [ ] | SC-BND-002 | 4×4가 아닌 입력 | 행≠4 또는 열≠4이면 `INVALID_SIZE` 반환, Domain Solver 미호출 | RED-BND-002 | `tests/boundary/test_input_validator.py::test_validate_non_4x4_matrix_returns_invalid_size` | 크기 검증 로직 없음 → `code == "INVALID_SIZE"` assertion 실패 | 행 수·각 행 길이 4 확인 `_check_size()` 최소 구현 | jagged/빈 리스트 케이스별 private 검증 함수 분리 | Boundary | `InputValidator` |
| - [ ] | SC-BND-003 | 빈칸 개수 오류 | `0` 개수 ≠ 2이면 `INVALID_EMPTY_COUNT` 반환, Domain Solver 미호출 | RED-BND-003 | `tests/boundary/test_input_validator.py::test_validate_wrong_blank_count_returns_invalid_empty_count` | 빈칸 개수 검증 없음 → `INVALID_EMPTY_COUNT` assertion 실패 | `0` 카운트 == 2 확인 최소 로직 | `_count_blanks(matrix) -> int` 헬퍼 추출 | Boundary | `InputValidator` |
| - [ ] | SC-BND-004 | 값 범위 오류 | 셀 값이 0 또는 1~16이 아니면 `INVALID_VALUE_RANGE` 반환 | RED-BND-004 | `tests/boundary/test_input_validator.py::test_validate_out_of_range_value_returns_invalid_value_range` | 범위 검증 없음 → `INVALID_VALUE_RANGE` assertion 실패 | 셀별 `0 <= v <= 16` (비0는 1~16) 최소 검사 | `MIN_CELL_VALUE`/`MAX_CELL_VALUE` 명명 상수 도입 | Boundary | `InputValidator` |
| - [ ] | SC-BND-005 | 중복 숫자 오류 | 비0 값 중복 시 `INVALID_DUPLICATE` 반환, Domain Solver 미호출 | RED-BND-005 | `tests/boundary/test_input_validator.py::test_validate_duplicate_non_zero_returns_invalid_duplicate` | 중복 검증 없음 → `INVALID_DUPLICATE` assertion 실패 | 비0 값 multiset vs 고유 개수 비교 최소 구현 | `_find_duplicates(values) -> set[int]` 분리 | Boundary | `InputValidator` |
| - [ ] | SC-DOM-001 | 빈칸 좌표 row-major 탐색 | row-major 첫 `0` = firstBlank, 둘째 `0` = secondBlank, 좌표 1-index | RED-DOM-001 | `tests/entity/test_blank_finder.py::test_find_blanks_row_major_returns_first_and_second_1_indexed` | `BlankFinder` 미구현 → 좌표 assertion 실패 | row 1→4, col 1→4 순회 후 0 두 좌표 반환 최소 구현 | `CellPosition` Value Object + `BlankFinder` Domain Service 분리 | Entity | `BlankFinder`, `MagicBoard` |
| - [ ] | SC-DOM-002 | 누락 숫자 오름차순 탐색 | 1~16 중 미포함 2개 반환, `small < large` | RED-DOM-002 | `tests/entity/test_missing_number_finder.py::test_find_missing_returns_two_numbers_in_ascending_order` | `MissingNumberFinder` 미구현 → 누락 숫자 assertion 실패 | `set(1..16) - present` 차집합 후 정렬 반환 최소 구현 | `MissingNumbers(small, large)` dataclass 도입 | Entity | `MissingNumberFinder` |
| - [ ] | SC-DOM-003 | 모든 행 합 34 검증 | 4행 각 합 = 34 → true, 하나라도 ≠34 → false | RED-DOM-003 | `tests/entity/test_magic_square_validator.py::test_validate_row_sums_all_34_returns_true` | 행 합 검증 함수 없음 → boolean assertion 실패 | 4행 `sum(row) == MAGIC_CONSTANT` 비교 최소 구현 | `_check_row_sums(grid) -> bool` private 메서드 추출 | Entity | `MagicSquareValidator` |
| - [ ] | SC-DOM-004 | 모든 열 합 34 검증 | 4열 각 합 = 34 → true, 하나라도 ≠34 → false | RED-DOM-004 | `tests/entity/test_magic_square_validator.py::test_validate_col_sums_all_34_returns_true` | 열 합 검증 없음 → boolean assertion 실패 | 열별 합산 후 `MAGIC_CONSTANT` 비교 최소 구현 | 행/열 합 공통 `_sum_lines()` 헬퍼 추출 | Entity | `MagicSquareValidator` |
| - [ ] | SC-DOM-005 | 두 대각선 합 34 검증 | 주·반대각 합 = 34 → true, 하나라도 ≠34 → false | RED-DOM-005 | `tests/entity/test_magic_square_validator.py::test_validate_diag_sums_all_34_returns_true` | 대각선 합 검증 없음 → boolean assertion 실패 | `grid[i][i]`, `grid[i][3-i]` 합 비교 최소 구현 | `MagicConstant` Value Object로 34 캡슐화 | Entity | `MagicSquareValidator`, `MagicConstant` |
| - [ ] | SC-DOM-006 | small-first 성공 | Attempt1(small→first, large→second) 성공 시 `[r1,c1,small,r2,c2,large]` 반환 | RED-DOM-006 | `tests/control/test_solve_two_blanks_use_case.py::test_solve_small_first_attempt_succeeds_returns_correct_order` | `Solver`/`UseCase` 미구현 → 결과 배열 assertion 실패 | BlankFinder + MissingNumberFinder + Validator 조합 Attempt1 시도·성공 반환 | `TwoAssignmentTrial` Domain Service로 조합 생성 분리 | Control | `Solver`, `SolveTwoBlanksUseCase` |
| - [ ] | SC-DOM-007 | small-first 실패 후 reverse 성공 | Attempt1 실패 → Attempt2(large→first, small→second) 성공 시 `n1=large, n2=small` | RED-DOM-007 | `tests/control/test_solve_two_blanks_use_case.py::test_solve_reverse_attempt_succeeds_after_small_first_fails` | reverse 시도 분기 없음 → `n1 > n2` 기대 assertion 실패 | Attempt1 false 시 Attempt2 실행 후 성공 결과 반환 | `SolutionOrderResolver`로 n1/n2 순서 결정 책임 분리 | Control | `Solver`, `SolveTwoBlanksUseCase` |
| - [ ] | SC-DOM-008 | 두 조합 모두 실패 | Attempt1·Attempt2 모두 비마방진 → `NoValidCompletion` / `DOMAIN_NO_SOLUTION` | RED-DOM-008 | `tests/control/test_solve_two_blanks_use_case.py::test_solve_both_attempts_fail_raises_no_valid_completion` | 실패 정책 미구현 → 예외 미발생 또는 잘못된 성공 반환 | 양쪽 판정 false 시 `NoValidCompletion` 반환/발생 최소 구현 | Domain 실패 Result vs 예외 1종 통일 | Control | `Solver`, `NoValidCompletion` |
| - [ ] | SC-INT-001 | 결과 배열 길이 6 | 성공 응답 `result` 길이 = 6, `[r1,c1,n1,r2,c2,n2]` 형식 | RED-INT-001 | `tests/boundary/test_puzzle_boundary.py::test_submit_valid_puzzle_returns_result_length_six` | end-to-end `submit()` 미구현 → `len(result) == 6` assertion 실패 | Boundary→Control→Entity 연결 후 6원소 list 반환 | `Solution6` dataclass + `to_list()` 변환기 추출 | Boundary | `PuzzleBoundary`, `ResultFormatter` |
| - [ ] | SC-INT-002 | 반환 좌표 1-index | `r1,c1,r2,c2` 모두 1~4 범위, 0-index 변환 없이 1-index 유지 | RED-INT-002 | `tests/boundary/test_puzzle_boundary.py::test_submit_valid_puzzle_returns_1_indexed_coordinates` | 0-index 반환 또는 미구현 → 좌표 범위 assertion 실패 | BlankFinder 1-index 좌표를 출력에 그대로 전달 | 내부 0-index / 외부 1-index 변환을 Boundary에서만 처리 | Boundary | `PuzzleBoundary`, `BlankFinder` |

상세 TASK 목록(20건) 및 Traceability: [Report/08. TDD To-Do List](Report/08.%20MagicSquare_TDD_ToDoList_Report.md)

---

## 7. RED Start Checklist

RED 단계 착수·유지 시 아래를 확인합니다. **커밋·GREEN 진행 추적은 §7.1·§7.2를 SSOT로 사용합니다.**

- [x] 모든 Scenario가 정의되었는가?
- [x] 모든 Acceptance Criteria가 테스트 가능한 문장인가?
- [x] Dual-Track RED Test ID (`RED-BND-*`, `D-*`, `U-*`)가 부여되었는가?
- [x] R1 Test Skeleton 작성 완료 (`test_ac_fr_01_01_*.py` 25건)
- [ ] R2~R4: `pytest.fail` 스텁 → assertion RED 전환 (§7.1)
- [x] Boundary RED와 Logic RED가 분리되었는가? (Track A mock / Track B Domain Mock 금지)
- [x] ECB Layer가 명확히 지정되었는가?
- [ ] RED 확인 없이 GREEN 확장 금지 (G-01 size 분기 등 잔여 9건 우선)
- [ ] REFACTOR는 GREEN 완료 후만 (§7.2 Phase 마무리)

---

## 7.1 RED 커밋 체크리스트 (Dual-Track)

> 각 RED 커밋 후 `pytest`로 **의도적 RED**를 확인한 뒤에만 GREEN으로 진행합니다.  
> 상세 설계: [Report/13 FR-01~FR-05 Dual-Track RED](Report/13.%20MagicSquare_FR01_FR05_DualTrack_RED_Design_Report.md) · [docs/test_plan.md](docs/test_plan.md)

| 커밋 | 포함 Test ID | 파일 | 건수 |
|------|--------------|------|:----:|
| **R1** | `AC-FR-01-01` / `RED-BND-001`·`002`·`006` | `tests/boundary/test_ac_fr_01_01_*.py`, `conftest.py` | 25 |
| **R2** | `D-LOC-01` ~ `D-VAL-06` | `tests/entity/test_d_loc_01_*.py` … `test_d_val_06_*.py` | 8 |
| **R3** | `D-SOL-01` ~ `D-SOL-04` | `tests/entity/test_d_sol_01_*.py` … `test_d_sol_04_*.py` | 4 |
| **R4** | `U-FLOW-02` ~ `U-OUT-03` | `tests/boundary/test_u_*.py` | 12 |
| **R5** (선택) | `U-IN-01` ~ `U-IN-03` | 신규 `tests/boundary/test_u_in_0*.py` | 4 |

### R1 — AC-FR-01-01 (기착수)

- [x] R1 테스트·fixture 작성 (`test_ac_fr_01_01_*.py`, `conftest.py`)
- [ ] R1 RED 확인: `python -m pytest tests/boundary/test_ac_fr_01_01_*.py -v`
- [ ] R1 git 커밋: `test(red): AC-FR-01-01 boundary RED — 25 cases`

### R2 — Entity D-LOC / D-MIS / D-VAL

- [ ] `pytest.fail` 스텁 → Given-When-Then + assertion RED로 교체
- [ ] R2 RED 확인: `python -m pytest tests/entity/test_d_loc_01_*.py tests/entity/test_d_mis_01_*.py tests/entity/test_d_val_*.py -v`
- [ ] R2 git 커밋: `test(red): entity D-LOC/D-MIS/D-VAL RED — 8 cases`

### R3 — D-SOL (Control/Entity)

- [ ] G2/G3 격자 픽스처 SSOT 고정 후 assertion RED 작성
- [ ] R3 RED 확인: `python -m pytest tests/entity/test_d_sol_*.py -v`
- [ ] R3 git 커밋: `test(red): entity/control D-SOL RED — 4 cases`

### R4 — Boundary U-FLOW / U-IN / U-OUT

- [ ] `pytest.fail` 스텁 → assertion RED로 교체 (U-OUT는 UseCase mock/spy)
- [ ] R4 RED 확인: `python -m pytest tests/boundary/test_u_*.py -v`
- [ ] R4 git 커밋: `test(red): boundary U-FLOW/U-IN/U-OUT RED — 12 cases`

### R5 (선택) — U-IN-01 ~ U-IN-03

- [ ] `INVALID_SIZE` vs E00x envelope 매핑 결정
- [ ] 신규 RED 4건 작성·RED 확인·커밋

---

## 7.2 GREEN 단계 Todo List

> RED 묶음과 1:1이 아닌 **의존성 순서**입니다. GREEN 단계에서 **리팩터링·테스트 약화·skip 금지**.

### Phase 0 — 공통

- [ ] `python -m pytest tests/ -q` 기준선 기록
- [ ] ECB `boundary → control → entity` 역의존 없음 확인

### G-01 — R1 대응: AC-FR-01-01 완료

**Test ID:** `RED-BND-001`, `RED-BND-002`, `RED-BND-006`

- [x] `None` / `[]` → `INVALID_SIZE` + `Grid must be 4x4.`
- [ ] `_is_valid_size()`: `[[]]*4`, 3×4, 4×3, 5×5 → `INVALID_SIZE`
- [ ] `FailureResponse` ↔ 테스트 `ErrorResponse` 계약 정합
- [ ] `PuzzleBoundary.submit`: invalid 시 `execute` 0회 early return
- [ ] GREEN 확인: `python -m pytest tests/boundary/test_ac_fr_01_01_*.py -v` → **25 passed**
- [ ] git 커밋: `feat(green): AC-FR-01-01 size validation and boundary isolation`

### G-02 — R2 (1/2): D-LOC-01, D-MIS-01

- [ ] `find_blank_coords(G1)` → 1-index `(2,2)`, `(3,3)`
- [ ] `find_not_exist_nums(G1)` → `(7, 10)` 오름차순
- [ ] GREEN 확인 · git 커밋

### G-03 — R2 (2/2): D-VAL-01 ~ D-VAL-06

- [ ] `MagicConstant` = 34 · `is_magic_square` 행/열/대각/집합/0 금지
- [ ] GREEN 확인 · git 커밋

### G-04 — R3: D-SOL-01 ~ D-SOL-04

- [ ] G1 Attempt A · G2 reverse · G3 `UnsolvableDomainError` · 출력 shape
- [ ] GREEN 확인 · git 커밋

### G-05 — R4 (1/2): U-IN-04 ~ U-IN-08 (+ R5 시 U-IN-01~03)

- [ ] short-circuit: size → empty → range → duplicate (E001~E005 envelope)
- [ ] GREEN 확인 · git 커밋

### G-06 — R4 (2/2): U-FLOW-02 (a~d)

- [ ] invalid 유형별 `execute.call_count == 0`
- [ ] GREEN 확인 · git 커밋

### G-07 — R4 (3/3): U-OUT-01 ~ U-OUT-03

- [ ] G1 + UseCase mock → len=6, 1-index coords, `n1≠n2`
- [ ] GREEN 확인 · git 커밋

### Phase 마무리

- [ ] 전체: `python -m pytest tests/ -v` → **53 passed** (R5 제외 시 49)
- [ ] Boundary 커버리지 ≥ 85%: `pytest tests/boundary/ --cov=src/boundary --cov-fail-under=85`
- [ ] REFACTOR 백로그 분리 (G-* 커밋과 분리)

### RED → GREEN 매핑

| RED | 건수 | GREEN |
|-----|:----:|-------|
| R1 | 25 | G-01 |
| R2 | 8 | G-02, G-03 |
| R3 | 4 | G-04 |
| R4 | 12 | G-05, G-06, G-07 |
| R5 (선택) | 4 | G-05에 병합 |

**권장 진행:** `R1✓ → G-01 → R2 → G-02 → G-03 → R3 → G-04 → R4 → G-05 → G-06 → G-07 → (R5) → 마무리`

### AC-FR-01-01 Track A (R1 세부 — [docs/test_plan.md](docs/test_plan.md))

- [x] TC-A-01: `grid=None` → 실패 결과 반환
- [x] TC-A-02: `code == "INVALID_SIZE"`
- [x] TC-A-03: `message == "Grid must be 4x4."`
- [x] TC-A-04: `grid=None` 시 `execute` 0회 (mock/spy)
- [x] TC-A-05: `grid=[]` → `INVALID_SIZE`
- [ ] TC-A-06: 3×4·4×3·5×5·`[[]]*4` → `INVALID_SIZE` (GREEN G-01)
- [ ] TC-A-07: 반환 타입 계약 (`FailureResponse` / `ErrorResponse` 정합)

### 커버리지 · 결함

- [ ] Domain Logic: 95%+ (`pytest-cov`)
- [ ] Boundary Layer: 85%+
- [ ] 전체 TOTAL: 90%+
- [x] [defect_list.md](defect_list.md) 생성 (DEF-001~006, 2026-05-29)
- [ ] 모든 결함 수정 후 회귀 테스트 통과

---

## 8. Quality Gates

| 항목 | 기준 |
|------|------|
| Domain Logic 커버리지 | **95%+** |
| Boundary Validation 커버리지 | **85%+** |
| 테스트 프레임워크 | **pytest** |
| 테스트 패턴 | **AAA (Arrange-Act-Assert)** |
| 테스트 약화 | **금지** (삭제/완화/skip/무의미 assertion으로 통과 금지) |
| 디버깅 출력 | **`print()` 금지** — assertion, logging, 디버거 사용 |
| 매직 넘버 | **금지** — `GRID_SIZE`, `MAX_VALUE`, `MAGIC_CONSTANT` 등 명명 상수 |
| 타입 힌트 | **필수** — 모든 함수/메서드 |
| 코드 스타일 | **PEP8**, max line length 88 |
| Python 버전 | **3.14+** |
| 계약 변경 | **금지** — 입력/출력/오류 코드·메시지는 PRD §12·§13 고정 |
| ECB 의존 방향 | boundary → control → entity (역방향 금지) |
| bare except | **`except:` 금지** — 구체 예외 또는 `except Exception` |
| 입력 부작용 | Solver/Validator 실행 후 **원본 matrix 변경 금지** |

---

## 9. Reference Documents

| 문서 | 역할 |
|------|------|
| [Report/07. PRD](Report/07.%20MagicSquare_PRD_Report.md) | PRD 요약·요구사항·입출력 계약·오류 정책·Dual-Track TDD 전략 **1차 기준** |
| [Report/08. TDD To-Do List](Report/08.%20MagicSquare_TDD_ToDoList_Report.md) | Scenario→AC→RED→GREEN Tracking Board 20 TASK, Traceability 16 Concept |
| [Report/09. README Start Guide](Report/09.%20MagicSquare_README_StartGuide_Report.md) | 본 README 정본 Report |
| [Report/06. Level1-5 Scenario Verification](Report/06.%20MagicSquare_Level1-5_Scenario_Verification_Report.md) | Epic → User Story → Scenario → AC 연결 일관성 검증 |
| [Report/02. Architecture & Contracts](Report/02.%20MagicSquare_Architecture_Contracts_Report.md) | 입력/출력 계약, Domain Invariant(I1~I8), Layer Boundary |
| [Report/02.design.md](Report/02.design.md) | 불변 조건별 RED/GREEN 테스트 케이스, TDD 실행 순서 |
| [Report/10. AC-FR-01-01 RED QA](Report/10.%20MagicSquare_AC_FR_01_01_RED_QA_Report.md) | AC-FR-01-01 RED 25건·실행 결과·GREEN 제안 |
| [Report/13. FR-01~FR-05 Dual-Track RED](Report/13.%20MagicSquare_FR01_FR05_DualTrack_RED_Design_Report.md) | `U-*` / `D-*` SSOT 21건 RED 설계표 |
| [Report/16. RED/GREEN Todo & README](Report/16.%20MagicSquare_RED_GREEN_TodoList_README_Update_Report.md) | R1~R5 · G-01~G-07 체크리스트 · SSOT ID 오름차순 · README 갱신 |
| [docs/test_plan.md](docs/test_plan.md) | AC-FR-01-01 테스트 계획·경계값·실행 순서 |
| [defect_list.md](defect_list.md) | RED 단계 결함 추적 (DEF-001~006) |
| [Prompting/16. RED/GREEN Todo Transcript](Prompting/16.%20MagicSquare_RED_GREEN_TodoList_README_Update_Transcript.md) | 본 세션 Turn 1~4 대화 Export |
| [Report/03. User Entity ECB/TDD](Report/03.%20MagicSquare_UserEntity_ECB_TDD_Report.md) | ECB entity TDD 적용 사례(User) |
| [Report/04. CursorRules Extension](Report/04.%20MagicSquare_CursorRules_Extension_Report.md) | `.cursorrules` → `.cursor/rules/*.mdc` 분리 구성 |
| [Report/01. Problem Recognition](Report/01.%20MagicSquare_ProblemRecognition_Report.md) | 문제 인식·불변식 정의 |
| `.cursorrules` / `.cursor/rules/*.mdc` | Cursor 개발 규칙 (ECB, TDD, 금지 패턴) |

### 문서 간 관계

```
01 Problem Recognition
  └─▶ 02 Architecture & Contracts (+ 02.design)
        └─▶ 06 Scenario Verification
              └─▶ 07 PRD
                    └─▶ 08 To-Do List + 09 README (본 문서)
                          └─▶ tests/ + src/ (RED → GREEN → REFACTOR)
```

---

## 10. Current Project Status

| 항목 | 상태 |
|------|------|
| 문제 인식 (STEP 1~5) | ✅ 완료 |
| STEP 6 TDD 설계 | ✅ 완료 |
| 아키텍처·계약·PRD | ✅ 완료 |
| FR-01~FR-05 Dual-Track RED 설계 | ✅ [Report/13](Report/13.%20MagicSquare_FR01_FR05_DualTrack_RED_Design_Report.md) |
| **R1** AC-FR-01-01 RED (25건) | ✅ 기착수 |
| **R2~R4** `D-*` / `U-*` RED | 🔄 스텁(`pytest.fail`) — assertion RED 전환·커밋 대기 |
| **G-01** AC-FR-01-01 GREEN | 🔄 진행 중 (`None`/`[]` 통과, size·격리 9건 FAIL) |
| **pytest** (전체) | 20 passed · 33 failed · 53 collected |
| **REFACTOR** | ❌ GREEN 완료 후 (§7.2 Phase 마무리) |

### 다음 단계 (즉시)

1. **G-01** 완료: `_is_valid_size()` · `PuzzleBoundary` early return · 응답 타입 정합 → `test_ac_fr_01_01_*` 25 passed
2. **R2** assertion RED 확정 후 커밋 → **G-02** · **G-03**
3. **R3** → **G-04** → **R4** → **G-05** · **G-06** · **G-07**

### 테스트 실행

```powershell
# AC-FR-01-01만 (G-01 목표: 25 passed)
python -m pytest tests/boundary/test_ac_fr_01_01_*.py -v

# 전체 기준선
python -m pytest tests/ -q

# RED 커밋별
python -m pytest tests/entity/test_d_loc_01_*.py tests/entity/test_d_val_*.py -v
python -m pytest tests/boundary/test_u_*.py -v
```

### 권장 진행 순서 (RED 커밋 → GREEN)

```
R1 (AC-FR-01-01, 25) ──▶ G-01
R2 (D-LOC~D-VAL, 8)  ──▶ G-02, G-03
R3 (D-SOL, 4)        ──▶ G-04
R4 (U-*, 12)         ──▶ G-05, G-06, G-07
R5 (U-IN-01~03, 4)   ──▶ G-05에 병합 (선택)
```

---

## 브랜치 전략

| 브랜치 | 역할 |
|--------|------|
| `main` | 안정 기준선 (문서·PRD 통합본) |
| `spec` | 명세·계약·PRD 기준 |
| `develop` | 통합 브랜치 (선택) |
| `feature/*` | RED → GREEN → REFACTOR 구현 단위 |

**PR 흐름:** `feature/...` → `main` (또는 `develop` → `main`)

---

## 디렉터리 구조

```
MagicSquare_xx/
├── README.md
├── defect_list.md
├── docs/test_plan.md
├── .cursor/rules/              # ECB · TDD · 코드 스타일 규칙
├── Report/                     # PRD · RED 설계 · QA 보고서
├── src/
│   ├── boundary/               # InputValidator, PuzzleBoundary, schemas
│   ├── control/                # SolveTwoBlanksUseCase (스텁)
│   └── entity/                 # user.py (예제) · 향후 BlankFinder 등
└── tests/
    ├── boundary/
    │   ├── conftest.py
    │   ├── test_ac_fr_01_01_*.py   # R1 — 25건
    │   └── test_u_*.py             # R4 — 12건
    └── entity/
        ├── test_user.py
        ├── test_d_loc_01_*.py      # R2
        ├── test_d_val_*.py         # R2
        └── test_d_sol_*.py         # R3
```

---

## 라이선스 / 기여

미정 (프로젝트 초기 단계)

---

*구현·테스트는 RED 실패 확인 후 GREEN 최소 코드만 추가합니다. 진행 상태는 §7.1·§7.2·§10 체크리스트를 SSOT로 갱신합니다.*
