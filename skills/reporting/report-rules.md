# Report Rules

## Executive-Friendly Daily Report Rule

Daily reports may be read by a non-developer executive. Write for business understanding first.

- Each `금일` and `명일` bullet should usually be 50-90 Korean characters, excluding the leading dash. Shorter lines must add real context such as service, schedule, target, or verification scope.
- Avoid overly long bullets. If one line needs more than about 100 characters, split or summarize it.
- Do not expose low-level implementation names unless they are the business-facing issue name. Prefer "관리 화면 보안 취약 버전 개선" over package, mapper, SQL, class, or property names.
- Mention business outcome, affected service, deployment or verification state, and next action.
- Keep `금일` and `명일` separated. `금일` is completed or materially progressed work; `명일` is planned work only.
- `금일` and `명일` use different list formats. `금일` uses `서비스명 업무영역 ─  내용 (100%)`; `명일` does not use the `서비스명 ─` prefix and contains only the planned action sentence.
- Human review is required before external submission.

## 대표 등 비개발자 독자 — 일일 보고 기본

하이웍스 형식이나 동일 채널의 **외부형 일일 보고**는 **대표·비개발 경영층**이 읽을 것을 전제한다.

- **`금일`과 `명일` 모두** 기술·구현 내부만 아는 줄로 끝내지 않는다.
- Mapper·패키지·테스트 속어·파이프라인 코드 같은 표현 대신 서비스·사용자·운영 결과를 말한다.
- 규격·예외·예시 피해야 할 패턴은 `highworks-reporting.md`의 **대표 등 비개발자 독자 기준** 절을 따른다.

## Korean Business Reporting Style

- 문장은 짧고 명확하게 씁니다.
- 존댓말 문장보다 명사형 업무보고 문장을 우선합니다.
- **일일 보고 한 줄 종결은 `~한다`, `~함` 같은 서술형보다 업무 상태·동작 명사**(예: 배포, 검증, 검수, 확인, 점검, 반영, 정리, 검토)**로 마무리**합니다 (`highworks-reporting.md`의 어조 절 참고).
- 내부 사고 과정이나 시행착오는 제외합니다.
- 완료 업무는 산출물, 검토, 반영, 정리, 개선 같은 업무 동사로 표현합니다.
- 불확실한 결과는 완료로 쓰지 않습니다.

## Progress Percentage Notation

- 진행률이 필요할 때만 사용합니다.
- 형식은 `진행률 70%`처럼 작성합니다.
- 추정치라면 `진행률 약 70%`로 표시합니다.
- 완료된 작업은 보통 `100%` 대신 완료 문장으로 씁니다.

### Highworks 일일 보고 예외 (`금일` / `명일`)

- **`금일`**: 각 줄 **끝**에 회사 형식대로 진행도 괄호를 붙인다. **기본값은 `(100%)`** (완료 보고 시). 진행 중·부분 완료는 실측에 맞게 수정한다.
- **`명일`**: **`(NN%)` 등 진행도 표기를 쓰지 않는다.** **`금일`과 같은 `… ─  …` 카테고리 접두는 두지 않고** 계획 본문만 한 줄에 작성한다 (`highworks-reporting.md`).

## Concise Wording

- 한 항목은 가능하면 한 줄로 작성합니다.
- 같은 단어가 반복되면 병합합니다.
- "작업 진행", "확인 진행" 같은 빈 표현은 구체화합니다.
- 외부 독자가 몰라도 되는 파일명, 명령어, 내부 tool 이름은 제외합니다.

## Business-Oriented Summaries

좋은 표현:

- 업무보고 생성 체계 설계 및 템플릿 정리
- 에이전트별 역할과 검토 흐름 문서화
- 보고서 제출 전 검토 기준 수립

피할 표현:

- `mkdir`로 폴더 생성
- markdown 파일 patch 적용
- 내부 diff 확인

## Redundant Technical Details

제외 대상:

- 세부 명령어
- 임시 파일명
- 내부 구현 순서
- 실패했다가 바로 해결한 시행착오
- 외부 공유 가치가 낮은 tool 출력

## Completed Work vs Next-Day Plans

`금일`:

- 완료한 일
- 의미 있게 진전된 일
- 검토 완료된 산출물

`명일`:

- 다음 날 할 일
- 이어서 검증할 일
- 리뷰 또는 보완 예정 업무

## Highworks `명일` 항목 길이·정렬 (필수)

- **최소 길이:** `명일`의 각 할 일 줄은 **공백 포함 최소 50자** 이상으로 작성한다. 목적·대상 시스템·검증 또는 산출 기대를 한 줄 안에 담는다.
- **길이 보완:** 한 줄이 50자에 못 미치면 **내용 허브만 덧붙이지 말고** 대상·일정 창구·점검 항목·선행 조건 등 **실제 보고 대상 정보**를 보강하여 50자 이상으로 맞춘다 (`highworks-reporting.md`).
- **정렬:** 업무 성격이 같은 항목은 **본문 순서만** 조정해 **인접** 나열한다. **`명일`에는 `달달영어 ─  본문` 같은 접두 카테고리 줄을 만들지 않는다** (`highworks-reporting.md` **명일 접두 금지** 참고).
- **`금일`·`명일` 어조:** `highworks-reporting.md`의 **동작·상태 명사형 종결** 규칙을 동일하게 적용한다 (`명일`의 최소 길이 규칙과 병행).

## Human Review

외부 제출 전 반드시 사람이 검토합니다.

검토 기준:

- **비개발자 독자(대표) 기준 가독성:** `금일`·`명일` 줄에 Mapper·패키지·속성 이름·테스트 속어 같은 내부 구현어만 있지 않은가 (`highworks-reporting.md` 대표 등 비개발자 독자 절).
- 회사 양식과 맞는가 (`금일` 줄 끝 `(100%)` 기본 포함 여부 포함)
- `명일`에 퍼센트 표기가 끼어들지 않았는가
- `명일` 각 줄에 `금일`식 **`서비스 범주 ─  ` 접두**(또는 이에 해당하는 카테고리·분리 대시 패턴)가 없고 **내용 한 덩어리만** 있는가 (`highworks-reporting.md`).
- `명일` 각 줄 **최소 50자** 충족·부족 시 맥락 보완(억지 장문 아님) 여부
- **`~한다`·`~함` 등 서술형 종결 없이 업무 상태·동작 명사형으로 끝났는가** (`금일`·`명일`)
- 불필요한 내부 정보가 없는가
- 중복 항목이 없는가
- 실제 완료 상태와 표현이 일치하는가
- 복사/붙여넣기 출력만으로 충분한가
