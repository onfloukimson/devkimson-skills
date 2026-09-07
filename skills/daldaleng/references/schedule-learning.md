# 시간표·학습·완강

## 공통 편성과 학생 반영

BO ScheduleServiceImpl.updSchedule → 공통 schedule mapping 변경.
API MemberServiceImpl 로그인 또는 MmbrScheduleController /schedule/checkSchedule → MmbrScheduleServiceImpl.setStudentScheduleCheckSchedule.
Mapper getListMmbrScheduleDtlUptCheck가 학생 시간표에 없는 공통 수업을 찾고, 서비스는 allTotalCnt+i+1 순서로 추가한다. 초기 상태 R, 학습 ID/완료 페이지 0, 초기 INFO_DATA 경로를 확인했다.

누락 후보 조회와 실제 insert 조건은 다르다. getListMmbrScheduleDtlUptCheck는 공통 매핑/학생 시간표 활성 조건과 기존 상세 부재를 확인하지만 lesson USE_YN/모듈 제한은 없다. 실제 삽입은 MC003와 활성 단원·시리즈를 요구한다. 따라서 후보가 있어도 삽입되지 않을 수 있다. 서비스 응답 개수는 실제 insert 결과 합계가 아니라 후보 목록 크기이고, 로그인 caller는 반환 ApiResponse를 검사하지 않는다. 로그인 성공이나 업데이트 개수만으로 완료를 판정하지 말고 학생 상세 행을 확인한다.

따라서 운영자의 공통 수업 순서 변경이 기존 학생의 순서·완료 이력을 전부 같은 순서로 재작성한다는 뜻이 아니다. 학생별 누락 편성, 기존 진행 기록, 활성 수업 여부를 구분해 조사한다.

## 학습/쌍둥이

TB_MMBR_SCHEDULE_DTL → TB_MMBR_LRN → TB_MMBR_LRN_PAGE → TB_MMBR_LRN_PAGE_CNTNT 순으로 상태가 연결된다. 한 테이블 플래그만 강제로 맞추는 복구는 이 계층의 불일치를 남길 수 있다.

TwinAdd 계열은 S003/LTC002에서 같은 단원·LESSON_ORD의 LTC005를 연결하는 경로가 있다. TwinSync는 비어 있는 연결을 보정하는 유일성 조건을 확인해야 한다. getStudentLesson 진입 중 연결 보정이 실행될 수 있어 조회 요청이 쓰기를 수반한다.

9월 4일 커밋 b1ec620/10a10f1은 쌍둥이 연결·INFO_DATA 보정과 관련된다. 9월 7일 working tree에서 LrnServiceImpl의 INFO_DATA 응답 재구성 경로가 다시 변경 중이었다. getListMmbrLrnInfoRepair mapper 존재만으로 현재 caller가 실행한다고 주장하지 않는다. HEAD와 diff를 같이 읽는다.

## getAllLessonEndYn의 실제 판정

소스: API MmbrScheduleServiceImpl.getAllLessonEndYn → MmbrScheduleMapper.getMmbrScheduleInfo → getWeekLastNumCheck.

1. 현재 유효한 학생 시간표를 선택한다.
2. DEL_YN=N/USE_YN=Y 수업의 LTC001/LTC002 중 MC003 main, BASIC_TY=Y이면 MC002 basic도 대상으로 한다.
3. 대상에 END_ROUND=0인 수업이 없어야 한다.
4. ALL_TOTAL_CNT는 **main 수업의 MAX(SCHEDULE_ORD)** 이다. 단순 COUNT가 아니다.
5. requiredWeek = ceil((ALL_TOTAL_CNT - (BASIC_TY=N이면 BASIC_CNT, 아니면 0)) / (2 × WEEK_CNT)).
6. requiredWeek <= NOW_WEEK_NUM이고, NOW_WEEK_DT가 있어야 하며 기준일과 같은 월요일 기준 주차가 아니어야 한다.

getAllLessonEndYn 자체에는 TB_MMBR.STATUS_YN/BASIC_TEST_YN 모집단 조건이 없다. 운영 대상 학생을 제한하는 조회 SQL에서 이를 더하면 함수 그대로의 전체 회원 결과와 다르다.

주의:
- 이 판정은 현재 시간표/콘텐츠 상태다. 과거 날짜에 실제로 완강했다는 이벤트 이력 조회가 아니다.
- 대상 0건, END_ROUND null, WEEK_CNT 비정상, 미래 NOW_WEEK_DT 등은 정상 데이터 전제 밖이다. 추가 방어조건은 운영 품질 보강이며 원본 함수 동치 조건이라고 숨기지 않는다.
- daldal.allLessonEndCheck(default N)는 progressSave의 완강/초기화 관련 분기에 영향을 준다. getAllLessonEndYn 반환과 동일한 switch가 아니다.
- ContainerService의 완강 후 weekYn/monthYn=N 보상 분기를 별도로 확인한다.
- 정책 PDF '완강 [AS-IS]'와 운영 #145는 재학습/초기화 맥락의 근거다. AS-IS 문서를 현재 환경 설정보다 우선하는 실행 보장으로 취급하지 않는다.

[완강 SQL](sql-checks.md)에는 과거 2026-09-07 조회 예제와 추가 필터 의미가 있다.
