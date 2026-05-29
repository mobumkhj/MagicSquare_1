# MagicSquare_1

4×4 마방진(Magic Square) TDD 학습·실습 프로젝트입니다.

**Repository:** [github.com/mobumkhj/MagicSquare_1](https://github.com/mobumkhj/MagicSquare_1)

**현재 단계:** 문제 인식(STEP 1~5) · 아키텍처·계약 설계 · PRD 작성 · PRD 검토까지 완료. **구현(STEP 7)은 feature 브랜치 + PR로 진행 예정.**

---

## 프로젝트 목적

고정된 **4×4 격자**와 **1~16(각 숫자 한 번)** 위에서,

- 그 배치가 규칙을 만족하는지 **일관되게 판정**하고
- 필요할 때만 규칙을 만족하는 배치를 **제시**할 수 있는 기반을 마련하는 것

중심은 “16칸을 맞추는 손맛”이 아니라 **규칙·불변 조건·입출력 계약·Dual-Track TDD**를 훈련하는 것입니다.

---

## 현재 상태

| 항목 | 상태 |
|------|------|
| 문제 인식 (STEP 1~5) | 완료 |
| STEP 6 TDD 설계 | 완료 |
| 아키텍처·계약·테스트 설계 | 완료 |
| PRD (구현 전 기준) | 완료 |
| PRD 검토 | 완료 |
| Magic Square 구현 | 미착수 |
| 샘플 코드 | User 엔티티(ECB/TDD 예제)만 존재 |

---

## 진행 단계

| 단계 | 내용 | 상태 |
|------|------|------|
| STEP 1~5 | 문제 인식 · Why chain · Invariant | 완료 |
| STEP 6 | TDD 설계 | 완료 |
| STEP 7 | 구현 (feature 브랜치 + PR) | 예정 |

---

## 브랜치 전략

| 브랜치 | 역할 |
|--------|------|
| `main` | 안정 기준선 (문서·PRD 통합본) |
| `spec` | 명세·계약·PRD 기준 (현재 `main`과 동일 커밋) |
| `develop` | 통합 브랜치 (선택) |
| `feature/*` | RED → GREEN → REFACTOR 구현 단위 |

**PR 흐름:** `feature/...` → `main` (또는 `develop` → `main`)

문서·설계는 이미 `main`에 반영되어 있으므로, **다음 PR은 구현 feature 브랜치에서 생성**합니다.

---

## 문제 정의 요약 (STEP 5)

> 4×4, 1~16(각 1회) 배치가 **모든 행·열·두 대각선의 합이 동일한지**를 **재현 가능하게 판정**하고, 필요 시에만 그 조건을 만족하는 배치를 **제시**한다.

| 구분 | 내용 |
|------|------|
| 핵심 능력 1 | **판정** (필수) |
| 핵심 능력 2 | **제시** (선택) |
| 마법 상수 | 34 |

### 고정 입출력 계약 (요약)

- **입력:** 4×4 `int[][]`, `0`=빈칸, 빈칸 2개, 값 `0` 또는 `1~16`, 0 제외 중복 금지
- **출력:** `int[6]` = `[r1,c1,n1,r2,c2,n2]`, 좌표 **1-index**, small-first → reverse 시도

상세: [07. PRD](Report/07.%20MagicSquare_PRD_Report.md)

---

## 핵심 Invariant

| ID | 내용 |
|----|------|
| I1 | 16개 값 = {1, …, 16} |
| I2 | 네 행·네 열·두 대각선의 합이 모두 동일 |
| I3 | 공통 합 = 34 |
| I5 | 동일 입력 → 동일 판정 결과 |
| I7 | 불만족 시 침묵 성공 없음 |

---

## 디렉터리 구조

```
MagicSquare_1/
├── README.md
├── .cursorrules
├── .cursor/rules/          # ECB · TDD · 코드 스타일 규칙
├── Report/                 # 보고서 (문제 인식 ~ PRD 검토)
├── Prompting/              # 대화·프롬프트 Transcript
├── src/                    # ECB 소스 (entity 예제)
│   └── entity/
└── tests/                  # pytest (entity 예제)
    └── entity/
```

---

## 문서

| 문서 | 설명 |
|------|------|
| [01. MagicSquare_ProblemRecognition_Report.md](Report/01.%20MagicSquare_ProblemRecognition_Report.md) | STEP 1~5 문제 인식 |
| [01.problem-definition.md](Report/01.problem-definition.md) | 문제 정의 보고서 |
| [02.design.md](Report/02.design.md) | STEP 6 TDD 설계 |
| [02. MagicSquare_Architecture_Contracts_Report.md](Report/02.%20MagicSquare_Architecture_Contracts_Report.md) | Dual-Track / Clean Architecture · 계약 |
| [03. MagicSquare_UserEntity_ECB_TDD_Report.md](Report/03.%20MagicSquare_UserEntity_ECB_TDD_Report.md) | User 엔티티 ECB/TDD 예제 |
| [06. Level1-5 Scenario Verification](Report/06.%20MagicSquare_Level1-5_Scenario_Verification_Report.md) | Epic→Scenario 검증 |
| [07. PRD](Report/07.%20MagicSquare_PRD_Report.md) | 구현 전 PRD |
| [08. PRD 검토](Report/08.%20MagicSquare_PRD_Review_Report.md) | PRD 7기준 검토 |

---

## 개발 규칙 (요약)

- Python 3.14+, PEP8, type hints 필수
- ECB: `boundary → control → entity`
- Dual-Track TDD: Boundary 계약 / Domain 불변식 분리
- RED 확인 없이 구현 금지, 테스트 약화 금지

상세: `.cursorrules`, `.cursor/rules/*.mdc`

---

## 라이선스 / 기여

미정 (프로젝트 초기 단계)
