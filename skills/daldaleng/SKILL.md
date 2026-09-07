---
name: daldaleng
description: 달달영어의 API, 백오피스, 배치, 프론트엔드 개발과 이슈 대응을 돕는 인수인계 지식 스킬. 현재 소스와 Git 변경 이력, Dooray 정책·운영 근거를 연결해 학습·시간표·완강·리포트·랭킹·LMS·질문노트 문제를 추적하고 코드나 조회 SQL을 검토한다.
---

# 달달영어 개발 지식

달달영어 담당자의 인수인계 공백을 메우는 근거 중심 작업 지침이다. 이 스킬은 2026-09-07 소스와 Dooray 조사 결과를 출발점으로 사용한다. **현재 체크아웃, 미커밋 변경, 배포본, 운영 데이터는 서로 다르다.** 저장된 설명만으로 현재 운영을 확정하지 않는다.

## 작업 시작

1. 사용자 증상·기간·학생 유형(B2B/B2C)·화면/API를 기준으로 아래 문서를 선택한다. 모든 문서를 한 번에 읽지 않는다.
2. [저장소](references/repositories.md)에서 실제 경로를 확인하고 해당 저장소의 branch/HEAD/status를 읽는다. 사용자가 수정 중인 파일을 보존한다.
3. 화면 → frontend service → Controller → Service → Mapper → 테이블 → batch/BO 영향을 연결한다. [코드 지도](references/code-map.md)와 검색 스크립트로 심볼을 찾고, 관련 본문을 읽는다.
4. 정책 또는 장애 원인이 관련되면 [Dooray 조회](references/dooray.md)를 따라 티켓 본문과 최신 댓글을 확인한다. 커밋 제목은 탐색 단서이며 변경 근거는 diff와 호출부다.
5. 답변에는 결론, 근거 경로/심볼·티켓, 확인한 범위와 남은 불확실성을 포함한다. 코드·테스트 확인과 운영 검증을 구분한다. 작은 작업에 전체 시스템 조사나 고정된 보고서 형식을 강요하지 않는다.

## 업무별 참고

| 요청 | 읽을 문서 |
|---|---|
| 전체 구조·연관 저장소·데이터 식별자 | [아키텍처](references/architecture.md), [데이터 모델](references/domain-model.md) |
| API 인증·회원·적립·외부 연동 | [API](references/api.md), [외부 서비스/배포 이력](references/external-systems.md) |
| 시간표 변경·진도·쌍둥이·완강·재학습 | [학습과 시간표](references/schedule-learning.md) |
| 신규 콘텐츠 평균·DB 이벤트·쌍둥이 이력 | [#198 콘텐츠/평균](references/content-averages.md) |
| 리포트 누락·평균·랭킹·월 경계 | [리포트/랭킹](references/reports-ranking.md), [#183](references/ticket-183-ranking.md) |
| LMS today/weekly/monthly | [#174 계약](references/ticket-174-lms-api.md) |
| 질문노트·첨부·답변·캡처 연계 | [노트/파일](references/notes-files.md) |
| BO 콘텐츠·공통 시간표·회원 표시 | [백오피스](references/backoffice.md) |
| 화면·상태·요청·뷰어 메시지 | [프론트엔드](references/frontend.md) |
| 배치 시간·수동 실행·배포 영향 | [배치 운영](references/batch-operations.md) |
| 조회 SQL·완강자 추출 | [SQL 설명과 예제](references/sql-checks.md) |
| 과거 이유·운영 결정 | [변경 이력](references/history.md), [정책 변경/미결](references/policy-watch.md), [Dooray](references/dooray.md) |
| 증상에서 추적 시작 | [장애 탐색](references/troubleshooting.md) |
| 분석 범위·미확인 사항·MCP 인덱스 | [커버리지](references/coverage.md) |

## 이 시스템에서 특히 중요한 구분

- 공통 시간표와 학생별 시간표, 학습 기록은 별도다. BO 편집을 학생 이력 전체 재작성으로 해석하지 않는다.
- 전 과정 완강, 이번 주/월 진도 100%, 학습 한 건 완료, 재학습 상태는 별개다.
- 조회처럼 보이는 학습 진입도 연결 정보 보정을 쓸 수 있다. `/job/runNow`는 실제 업무 처리이며 랭킹 재실행은 포인트와 연결된다.
- 코드에 cron이나 mapper가 있다고 실제 활성화·실행되는 것은 아니다. 티켓의 배포 완료 댓글도 현재 배포 SHA 증명은 아니다.
- 쿼리 제공은 운영 DB 실행 권한을 뜻하지 않는다. [가드레일](references/guardrails.md)에 이 시스템의 부작용과 데이터 취급 기준을 정리했다.

## 지식 갱신

새 사실을 얻으면 해당 도메인 문서에 근거와 확인 날짜를 추가한다. 추측을 확정 정책으로 바꾸지 않는다. KPA의 작업 지식은 MCP resource에 기록한다. 로컬 skill 변경/동기화는 사용자가 요청한 범위만 수행한다. 저장 경로와 조회 방법은 [Dooray/MCP](references/dooray.md)를 따른다.
