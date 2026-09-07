# 작업용 코드 지도

api/bo/batch/front 별칭은 [repositories](repositories.md) 기준이다. 정확한 클래스/메서드 경로는 catalog나 git grep으로 확인한다. 줄 번호는 변경되므로 심볼을 우선한다.

| 질문 | 시작 심볼 | 이어 읽을 곳 |
|---|---|---|
| 완강 Y/N은 왜 다른가 | api MmbrScheduleServiceImpl.getAllLessonEndYn | MmbrScheduleMapper.getMmbrScheduleInfo, getWeekLastNumCheck |
| 공통 시간표 변경 반영 | bo ScheduleServiceImpl.updSchedule | api setStudentScheduleCheckSchedule, getListMmbrScheduleDtlUptCheck |
| 쌍둥이/학습 저장 오류 | api LrnServiceImpl.getStudentLesson, ContainerServiceImpl | TwinAdd/TwinSync, LRN/PAGE/CNTNT mapper와 viewer message |
| 리포트 발행 | batch ReportWeekService/ReportMonthService | API MmbrReport, TB_MMBR_REPORT, front useReportService |
| 랭킹 분모·점수 | batch RankMapper/Report*Rk 서비스 | api report, front RankCard |
| 질문 첨부 계약 | front useNoteQuestionDetail | api NoteVO, setNoteNoteAdd/Mod, BO MmbrNoteQuestionMapper |
| 운영 답안 표시 | bo AnswDisplayTypeHandler | MemberMapper resultMap, Thymeleaf |
| LMS 학습률/null | api ChococlassExternalWeek/MonthServiceImpl | DTO, chococlass XML, #174 |
| 외부 회원/포인트 | api Member/ChocoB2B/ChocoB2C/PointService | member/point/intg mapper, batch MmbrSync |
| 단어장 | front useWordBookService → api EngWordController/Service | EngWordMapper, TB_MMBR_ENG_WORD, TB_MMBR_ENG_WORD_CNT |
| 자율/기억/취약 학습 | front useSelfStudyService → api MmbrSelfStudyService | TB_MMBR_SELF_STUDY/DTL, batch Relearn/MemoryQuiz |
| 콘텐츠 동기화 | bo CmsSync, batch TotalCmsJob | lesson/content/version mapping |
| 도전과제/출석 | api PointService, BO reward | TB_POINT_MISSION(_MMBR), TB_MMBR_POINT_HST, 외부 적립 |
| 주차 전환 | batch ScheduleTimeJob | processSingleSchedule, schedule mapper |
| 배치 등록/수동 실행 | batch QuartzConfig/JobController/JobService | 조건부 bean, trigger, 호출 service |

## 자동 탐색 자료

- [API mapper](catalogs/api-mappers.md): 273 statements/fragments
- [BO mapper](catalogs/backoffice-mappers.md): 229
- [batch mapper](catalogs/batch-mappers.md): 72
- [Controller/frontend 요청](catalogs/endpoints.md): 43 Controller + 77 문자열 요청
- scripts/inspect_repository.py: 변경 후 같은 인덱스를 읽기 전용 재생성

목적을 정한 뒤 mapper ID로 Java interface와 caller를 같이 찾는다. XML이 존재해도 현재 caller에서 사용하지 않을 수 있다. body 통째 복제 대신 설명·심볼·입력·테이블을 유지해 코드 수정 시 원본을 다시 읽게 한다.
