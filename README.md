# MagicSquare_07

4×4 마방진(Magic Square)을 다루는 학습·실습 프로젝트입니다.  
**문제 인식(STEP 1~5)**, **아키텍처·계약 설계**, **PRD**까지 완료된 상태입니다.

---

## 프로젝트 목적

고정된 **4×4 격자**와 **1~16(각 숫자 한 번)** 위에서,  
**모든 행·열·두 대각선의 합이 같은 배치**를 다루되,

- 그 배치가 규칙을 만족하는지 **일관되게 판정**하고
- 필요할 때만 규칙을 만족하는 배치를 **제시**할 수 있는 기반을 마련하는 것

이 프로젝트의 중심은 “16칸을 맞추는 손맛”이 아니라, **규칙·불변 조건·판정 계약**을 명확히 하는 것입니다.

---

## 현재 상태

| 항목 | 상태 |
|------|------|
| 문제 인식 (STEP 1~5) | 완료 |
| STEP 6 TDD 설계 문서 | 완료 ([Report/02.design.md](Report/02.design.md)) |
| 아키텍처·계약·테스트 설계 | 완료 |
| PRD (구현 전 기준) | 완료 · [07. PRD](Report/07.%20MagicSquare_PRD_Report.md) · [08. PRD 검토](Report/08.%20MagicSquare_PRD_Review_Report.md) |
| 구현·알고리즘 | 미착수 |
| 테스트·소스 코드 | User 엔티티 예제만 존재 |

---

## 진행 단계

| 단계 | 내용 | 상태 |
|------|------|------|
| STEP 1~5 | 문제 인식 · Why chain · Invariant | 완료 |
| STEP 6 | TDD 설계 | 완료 |
| STEP 7 | 구현 | 예정 |

---

## 문제 정의 요약 (STEP 5)

### 개선된 정의 (기준)

> 4×4, 1~16(각 1회) 배치가 **모든 행·열·두 대각선의 합이 동일한지**를 **재현 가능하게 판정**하고, 필요 시에만 그 조건을 만족하는 배치를 **제시**한다. 동일 입력에 대한 판정 결과는 항상 같아야 한다.

| 구분 | 내용 |
|------|------|
| 핵심 능력 1 | **판정** (필수) |
| 핵심 능력 2 | **제시** (선택, 제시물은 반드시 판정 통과) |
| 마법 상수 | 34 (4×4, 1~16) |

---

## 핵심 Invariant

| ID | 내용 |
|----|------|
| I1 | 16개 값 = {1, …, 16} |
| I2 | 네 행·네 열·두 대각선의 합이 모두 동일 |
| I3 | 공통 합 = 34 |
| I4 | “규칙 만족”으로 인정된 배치는 I1~I3 충족 |
| I5 | 동일 입력 → 동일 판정 결과 |
| I6 | (제시 기능 사용 시) 제시 배치는 판정 통과 |
| I7 | 불만족 시 침묵 성공 없음 |

---

## 문서

| 문서 | 설명 |
|------|------|
| [01. MagicSquare_ProblemRecognition_Report.md](Report/01.%20MagicSquare_ProblemRecognition_Report.md) | STEP 1~5 통합 보고서 |
| [01.problem-definition.md](Report/01.problem-definition.md) | 문제 정의 보고서 (원격 spec 이력) |
| [02.design.md](Report/02.design.md) | STEP 6 TDD 설계 문서 |
| [02. MagicSquare_Architecture_Contracts_Report.md](Report/02.%20MagicSquare_Architecture_Contracts_Report.md) | Dual-Track TDD / Clean Architecture 설계·계약 |
| [07. MagicSquare_PRD_Report.md](Report/07.%20MagicSquare_PRD_Report.md) | 구현 전 PRD |
| [08. MagicSquare_PRD_Review_Report.md](Report/08.%20MagicSquare_PRD_Review_Report.md) | PRD 7기준 검토 |

---

## 라이선스 / 기여

미정 (프로젝트 초기 단계)
