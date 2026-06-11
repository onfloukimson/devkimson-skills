# Reporting Workflow Skill

Raw daily work logs를 외부 커뮤니케이션용 business report로 변환하는 재사용 workflow입니다.

이 스킬은 markdown-first로 동작해야 하며, 자동화 스크립트가 없어도 사용할 수 있어야 합니다.

## 목적

- 내부 작업 기록과 외부 보고서를 분리합니다.
- 완료 업무를 business-readable 문장으로 요약합니다.
- **외부 채널 일일 보고**(`금일`·`명일`)는 비개발자 경영층(대표) 독자를 기본값으로 두고 작성합니다 (`highworks-reporting.md` **대표 등 비개발자 독자 기준** 참고). **`명일`은 ` ─  ` 접두 없이** 계획 본문만 둡니다 (`highworks-reporting.md`).
- 회사별 보고 양식을 재사용 가능하게 유지합니다.
- 복사/붙여넣기 최적화 출력을 만듭니다.
- 향후 자동 보고 생성, 요약, 중복 탐지, clipboard hook을 붙일 수 있게 준비합니다.

## 기본 입력

- `ai-workspace/40-tasks/daily/raw/YYYY-MM-DD.md`
- 관련 task/checklist
- 관련 artifact/log

## 기본 출력

- `ai-workspace/40-tasks/daily/reports/YYYY-MM-DD-report.md`
- 필요 시 `ai-workspace/40-tasks/daily/summaries/YYYY-MM-summary.md`

## Workflow

```txt
raw daily logs
-> task grouping
-> business formatting
-> report generation
-> review
-> copy/paste output
```

## Human Review

외부 제출 전 human review는 필수입니다.

Echo는 가능하면 보고서의 문장, 중복, 일관성, 가독성을 검토합니다.
