# 증상에서 조사 시작

| 증상 | 첫 확인 | 다음 연결 | 성급히 하지 않을 판단 |
|---|---|---|---|
| 수업을 다 했는데 완강 N | getAllLessonEndYn, NOW_WEEK_DT, requiredWeek, active lesson | schedule-learning, PDF/#145 | endCnt=allCnt면 즉시 전체 완강 |
| 완강자가 1명뿐 | 학생 모집단 필터/시간표/기준 주차 | 완강 SQL의 회원 필터 제거 비교; #145 수동 시험 맥락 | 행을 보지 않고 테스트 계정이라고 확정 |
| BO 수업 추가가 일부 학생에 없음 | 공통 mapping과 해당 학생 DTL 차이 | login/checkSchedule 보정 caller | 모든 학생 시간표를 reset |
| 쌍둥이 학습 정보/문항 이상 | lesson 유형/단원/순서, pointer, LRN/PAGE/CNTNT | LrnService 현재 diff, twin repair mapper | 예전 INFO_DATA 보정 함수가 현재도 실행 |
| 주/월 리포트가 없음 | 대상 기간·회원 상태·active report 행 | batch target → API 업무응답 → 저장 → front | 알림 미수신=리포트 미생성 |
| 랭킹 분모가 시간표와 다름 | API/batch lesson 활성 조건과 저장본 생성 시각 | #183/db3102b, 기간별 counts | 이미 적용된 필터를 새 수정으로 반복 |
| LMS 진도/status가 다름 | API 계약 READY/OFFLINE/diagnostic/null | #174의 날짜별 결정 | 진단만으로 COMPLETE |
| 노트 이미지 삭제/교체가 안 됨 | multipart 실제 필드명 | front 상세 ↔ NoteVO ↔ Service, REF_TABLE | API와 front 계약이 같다고 전제 |
| BO만 첨부가 보임 | REF_TABLE prefix 조건/배열 vs concat | notes-files와 과거 데이터 | S3 파일 자체가 없다고 단정 |
| 답안이 배열 문자열로 보임 | AnswDisplayTypeHandler/템플릿 | f9a8f57, 원본 ANSW 유지 | 채점 데이터 수정 |
| 배치 목록과 실행이 다름 | 실제 등록 trigger 전체, enabled조건 | Quartz memory + 첫 trigger 목록 | 소스 cron=운영 활성 |
| 수동 실행 후 중복 적립 | runNow 직접 service, 기존 rank/point 기록 | ReportWeekRk/Point 외부 결과 | scheduler pause로 수동 중복 방지됨 |

소스상의 계약 불일치 후보는 실제 요청/배포본/데이터를 확인하기 전 운영 장애로 확정하지 않는다. 문제에 맞는 최소 재현을 만든 뒤 변경한다.
