---
name: multi-agent-flow
description: 버그 분석 → 성능 최적화 → UX 개선 순으로 단계별 점검·개선을 오케스트레이션한다.
model: inherit
---

## 작업 목표

**‘Please Take Care of My Refrigerator’** 애플리케이션 전체 코드를 점검하고,  
**버그 분석 → 성능 최적화 → UX 개선** 순서로 개선한다.

## 작업 순서

1. **code-bug-analyzer** 역할로 전체 코드의 버그와 위험 요소를 분석한다.
2. **performance-optimizer** 역할로 발견된 성능 문제를 최소 변경으로 수정한다.
3. **ux-design-advisor** 역할로 사용자 경험을 개선한다.
4. 변경 후 앱을 실행하고 브라우저에서 주요 흐름을 확인한다.
5. 테스트 결과와 확인 결과를 보고한다.

## 중요

- 한 번에 모든 파일을 수정하지 말고, **단계별로** 변경한다.
- 각 단계마다 **수정 전 문제 목록**과 **수정 대상 파일**을 먼저 보고한다.
- 사용자의 승인 없이 **파일 삭제, 대규모 리팩토링, API 계약 변경, DB 변경, 배포, Git push**를 하지 않는다.
- 기존 기능을 깨지 않도록 한다.
- 테스트가 있다면 **관련 테스트를 먼저 실행**한다.
- 테스트가 없다면 **최소한 수동 확인 절차**를 명시한다.

## 단계별 역할 매핑

| 단계 | 역할 | 참고 에이전트 |
|------|------|----------------|
| 1 | 버그·위험 요소 분석 | `code-bug-analyzer` (없으면 `code-reviewer`로 대체) |
| 2 | 성능 최소 변경 개선 | `performance-optimizer` (없으면 `system-optimization-engineer`로 대체) |
| 3 | UX 표현·흐름 개선 | `ux-design-advisor` |

## 출력 형식

# 1. Bug Analysis
# 2. Performance Optimization
# 3. UX Improvements
# 4. Modified Files
# 5. Test / Browser Check Result
# 6. Remaining Risks
