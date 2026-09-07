# 리포트·랭킹

## 기간과 발행

2026-09-07 월요일 기준 예시: 8월 5주차=8/31~9/6, 8월 월간=8/3~9/6. 달력의 8/1~8/31을 월간 보고 범위로 넣으면 달라진다. 이후 날짜는 실제 기간 계산 함수를 재확인한다.

TB_MMBR_REPORT의 RT00W/RT00M/RT00U, YEAR/MONTH/WEEK, REG_DT, DEL_YN/USE_YN을 함께 사용한다.
- 학습 대상 기간과 리포트 생성일은 별개.
- 일부 저장 경로는 MMBR_SCHEDULE_SEQ setter가 주석이므로 nullable할 수 있다. 회원+리포트 종류+기간을 기준으로 조회한다.
- 재생성은 논리 삭제와 insert를 수반한다. '이번에 생성된 행 존재'와 '학생에게 정상 노출/알림 도착'은 별개 검증.
- 학생 화면·LMS·배치 target selection이 같은 필터를 쓰는지 호출 흐름별로 확인한다.

## 실행 연결

ReportWeek/MonthService(batch) → 내부 인증 정보를 만들고 API report endpoint HTTP 호출 → API 집계/저장 → 응답 HTTP와 statusCode 확인. batch의 비슷한 이름 SQL을 실제 실행 경로로 단정하지 않는다.

주·월 report rank가 먼저 계산되고 이후 리포트를 만든다. 상세 시각/작업은 [batch-operations](batch-operations.md).
주간/월간 리포트 알림톡은 #81에 따라 2026-05-19 운영 중지, 5/26 최종 확인. BO 질문노트 답변 알림톡은 별개로 유지됐다. 현재 스케줄 활성 상태는 실제 운영 조회가 필요하다.

## 랭킹 대상과 집계

#183: 비활성/삭제 수업 포함으로 화면 수업 수와 rank 분모가 달라진 문제. batch db3102b에서 활성 수업 조건 추가, 8/20 운영 반영 및 8월 2주차 재생성 댓글 확인.
현재 **주간 V2_Schedule**에 active lesson 필터가 존재하므로 이를 새 요구로 반복 적용하지 않는다. 월간 V2_WeekScore에는 같은 필터가 직접 존재하지 않는다. 두 경로를 같은 구현으로 일반화하지 않는다. API 조회, batch 집계, 보고서 저장본 중 어느 값이 아직 다른지 좁힌다.

RankCard의 endCnt/allCnt는 기간별 진도율이며 전 과정 완강 판정과 다르다. API report 서비스도 전체/해당 기간 건수를 나눠 쓴다.
월간 ranking mapper는 주간 점수를 평균하고 첫 완료 시점의 기간 조건을 쓰는 경로가 있다. 주간 SQL을 단순히 month 필터로 바꾸지 않는다.
주·월 회원 랭킹의 ROW_NUMBER는 MMBR_TYPE별 파티션에서 TOTAL_SCORE DESC, AVG_ELAPSED_TIME ASC, MMBR_SEQ ASC 순서다. 특정 학생만 먼저 WHERE로 제한한 후 ROW_NUMBER를 계산하면 전체 순위를 재현하지 못한다. 전체 모집단 순위 계산 후 학생을 필터링한다. 수업/단원 랭킹은 별도의 partition/정렬이므로 같은 tie-break를 가정하지 않는다.
랭킹 재처리는 기존 rank 삭제/reset 및 B2C 상위 순위 포인트와 연결된다. 대상 기간과 중복 지급 방식을 확인하기 전 재실행하지 않는다.

## 조사 순서

보고 기간/종류 → 회원 자격과 시간표 → 활성 lesson/완료 범위 → batch 실행 로그 및 API 업무응답 → 저장된 리포트 → frontend 조회 조건. 평균 오차는 집계 분자/분모, 시간 단위, 0/null 처리부터 비교한다. [#198](content-averages.md)의 DB 이벤트 제한 이력과 ModuleAvg reset/insert도 확인한다. API 9dee01b 단원 평균 시간 수정도 참고.
