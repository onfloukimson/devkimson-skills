# Daily Reporting

## Purpose

하루 단위 raw work log를 외부 제출 가능한 업무보고로 변환합니다.

**독자:** 일일 보고 본문(`금일`·`명일`)은 기본적으로 **비개발자 경영층(대표)** 가 읽을 전제로 작성한다 (`highworks-reporting.md` **대표 등 비개발자 독자 기준** 참고).

## Inputs

- `ai-workspace/40-tasks/daily/raw/YYYY-MM-DD.md`
- `ai-workspace/40-tasks/checklist.md`
- 관련 산출물, 결정 로그, blocker 기록

## Outputs

- `ai-workspace/40-tasks/daily/reports/YYYY-MM-DD-report.md`
- 복사/붙여넣기용 `Copy/Paste Output`

## Steps

1. raw daily log에서 완료 항목, blocker, follow-up을 확인합니다.
2. 완료 항목을 관련 업무 단위로 묶습니다.
3. 내부 구현 세부사항을 제거하고 업무 가치 중심으로 바꿉니다 (**대표·비개발자 가독성** 규격은 `highworks-reporting.md` 대표 등 비개발자 독자 절).
4. 완료 업무는 `금일`, 다음 계획은 `명일`로 분리합니다. **`명일`은 ` ─  ` 접두 없이 본문 한 덩어리만** 작성합니다 (`highworks-reporting.md`).
5. 불필요한 반복 표현을 제거합니다.
6. 회사별 양식이 있으면 해당 format skill을 적용합니다.
7. Echo 또는 human review 후 외부 제출합니다.

## Output Requirements

- 간결해야 합니다.
- 업무 담당자가 바로 복사/붙여넣기할 수 있어야 합니다.
- 진행률이 필요한 경우 `진행률 70%`처럼 숫자와 `%`를 함께 씁니다 (**하이웍스 `금일` 줄 끝 `(100%)` 형식 제외**, 해당 규격은 `highworks-reporting.md` 참조).
- 불확실한 내용은 단정하지 않습니다.
- 외부에 노출할 필요가 없는 내부 시행착오는 제외합니다.

## Automation Hooks

향후 자동화는 다음 hook을 사용할 수 있습니다.

- raw log parser
- task grouping
- duplicate detection
- report formatter
- clipboard output
- human review status checker
