# API 작업

루트: `src/main/java/com/miraenchoco/frontApi/`, SQL: `src/main/resources/mapper/`.

주요 Controller: member(Member/ChocoB2B/ChocoB2C), schedule(MmbrSchedule/MmbrSelfStudy), lrn/Lrn, container/Container, report/MmbrReport, note/Note, intg/IntgApi, chococlass/ChococlassExternal, main/Main, player/Player, word/EngWord, file/File, board/Board. 세부 endpoint는 [인덱스](catalogs/endpoints.md) 또는 inventory --query로 찾는다.

## 응답·인증

- ApiResponse는 statusCode/message/data envelope이고 NON_NULL 직렬화다. HTTP 200만으로 업무 성공이라고 판단하지 않는다.
- AccessTokenAspect의 AccessTokenRequired 적용 지점에서 token header, teacher token parameter 경로, JwtContextHolder/TeacherJwtContextHolder를 확인한다. finally에서 context 정리한다.
- Bearer header를 일괄 전제로 하지 않는다. B2B/B2C/교사 열람/guest 분기는 실제 caller와 annotation 경계를 읽는다. 모든 endpoint의 인증/서명 검증을 감사했다는 뜻은 아니다.
- main의 MainCacheServiceImpl은 점검/운영상태 cache 성격이다. 이름만 보고 홈 데이터 전체 cache로 해석하지 않는다.

## 회원·포인트

MemberServiceImpl 로그인 흐름에서 회원 상태·구독 정보·학생 시간표 생성/보정이 이어진다. ChocoB2B/B2C와 외부 회원 연동은 내부 MMBR_SEQ와 외부 식별자의 mapping부터 확인한다.

PointServiceImpl.mmbrPointProcess는 트랜잭션이 있지만 B2C payChocoChip 외부 호출과 DB가 하나의 원자적 트랜잭션이라고 가정할 수 없다. 최대 3회 시도 경로가 있다. B2B는 mission 기록과 적립 불가 분기가 다르다. 재시도/수동 재처리 제안 시 중복 여부·외부 결과·내부 기록을 함께 확인한다.

## 학습·노트·리포트 진입

- 일정/학습은 [schedule-learning](schedule-learning.md).
- ContainerService/LrnService는 규모가 크므로 요청 handler와 실제 mapper를 좁혀 읽는다. API GET이라도 학습 연결을 보정할 수 있다.
- 노트 파일 계약은 [notes-files](notes-files.md).
- report mapper의 집계는 같은 완료 건수도 전체/주/월 범위와 대상 수업이 다르다. [reports-ranking](reports-ranking.md) 참고.
- XML의 select 태그 안에 procedure 호출이 있을 수 있다(예: callAttendPointReq). 태그 이름으로 read-only를 판정하지 않는다.

코드 수정 후 해당 API 계약과 소비하는 frontend/BO/batch caller를 함께 검증한다. 인증키·개인정보가 든 실제 운영 요청으로 smoke test를 임의 실행하지 않는다.
