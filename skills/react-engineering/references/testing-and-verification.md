# 테스트와 검증

## 목차

1. 테스트 전략
2. 요소 선택과 상호작용
3. 비동기 테스트
4. Effect와 cleanup 테스트
5. 피해야 할 테스트
6. 완료 검증
7. 근거 자료

## 1. 테스트 전략

구현 세부가 아니라 공개 동작을 테스트한다.

우선순위:

1. 사용자가 완료해야 하는 핵심 작업
2. 데이터 손실이나 중복 mutation을 만들 수 있는 경로
3. loading, empty, error, retry와 validation
4. keyboard와 accessible name
5. 재발 가능성이 있는 버그

작은 순수 계산은 unit test로, 컴포넌트 상호작용은 DOM 기반 component test로, route와 실제 network 경계는 필요한 범위의 integration 또는 end-to-end test로 검증한다.

## 2. 요소 선택과 상호작용

사용자가 인식하는 role과 name을 우선한다. Testing Library를 사용한다면 `getByRole`, `getByLabelText`를 우선하고 `data-testid`는 의미 있는 query가 불가능할 때만 사용한다.

### Bad: 구현 구조에 결합

```tsx
const button = container.querySelector(".primary-button");
fireEvent.click(button);
expect(mockSetState).toHaveBeenCalled();
```

### Good: 사용자 결과 검증

```tsx
it("수량을 증가시킨다", async () => {
  const user = userEvent.setup();
  render(<Counter />);

  await user.click(screen.getByRole("button", { name: "수량 증가" }));

  expect(screen.getByText("수량: 2")).toBeVisible();
});
```

`userEvent`는 click, type, tab처럼 실제 상호작용에 가까운 event 묶음을 발생시킨다. 낮은 수준의 단일 event가 필요한 특수 상황에만 `fireEvent`를 사용한다.

## 3. 비동기 테스트

요청의 pending, success, failure를 제어 가능한 mock으로 테스트한다. 단순히 Promise를 임의 시간만큼 기다리지 않는다.

```tsx
it("실패 후 다시 시도해 목록을 표시한다", async () => {
  const user = userEvent.setup();
  server.use(
    http.get("/api/users", () =>
      HttpResponse.json(
        { message: "failed" },
        { status: 500 },
      ),
    ),
  );

  render(<UsersPage />);

  expect(
    await screen.findByRole("alert"),
  ).toHaveTextContent("사용자 목록을 불러오지 못했습니다.");

  server.use(
    http.get("/api/users", () =>
      HttpResponse.json([{ id: "1", name: "Kim" }]),
    ),
  );

  await user.click(screen.getByRole("button", { name: "다시 시도" }));

  expect(await screen.findByText("Kim")).toBeVisible();
});
```

- 비동기 등장에는 `findBy*`를 사용한다.
- 사라짐에는 `waitForElementToBeRemoved`를 검토한다.
- `waitFor` callback에는 최종 assertion을 넣고 임의 delay를 넣지 않는다.
- 실제 fetch 계약과 상태 코드를 가능한 한 network boundary에서 mock한다.
- 빠른 연속 요청을 만들어 이전 응답이 최신 결과를 덮지 않는지 검증한다.

## 4. Effect와 cleanup 테스트

외부 subscription Effect는 mount 시 subscribe, dependency 변경 시 resubscribe, unmount 시 cleanup되는 동작을 검증한다. StrictMode에서도 중복 listener가 남지 않아야 한다.

```tsx
it("room 변경과 unmount에 맞춰 연결을 정리한다", () => {
  const { rerender, unmount } = render(<ChatRoom roomId="general" />);

  expect(connect).toHaveBeenCalledWith("general");

  rerender(<ChatRoom roomId="support" />);
  expect(disconnect).toHaveBeenCalledWith("general");
  expect(connect).toHaveBeenCalledWith("support");

  unmount();
  expect(disconnect).toHaveBeenCalledWith("support");
});
```

가능하면 mock 함수 호출 자체보다 외부에서 관찰 가능한 subscription 결과를 검증한다. fake timer를 사용하면 각 테스트에서 원복한다.

React 상태 갱신을 직접 테스트할 때는 async `act`를 사용한다. React Testing Library의 render와 user-event helper는 일반적으로 `act` 처리를 제공하므로 중복으로 감싸지 않는다.

## 5. 피해야 할 테스트

- Hook 호출 순서나 `useState` setter 자체를 mock하는 테스트
- private 함수와 내부 state를 직접 검사하는 테스트
- snapshot 하나로 상호작용과 접근성을 모두 검증했다고 간주하는 테스트
- 모든 child를 mock해 실제 조합이 사라진 테스트
- timeout과 임의 sleep으로 우연히 통과하는 테스트
- 테스트를 통과시키기 위해 `act` warning을 숨기는 설정

### Bad: 구현을 고정

```tsx
expect(useMemo).toHaveBeenCalledTimes(1);
```

### Good: 계약을 검증

```tsx
expect(
  screen.getAllByRole("listitem").map(row => row.textContent),
).toEqual(["Alpha", "Beta"]);
```

## 6. 완료 검증

저장소에서 제공하는 명령을 먼저 확인하고 변경 범위에 맞춰 실행한다.

1. 관련 test 또는 가장 좁은 test suite
2. 전체 typecheck
3. lint와 `eslint-plugin-react-hooks`
4. 영향 범위가 넓다면 전체 test
5. production build
6. 접근성 자동 검사와 핵심 흐름의 수동 keyboard 확인

완료 전에 다음을 검색한다.

- 새 `eslint-disable` 또는 `@ts-ignore`
- cleanup 없는 subscription, timer, listener
- index/random key
- Effect 안의 동기식 파생 state
- 처리하지 않은 Promise rejection
- label 없는 form control과 name 없는 icon button
- 테스트되지 않은 error/retry 경로

실행하지 못한 검증은 통과한 것처럼 말하지 말고 명령과 이유를 명시한다.

## 7. 근거 자료

- React `act`: https://react.dev/reference/react/act
- React StrictMode: https://react.dev/reference/react/StrictMode
- React Hooks ESLint plugin: https://react.dev/reference/eslint-plugin-react-hooks
- React Testing Library: https://testing-library.com/docs/react-testing-library/intro/
- Testing Library user-event: https://testing-library.com/docs/user-event/intro/
- Testing Library query priority: https://testing-library.com/docs/queries/about/#priority
