# 컴포넌트 경계와 상태 설계

## 목차

1. 컴포넌트 경계
2. 상태 배치
3. 상태 구조
4. 파생 값
5. identity와 key
6. custom Hook과 Context
7. 근거 자료

## 1. 컴포넌트 경계

다음 중 하나 이상에 해당할 때 분리한다.

- 사용자 관점의 독립된 영역 또는 행동이다.
- 부모와 다른 이유와 빈도로 변경된다.
- 반복되는 UI와 동작을 하나의 계약으로 재사용한다.
- 복잡한 구현을 작고 명확한 props API 뒤에 숨긴다.
- 독립적인 오류, loading, Suspense 경계가 필요하다.

컴포넌트 크기나 JSX 줄 수만으로 분리하지 않는다.

### Bad: 책임이 섞인 거대 컴포넌트

```tsx
function ProductPage({ productId }: { productId: string }) {
  // 상품 조회, 장바구니 mutation, 리뷰 form, modal, toast를 모두 소유한다.
  // 서로 무관한 변경도 전체 파일과 상태를 건드린다.
  return <main>{/* 수백 줄의 UI */}</main>;
}
```

### Good: 사용자 책임과 변경 단위로 분리

```tsx
function ProductPage({ productId }: { productId: string }) {
  return (
    <main>
      <ProductSummary productId={productId} />
      <AddToCart productId={productId} />
      <ReviewSection productId={productId} />
    </main>
  );
}
```

단, `ProductSummaryTitle`, `ProductSummaryPriceWrapper`처럼 의미 없는 한 줄 wrapper를 기계적으로 만들지 않는다.

## 2. 상태 배치

각 state마다 다음을 확인한다.

1. 누가 변경하는가?
2. 누가 읽는가?
3. 가장 가까운 공통 소유자는 어디인가?
4. URL, server cache, form library 등 이미 원본이 존재하는가?

state는 필요한 곳에 최대한 가깝게 둔다. 형제들이 같은 값을 조정해야 할 때만 공통 부모로 올린다.

### Bad: 같은 선택을 두 곳에 복제

```tsx
function LeftPanel() {
  const [selectedId, setSelectedId] = useState<string | null>(null);
  // ...
}

function DetailPanel() {
  const [selectedId, setSelectedId] = useState<string | null>(null);
  // 서로 어긋날 수 있다.
}
```

### Good: 단일 소유자

```tsx
function Workspace() {
  const [selectedId, setSelectedId] = useState<string | null>(null);

  return (
    <>
      <ItemList selectedId={selectedId} onSelect={setSelectedId} />
      <ItemDetail itemId={selectedId} />
    </>
  );
}
```

## 3. 상태 구조

- 항상 같이 바뀌는 값은 한 구조 또는 reducer로 묶는다.
- 서로 모순되는 boolean 조합을 만들지 않는다.
- 객체 전체 대신 안정적인 ID를 저장한다.
- 깊은 중첩과 중복을 줄인다.
- props를 state로 복사하지 않는다. 사용자가 편집하는 draft처럼 의도적으로 분리된 경우에만 초기값으로 사용한다.

### Bad: 불가능한 요청 상태

```tsx
const [isLoading, setIsLoading] = useState(false);
const [hasError, setHasError] = useState(false);
const [data, setData] = useState<User[] | null>(null);
// isLoading && hasError 같은 모순이 가능하다.
```

### Good: 전이를 표현하는 상태

```tsx
type UsersState =
  | { status: "idle" }
  | { status: "pending" }
  | { status: "success"; data: User[] }
  | { status: "error"; error: Error };

const [users, setUsers] = useState<UsersState>({ status: "idle" });
```

### Bad: props를 무조건 복사

```tsx
function Profile({ user }: { user: User }) {
  const [name, setName] = useState(user.name);
  // user가 바뀌어도 자동으로 동기화되지 않는다.
}
```

### Good: 표시만 한다면 props 사용

```tsx
function Profile({ user }: { user: User }) {
  return <p>{user.name}</p>;
}
```

편집 draft가 필요하다면 경계를 명시한다.

```tsx
function ProfileEditor({ user, onSave }: Props) {
  const [draftName, setDraftName] = useState(() => user.name);
  // 부모는 user.id를 key로 사용해 다른 사용자로 전환할 때 draft를 재설정한다.
}

<ProfileEditor key={user.id} user={user} onSave={saveUser} />;
```

## 4. 파생 값

props와 state에서 결정적으로 계산되는 값은 state가 아니다.

### Bad: Effect로 파생 값을 복제

```tsx
const [fullName, setFullName] = useState("");

useEffect(() => {
  setFullName(`${firstName} ${lastName}`);
}, [firstName, lastName]);
```

### Good: 렌더 중 계산

```tsx
const fullName = `${firstName} ${lastName}`;
```

### Bad: 정렬 결과를 state에 저장하고 원본도 mutation

```tsx
useEffect(() => {
  setSorted(items.sort(compareByName));
}, [items]);
```

### Good: 원본을 보존하며 계산

```tsx
const sorted = useMemo(
  () => [...items].sort(compareByName),
  [items],
);
```

`useMemo`는 계산이 실제로 비싸거나 안정적인 참조가 하위 memoization 계약에 필요할 때만 사용한다. 일반적인 문자열 조합, 작은 배열 변환에는 일반 변수가 더 명확하다.

## 5. identity와 key

React는 tree의 같은 위치에 같은 컴포넌트가 있으면 state를 보존한다. 다른 entity의 local state를 재설정하려면 의도적으로 stable entity ID를 `key`로 사용한다.

### Bad: 순서가 변하는 리스트의 index key

```tsx
items.map((item, index) => (
  <EditableRow key={index} item={item} />
));
```

정렬 또는 삽입 시 다른 item의 local state가 행에 붙을 수 있다.

### Good

```tsx
items.map(item => (
  <EditableRow key={item.id} item={item} />
));
```

`Math.random()`이나 렌더마다 바뀌는 값을 key로 만들지 않는다. 매번 remount되어 focus와 local state가 사라진다.

## 6. custom Hook과 Context

custom Hook은 관련 Effect와 state 전이를 캡슐화한다. 두 호출은 로직만 재사용하고 state는 각각 소유한다.

### Bad: Hook 이름이지만 단순 계산만 숨김

```tsx
function useFullName(first: string, last: string) {
  return `${first} ${last}`;
}
```

### Good: 상태를 가진 외부 구독 캡슐화

```tsx
function useOnlineStatus() {
  return useSyncExternalStore(
    subscribeToOnlineStatus,
    getOnlineStatus,
    () => true,
  );
}
```

Context는 theme, 인증 세션, locale처럼 멀리 떨어진 소비자가 공유하는 의존성에 적합하다. 페이지의 모든 state를 하나의 Context 객체에 넣지 않는다. 변경 빈도와 책임이 다르면 Context를 분리하고 provider value의 identity를 의식한다.

## 7. 근거 자료

- React, Thinking in React: https://react.dev/learn/thinking-in-react
- React, Choosing the State Structure: https://react.dev/learn/choosing-the-state-structure
- React, Sharing State Between Components: https://react.dev/learn/sharing-state-between-components
- React, Preserving and Resetting State: https://react.dev/learn/preserving-and-resetting-state
- React, Rules of Hooks lint: https://react.dev/reference/eslint-plugin-react-hooks/lints/rules-of-hooks
