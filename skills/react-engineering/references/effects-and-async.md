# Effect와 비동기 처리

## 목차

1. Effect의 목적
2. Effect 내부 setState
3. 이벤트와 Effect
4. 외부 시스템 동기화
5. 데이터 조회와 경합
6. mutation과 React 19 Actions
7. Suspense와 Error Boundary
8. 근거 자료

## 1. Effect의 목적

Effect를 React 외부 시스템과 동기화하는 escape hatch로 사용한다. 외부 시스템에는 network, WebSocket, timer, browser API, DOM widget, subscription이 포함된다.

다음은 Effect가 아니다.

- JSX에 사용할 배열의 filter, sort, map
- props를 조합한 문자열이나 객체
- 클릭이나 submit 한 번 때문에 발생하는 요청
- 다른 state가 바뀌었다는 이유로 복제 state 갱신

## 2. Effect 내부 setState

금지 대상은 모든 `setState`가 아니라 Effect가 실행되자마자 렌더에서 계산 가능한 값을 동기식으로 다시 저장하는 패턴이다.

### Bad: 불필요한 두 번째 render

```tsx
const [visibleItems, setVisibleItems] = useState<Item[]>([]);

useEffect(() => {
  setVisibleItems(items.filter(item => item.active));
}, [items]);
```

`items` 변경 후 첫 render와 commit이 끝나야 Effect가 실행되고, `setVisibleItems`가 다시 render를 일으킨다.

### Good: 계산 가능한 것은 계산

```tsx
const visibleItems = items.filter(item => item.active);
```

계산 비용이 측정상 크다면 다음을 고려한다.

```tsx
const visibleItems = useMemo(
  () => items.filter(item => item.active),
  [items],
);
```

### Valid: 외부 비동기 결과 반영

```tsx
useEffect(() => {
  let ignore = false;

  fetchUsers().then(users => {
    if (!ignore) {
      setUsers(users);
    }
  });

  return () => {
    ignore = true;
  };
}, []);
```

비동기 callback의 결과는 render 중 계산할 수 없다. 가능하면 아래 AbortController 패턴이나 프로젝트의 data-fetching 계층을 사용한다.

### Valid: DOM 측정

```tsx
useLayoutEffect(() => {
  const nextHeight = ref.current?.getBoundingClientRect().height ?? 0;
  setHeight(nextHeight);
}, []);
```

paint 전에 측정값이 반드시 필요할 때만 `useLayoutEffect`를 사용한다. 그렇지 않으면 `useEffect` 또는 CSS로 해결한다. 크기가 계속 바뀌면 `ResizeObserver`를 구독하고 cleanup한다.

## 3. 이벤트와 Effect

코드가 왜 실행되어야 하는지로 위치를 결정한다.

### Bad: state를 감시해 주문 전송

```tsx
useEffect(() => {
  if (submittedOrder) {
    postOrder(submittedOrder);
  }
}, [submittedOrder]);
```

복원된 state, remount, 의존성 변경이 의도치 않은 재전송을 만들 수 있다.

### Good: 원인이 되는 사용자 이벤트에서 실행

```tsx
async function handleSubmit(order: Order) {
  await postOrder(order);
  setConfirmation("주문이 완료되었습니다.");
}
```

반대로 화면에 해당 room이 보이는 동안 연결이 유지되어야 한다면 Effect가 맞다.

```tsx
useEffect(() => {
  const connection = createConnection(roomId);
  connection.connect();

  return () => connection.disconnect();
}, [roomId]);
```

## 4. 외부 시스템 동기화

모든 Effect는 독립적인 synchronization process로 작성한다.

- setup과 cleanup을 대칭으로 만든다.
- 읽는 reactive value를 dependency에 모두 포함한다.
- dependency lint를 끄지 않는다.
- 서로 다른 외부 책임을 하나의 Effect에 섞지 않는다.
- StrictMode의 개발용 setup → cleanup → setup 순서에서도 올바르게 동작하게 만든다.

### Bad: stale closure를 숨김

```tsx
useEffect(() => {
  const id = window.setInterval(() => {
    setCount(count + step);
  }, 1000);

  return () => window.clearInterval(id);
  // eslint-disable-next-line react-hooks/exhaustive-deps
}, []);
```

### Good: 필요한 반응성을 명시

```tsx
useEffect(() => {
  const id = window.setInterval(() => {
    setCount(current => current + step);
  }, 1000);

  return () => window.clearInterval(id);
}, [step]);
```

Effect 안 일부 로직만 최신 값을 읽되 그 값에 반응하지 않아야 하고 React 버전이 지원한다면 `useEffectEvent`를 검토한다. Effect Event는 해당 Effect 근처에서 선언하고 Effect 안에서만 호출한다.

## 5. 데이터 조회와 경합

framework loader, router loader, server component, query/cache library가 이미 있으면 그것을 우선한다. 직접 Effect로 조회하면 cache, SSR, deduplication, waterfall, race condition을 직접 책임져야 한다.

직접 조회가 필요한 경우 최소한 취소와 모든 UI 상태를 구현한다.

```tsx
type UserState =
  | { status: "pending"; requestId: string }
  | { status: "success"; requestId: string; user: User }
  | { status: "error"; requestId: string; error: Error };

function UserProfile({ userId }: { userId: string }) {
  const [settledState, setSettledState] = useState<UserState>({
    status: "pending",
    requestId: userId,
  });

  const state: UserState =
    settledState.requestId === userId
      ? settledState
      : { status: "pending", requestId: userId };

  useEffect(() => {
    const controller = new AbortController();
    let ignore = false;

    getUser(userId, { signal: controller.signal })
      .then(user => {
        if (!ignore) {
          setSettledState({ status: "success", requestId: userId, user });
        }
      })
      .catch(error => {
        if (error instanceof DOMException && error.name === "AbortError") return;
        if (!ignore) {
          setSettledState({
            status: "error",
            requestId: userId,
            error: error instanceof Error ? error : new Error("Unknown error"),
          });
        }
      });

    return () => {
      ignore = true;
      controller.abort();
    };
  }, [userId]);

  if (state.status === "pending") return <UserSkeleton />;
  if (state.status === "error") return <ErrorMessage error={state.error} />;
  return <Profile user={state.user} />;
}
```

`userId`가 바뀌면 이전 요청을 취소해 늦게 도착한 이전 응답이 최신 화면을 덮지 않게 한다.

## 6. mutation과 React 19 Actions

mutation은 event handler에서 시작하고 pending 동안 중복 제출을 제어하며 실패를 사용자에게 보여준다.

### 기본 event handler

```tsx
async function handleSave() {
  if (status === "pending") return;
  setStatus("pending");

  try {
    await saveProfile(draft);
    setStatus("success");
  } catch (error) {
    setStatus("error");
  }
}
```

프로젝트가 React 19 Action 패턴을 사용하면 `useActionState`, form `action`, `useOptimistic`을 활용할 수 있다.

```tsx
type SaveState = { error: string | null };

async function saveAction(
  _previous: SaveState,
  formData: FormData,
): Promise<SaveState> {
  try {
    await saveProfile({ name: String(formData.get("name") ?? "") });
    return { error: null };
  } catch {
    return { error: "저장하지 못했습니다. 다시 시도해 주세요." };
  }
}

function ProfileForm() {
  const [state, submitAction, isPending] = useActionState(
    saveAction,
    { error: null },
  );

  return (
    <form action={submitAction} aria-busy={isPending}>
      <label>
        이름
        <input name="name" />
      </label>
      <button type="submit" disabled={isPending}>
        {isPending ? "저장 중…" : "저장"}
      </button>
      {state.error && <p role="alert">{state.error}</p>}
    </form>
  );
}
```

Actions를 기존 router/form/data library와 중복 도입하지 않는다. optimistic update는 실패 시 원래 값으로 복구되어도 사용자가 혼란스럽지 않고 충돌 정책이 명확한 작업에만 사용한다.

## 7. Suspense와 Error Boundary

- `lazy`로 불러온 code와 Suspense 지원 data source에 `<Suspense fallback>`을 사용한다.
- Effect나 event handler 안의 fetch는 Suspense가 감지하지 않는다.
- render 중 child가 던진 오류는 try/catch가 아니라 Error Boundary가 처리한다.
- event handler와 일반 Promise callback 오류는 Error Boundary가 자동으로 처리하지 않으므로 직접 catch한다.
- 경계를 route 또는 독립적으로 복구 가능한 feature 가까이에 둔다.

```tsx
const Report = lazy(() => import("./Report"));

function ReportRoute() {
  return (
    <ErrorBoundary fallback={<ReportError />}>
      <Suspense fallback={<ReportSkeleton />}>
        <Report />
      </Suspense>
    </ErrorBoundary>
  );
}
```

`lazy` 선언은 컴포넌트 바깥 module scope에 둔다. 내부에 선언하면 render마다 새로운 컴포넌트 identity가 생겨 state가 재설정된다.

## 8. 근거 자료

- React, You Might Not Need an Effect: https://react.dev/learn/you-might-not-need-an-effect
- React, Separating Events from Effects: https://react.dev/learn/separating-events-from-effects
- React, Synchronizing with Effects: https://react.dev/learn/synchronizing-with-effects
- React, useEffect: https://react.dev/reference/react/useEffect
- React, set-state-in-effect lint: https://react.dev/reference/eslint-plugin-react-hooks/lints/set-state-in-effect
- React, useLayoutEffect: https://react.dev/reference/react/useLayoutEffect
- React, Suspense: https://react.dev/reference/react/Suspense
- React, lazy: https://react.dev/reference/react/lazy
- React, useActionState: https://react.dev/reference/react/useActionState
- React, useOptimistic: https://react.dev/reference/react/useOptimistic
- React, Error Boundary guidance: https://react.dev/reference/react/Component#catching-rendering-errors-with-an-error-boundary
