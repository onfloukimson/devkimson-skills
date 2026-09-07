# 백오피스

루트 `src/main/java/com/miraenchoco/bo/`, 달달영어 도메인 `daldaleng`, Mapper `src/main/resources/mapper/`, 화면은 Thymeleaf templates의 account/content/display/member/tab/note/reward/schedule/statistics.

## 권한과 요청

Spring Security의 ADMIN/SUPER_ADMIN/TUTOR_ADMIN/CUSTOM_ADMIN, 세션/JSESSIONID, CustomSecurityChainFilter를 확인한다. ApiPermInterceptor/WebPermInterceptor의 이름과 실제 동작은 다르며 확인 당시 preHandle은 true였다. interceptor 이름만으로 권한이 검증된다고 판단하지 않는다.

## 공통 시간표 편집

ScheduleServiceImpl.updSchedule은 수업 존재/사용 여부를 검증하고 기존 공통 매핑을 논리 삭제한 뒤 다시 넣는다. 학생의 TB_MMBR_SCHEDULE_DTL 전체를 직접 재작성하는 흐름이 아니다. 학생 반영은 API 로그인/checkSchedule의 누락 편성 추가 경로와 연결된다. [시간표](schedule-learning.md)를 함께 읽는다.

## 콘텐츠·버전

LrnLesson/LrnAct/Cntnt/CmsSync 관련 서비스와 Excel import/export 경로를 묶어 본다. 수업 사용 여부 변경은 학습 편성뿐 아니라 랭킹/리포트 분모에 영향을 준다. TB_CNTNT_VERSION을 최신 행으로 바꾸는 것이 항상 정답은 아니다. 요청의 콘텐츠 버전과 연결된 lesson/학습 이력을 확인한다.

## 질문 답변과 표시

- MmbrNoteQuestionServiceImpl.updMmbrNoteQuestionAnsw는 답변 데이터, answ 첨부 삭제/업로드, 답변 여부 변경, sendNoteQuestionAnswAlimTalk와 연결된다.
- 답변 변경/재저장에 외부 알림 부작용이 있으므로 단순 화면 수정과 구분한다.
- AnswDisplayTypeHandler는 ANSW JSON 배열에서 빈 항목을 제외하고 `/`로 이어 표시한다. scalar는 text, 잘못된 JSON은 원문 fallback. f9a8f57에서 템플릿 파싱을 이동했다. 표시 형식을 바꾸려고 원본 답안이나 채점 로직을 바꾸지 않는다.
- 최근 로그인 값은 회원/노트 mapper 수정 이력이 각각 존재한다. 한 화면을 고치고 다른 화면이 같은 쿼리를 쓴다고 가정하지 않는다.

[파일 계약](notes-files.md), [BO mapper 인덱스](catalogs/backoffice-mappers.md), [이력](history.md)에서 이어서 찾는다.
