# 복원력 있는 UI와 접근성

## 목차

1. UI 상태 설계
2. 오류와 복구
3. semantic HTML
4. form 접근성
5. 비동기 상태 알림
6. focus와 keyboard
7. 점검표
8. 근거 자료

## 1. UI 상태 설계

기능마다 다음 상태 중 실제로 가능한 상태를 명시한다.

- 최초 loading
- background refresh
- empty
- partial data
- success
- validation error
- recoverable request error
- unrecoverable render error
- 권한 없음 또는 인증 만료

하나의 `isLoading`으로 최초 loading과 background refresh를 모두 가리지 않는다. 이미 유용한 데이터가 있으면 보존하고 가까운 곳에 갱신 상태를 표시한다.

### Bad: 전체 콘텐츠 제거

```tsx
if (isFetching) {
  return <FullPageSpinner />;
}
```

### Good: 기존 콘텐츠 보존

```tsx
return (
  <section aria-busy={isFetching}>
    {isFetching && <p className="sr-only">목록 갱신 중</p>}
    <Results items={data} />
  </section>
);
```

최초 데이터가 없다면 구조를 예측할 수 있는 skeleton 또는 구체적인 loading 문구를 사용한다.

## 2. 오류와 복구

오류 메시지는 다음을 포함한다.

- 무엇이 실패했는가?
- 사용자가 지금 할 수 있는 행동은 무엇인가?
- 입력 내용과 기존 성공 데이터가 보존되는가?

### Bad

```tsx
{error && <p>Something went wrong</p>}
```

### Good

```tsx
{error && (
  <div role="alert">
    <p>사용자 목록을 불러오지 못했습니다.</p>
    <button type="button" onClick={retry}>
      다시 시도
    </button>
  </div>
)}
```

모든 오류를 같은 UI로 처리하지 않는다. validation은 field 가까이에, 요청 오류는 작업 영역에, render 오류는 Error Boundary에 둔다.

## 3. semantic HTML

native element를 우선한다. native semantics는 keyboard 동작과 접근성 tree를 함께 제공한다.

### Bad: 마우스만 가능한 가짜 버튼

```tsx
<div onClick={onSave}>저장</div>
```

### Good

```tsx
<button type="button" onClick={onSave}>
  저장
</button>
```

링크 이동에는 `<a>`, form 제출에는 `<button type="submit">`, 제목에는 순서가 맞는 heading, 목록에는 `<ul>/<ol>`, 표 데이터에는 `<table>`을 사용한다.

ARIA는 native semantics가 표현하지 못하는 widget 상태를 보완할 때 사용한다. 잘못된 ARIA로 native semantics를 덮지 않는다.

## 4. form 접근성

모든 control에 programmatic label을 연결한다. placeholder는 label이 아니다.

### Bad

```tsx
<input placeholder="이메일" />
```

### Good

```tsx
function EmailField({ error }: { error?: string }) {
  const inputId = useId();
  const errorId = `${inputId}-error`;

  return (
    <div>
      <label htmlFor={inputId}>이메일</label>
      <input
        id={inputId}
        name="email"
        type="email"
        autoComplete="email"
        aria-invalid={Boolean(error)}
        aria-describedby={error ? errorId : undefined}
      />
      {error && (
        <p id={errorId}>
          {error}
        </p>
      )}
    </div>
  );
}
```

- 반복 가능한 컴포넌트 ID에는 `useId`를 사용한다.
- icon-only button에 `aria-label` 또는 화면에 보이지 않는 텍스트를 제공한다.
- form 안의 비제출 버튼에는 `type="button"`을 명시한다.
- controlled input은 `value`와 동기식 `onChange`를 함께 제공한다.
- checkbox와 radio는 `checked` 및 `e.target.checked`를 사용한다.
- 입력 오류는 색만으로 전달하지 않는다.

## 5. 비동기 상태 알림

- 긴 작업 영역에 `aria-busy`를 사용한다.
- 중요한 비동기 실패는 `role="alert"`로 알리되 반복 render로 같은 메시지를 계속 공지하지 않는다.
- 비긴급 진행 상태는 적절한 live region을 검토한다.
- button text에 구체적인 pending 상태를 보여준다.

```tsx
<button type="submit" disabled={isPending}>
  {isPending ? "초대 보내는 중…" : "초대 보내기"}
</button>
```

`disabled`만 사용하면 왜 동작하지 않는지 모호할 수 있으므로 상태 문구를 함께 제공한다. 작업 취소가 가능해야 한다면 취소 control도 제공한다.

## 6. focus와 keyboard

- 모든 상호작용을 키보드만으로 완료할 수 있게 한다.
- focus indicator를 제거하지 않는다.
- modal, menu, tabs 같은 복합 widget은 WAI-ARIA APG keyboard pattern을 따른다.
- modal을 닫으면 일반적으로 modal을 연 control로 focus를 복귀시킨다.
- 오류 발생 시 무조건 focus를 이동하지 않는다. 제출 실패처럼 사용자가 즉시 수정해야 할 때 오류 요약 또는 첫 오류 field로 이동하는 방식을 검토한다.
- route 변경과 동적 콘텐츠 삽입 후 focus 동작을 실제 keyboard와 screen reader 흐름 기준으로 확인한다.

클릭 가능한 custom widget에 `tabIndex`와 key handler를 뒤늦게 붙이기보다 native element를 사용한다.

## 7. 점검표

- [ ] loading, empty, error, retry, success 상태가 서로 모순되지 않는다.
- [ ] 요청 실패 후 입력과 기존 데이터가 가능한 한 보존된다.
- [ ] 클릭 대상이 적절한 native element다.
- [ ] form control과 icon button에 accessible name이 있다.
- [ ] field 오류가 control에 연결되어 있다.
- [ ] mouse 없이 전체 작업이 가능하다.
- [ ] focus 위치와 indicator가 보인다.
- [ ] 비동기 진행과 실패가 시각 및 보조 기술에 전달된다.
- [ ] heading, landmark, list, table 구조가 콘텐츠 의미와 맞는다.
- [ ] error/loading UI도 정상 UI와 동일하게 테스트한다.

## 8. 근거 자료

- React DOM input: https://react.dev/reference/react-dom/components/input
- React DOM form: https://react.dev/reference/react-dom/components/form
- React DOM common components and ARIA props: https://react.dev/reference/react-dom/components/common
- W3C WAI Accessibility Principles: https://www.w3.org/WAI/fundamentals/accessibility-principles/
- WAI-ARIA Authoring Practices Guide: https://www.w3.org/WAI/ARIA/apg/
