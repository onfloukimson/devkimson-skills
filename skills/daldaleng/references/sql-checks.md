# 조회 SQL과 검증

SQL 파일은 MySQL/MariaDB 계열의 읽기 전용 SELECT 예제다. 제공 당시 운영 DB에서 실행하지 않았다. 스키마/엔진 버전과 실행 계획은 대상 환경에서 확인한다. 예제에 회원 이름·이메일은 포함하지 않는다.

| 파일 | 목적 | 입력/출력 |
|---|---|---|
| [completion-current.sql](sql/completion-current.sql) | getAllLessonEndYn 기반 현재 완강 후보 + 주/월 발행 표시 | as_of_date, report_year/month/week → 학생 seq, 미완료 수, 필요 주차, 발행일 |
| [report-publication.sql](sql/report-publication.sql) | 한 학생의 해당 기간 주·월 리포트 유효 행/생성일 확인 | member_seq, year/month/week → 보고서 종류별 count/min/max 생성일 |
| [schedule-state.sql](sql/schedule-state.sql) | 한 학생의 유효 시간표별 원본 상세/활성 수업/완료 이상치 | member_seq → schedule seq와 분류별 건수 |

## 완강 예제의 정확한 범위

completion-current.sql 기본값은 **2026-09-07 / 8월 5주차 / 8월 월간이라는 과거 사례**다. 매번 조회 목적에 맞게 params를 바꾼다. 기준 날짜는 KST 의도이며 DB session timezone/REG_DT 저장 기준 확인이 필요하다.

원본 함수와 같은 핵심: active LTC001/LTC002 + main/basic 조건, END_ROUND=0 없음, MAX(main SCHEDULE_ORD), 2×WEEK_CNT로 올림한 필요 주차, NOW_WEEK_DT와 기준일의 월요일 주차 비교.
추가 모집단: 회원 STATUS_YN=Y, BASIC_TEST_YN=Y. 원본 함수 자체에는 없다.
추가 정상성 전제: WEEK_CNT>0. 대상 0건/null END_ROUND 등은 [schedule-state](sql/schedule-state.sql)로 따로 점검한다. target_lesson_cnt>0 조건을 추가하면 원본과 다른 방어 로직이다.

발행 표시는 그 날짜 00:00 이상 다음날 00:00 미만 REG_DT인 유효 보고서를 찾는다. 늦은 재생성/다른 날 발행을 보려면 날짜 조건을 변경한다.
기본 결과는 완강 후보 전체이고 발행 여부를 Y/N으로 표시한다. 두 리포트 모두 발행된 학생만 요구하면 마지막의 두 조건을 활성화한다.
현재 시간표 기준 결과이므로 과거 완강 이벤트 이력이나 최초 완강일을 반환하지 않는다.

사용자가 이 사례를 운영에서 조회해 1명이 나왔다고 전달했다. 실학생 행/운영 DB를 에이전트가 확인한 결과는 아니다. #145에 수동 완강 시험 이력이 있지만 조회된 1명과 동일인이라고 확인되지 않았다.

## 검증

scripts/validate_completion_query.py는 SQLite 메모리 fixture로 19명의 정상/미완료/basic제외/비활성수업/주차경계/보고기간/생성일/최신시간표 사례를 검증한다. MySQL 날짜 함수만 fixture용으로 변환한다.
--api-repo를 주면 실제 getMmbrScheduleInfo XML SELECT도 읽어 모델링한 Java 조건과 비교한다. DB 접속 없이 실행한다.

```bash
python scripts/validate_completion_query.py --api-repo "C:/devkimson/02_workspace/02_miraen/daldal-english-api"
```

SQLite 통과는 MariaDB 운영 실행/성능 검증이 아니다. 운영 변경 SQL이나 재처리 SQL은 예제에 포함하지 않는다.
