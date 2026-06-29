---
name: react-engineering
description: Design, implement, review, and refactor reliable React 19 applications and components using correct component boundaries, state ownership, render-time derivation, Effects, asynchronous flows, resilient UI states, accessibility, and behavior-focused tests. Use for React JavaScript or TypeScript feature work, hook and component design, state/effect bugs, data fetching and mutations, forms, loading/error/empty states, accessibility fixes, or React code-quality reviews. Apply project-specific framework, styling, and folder conventions alongside this skill.
---

# React Engineering

React를 렌더링 기반 UI 시스템으로 다룬다. Hook을 먼저 선택하지 말고 데이터 소유권, 사용자 이벤트, 외부 동기화 경계를 먼저 결정한다.

## 작업 절차

1. 저장소의 React 버전, 프레임워크, 데이터 계층, 상태 관리, 린트, 테스트 도구와 기존 관례를 확인한다.
2. 요구사항을 사용자에게 보이는 상태와 전이로 정리한다. 성공 경로뿐 아니라 loading, empty, error, retry, disabled 상태를 포함한다.
3. 각 데이터의 원본을 하나만 정한다. 저장할 상태와 렌더 중 계산할 값을 분리한다.
4. 컴포넌트 경계를 책임과 변경 단위로 정하고 state를 가장 가까운 공통 소유자에 둔다.
5. 로직의 원인을 구분한다.
   - 렌더 때문에 필요한 계산: 컴포넌트 본문
   - 특정 사용자 행동 때문에 실행: event handler 또는 Action
   - 외부 시스템과 계속 동기화: Effect
6. 비동기 요청의 경합, 취소, 중복 제출, 실패 복구를 설계한다.
7. semantic HTML, 키보드 조작, accessible name, focus, 상태 알림을 구현한다.
8. 타입 검사, React Hooks 린트, 행동 테스트, 빌드 순으로 검증한다. 저장소에 있는 명령만 사용하고 결과를 보고한다.

## 구현 불변 조건

- 컴포넌트와 Hook의 render는 순수하게 유지한다. props, state, context, 전역 값을 mutation하지 않는다.
- Hook은 컴포넌트 또는 custom Hook 최상위에서 동일한 순서로 호출한다.
- state는 사용자가 변경하거나 시간에 따라 유지해야 하는 최소 데이터만 저장한다.
- props/state에서 계산 가능한 값은 일반 변수로 계산한다. 계산 비용이 실제로 클 때만 `useMemo`를 사용한다.
- 이전 state에 기반한 갱신은 functional updater를 사용한다.
- 함께 전이하며 모순될 수 있는 상태는 객체, reducer, 또는 명시적 상태 모델로 묶는다.
- 렌더에 필요 없는 mutable 값은 `useRef`에 둔다.
- 리스트 key에는 형제 사이에서 고유하고 데이터 수명 동안 안정적인 ID를 사용한다.
- `memo`, `useMemo`, `useCallback`을 정확성 도구로 사용하지 않는다. 측정된 비용이나 참조 안정성 계약이 있을 때만 사용한다.
- `react-hooks` 린트를 우회하지 않는다. 의존성을 숨기지 말고 코드를 재구성한다.
- 컴포넌트, Hook, `lazy` 선언을 다른 컴포넌트 내부에 중첩하지 않는다.

## Effect 판단 게이트

Effect를 작성하기 전에 순서대로 답한다.

1. 렌더 중 props/state로 계산 가능한가? 일반 변수 또는 필요한 경우 `useMemo`를 사용한다.
2. 특정 클릭, 입력, 제출 때문에 실행되는가? event handler 또는 Action에 둔다.
3. `key`로 subtree를 재설정하거나 state 소유권을 이동하면 해결되는가? Effect 대신 구조를 고친다.
4. React 밖의 시스템과 연결, 구독, 측정, 동기화하는가? cleanup을 포함한 Effect를 사용한다.

Effect 내부의 동기식 `setState`는 원칙적으로 의심한다. 비동기 응답, subscription callback, DOM 측정처럼 렌더 중 알 수 없는 외부 결과를 반영하는 경우는 허용한다. 자세한 판단과 예시는 [effects-and-async.md](references/effects-and-async.md)를 읽는다.

## 컴포넌트와 상태 설계

- 사용자에게 의미 있는 책임, 독립적으로 변경되는 영역, 반복되는 UI, 복잡성을 숨길 필요가 있는 영역을 컴포넌트 후보로 삼는다.
- 줄 수만 줄이기 위한 wrapper 컴포넌트와 props 전달만 반복하는 추상화를 만들지 않는다.
- 공유 state는 필요한 컴포넌트들의 가장 가까운 공통 부모로 올린다. 모든 state를 전역화하지 않는다.
- custom Hook은 stateful 동작을 재사용하지만 호출 간 state를 공유하지 않는다는 점을 지킨다.
- Context는 멀리 떨어진 소비자가 실제로 공유해야 하는 안정적인 의존성에 사용한다. 자주 바뀌는 거대한 객체 하나를 전달하지 않는다.

상태 구조, 경계, identity와 Bad/Good 예시는 [components-and-state.md](references/components-and-state.md)를 읽는다.

## 비동기 UI와 오류 경계

- 요청 상태를 최소한 `idle | pending | success | error`로 구분하고 불가능한 조합을 만들지 않는다.
- 최신 요청만 UI를 갱신하게 하고, 가능하면 `AbortController` 또는 사용 중인 데이터 계층의 취소 기능을 사용한다.
- mutation은 원인이 명확한 event handler 또는 React 19 Action에서 시작한다. state 변경을 감시하는 Effect로 mutation을 유발하지 않는다.
- Error Boundary는 render 오류 경계에 둔다. event handler와 일반 비동기 callback 오류는 직접 처리한다.
- Suspense는 지원되는 framework/data source 또는 `lazy`에 사용한다. Effect 안의 fetch는 자동으로 suspend하지 않는다.
- 이미 보이는 콘텐츠를 전역 spinner로 불필요하게 교체하지 않는다. 경계와 loading UI를 작업 범위에 가깝게 둔다.

React 19 Actions, 요청 취소, 오류 및 loading 상태 예시는 [effects-and-async.md](references/effects-and-async.md)와 [resilient-accessible-ui.md](references/resilient-accessible-ui.md)를 읽는다.

## 접근성 기준

semantic HTML을 우선한다. 클릭 가능한 `div`를 만들고 ARIA로 보수하지 않는다. 모든 입력에 label, 모든 icon button에 accessible name, 모든 상호작용에 키보드 경로, 비동기 변화에 적절한 상태 알림을 제공한다. focus를 강제로 이동할 때는 사용자 작업 흐름상 필요한지 확인한다.

구현 체크와 예시는 [resilient-accessible-ui.md](references/resilient-accessible-ui.md)를 읽는다.

## 테스트와 완료 조건

구현 세부 Hook 호출 횟수보다 사용자가 관찰하는 동작을 검증한다. role과 accessible name으로 요소를 찾고 실제 사용자에 가까운 입력을 발생시킨다. 최소한 핵심 성공 경로와 중요한 loading, error, retry 경로를 테스트한다.

테스트 선택, 예시, 검증 체크리스트는 [testing-and-verification.md](references/testing-and-verification.md)를 읽는다.

## 리뷰 결과 형식

코드 리뷰 요청에는 다음 형식을 사용한다.

1. 위치와 근거
2. 실제 실패 또는 유지보수 위험
3. 최소 수정안
4. 검증 방법

정확성, 데이터 손실, 접근성 차단을 우선하고 단순 취향은 결함으로 보고하지 않는다.
