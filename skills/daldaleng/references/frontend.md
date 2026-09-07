# 프론트엔드

구조 탐색: src/routers, services, hooks, store, pages, components, layouts. hook 폴더는 화면마다 `hook` 단수와 `hooks` 복수가 섞여 있다. 분석 시 자동 인덱스 밖 caller도 git grep으로 찾는다.

주요 화면: /basic/*, /container, /home(/unit), /schedule/list·manage, /learning/basic·reading·vocabulary·grammar, /selfstudy/theme·memory·relearn, /note/hard·wrong·question, /note/question/:questionId, /report/highlights·evaluation·comprehensive, /myNote, /mission, /parent/timeTable. guest/inspection/maintenance/networkError 분기도 별도다.

## 요청과 상태

- services/useAxios.jsx: timeout 30000, withCredentials, daldalAccessToken → token header. VIEW는 열람 대상 token, GUEST 또는 MMBR_SEQ=-1은 별도 경로.
- requestApi는 response.data(API envelope)를 반환한다. 소비처가 data를 몇 번 벗기는지 확인한다. 401은 로그인 이동 경로.
- 오류에 request data/header가 붙는 경로가 있으므로 디버그 정보를 티켓에 그대로 붙이지 않는다.
- useGetQuery는 [query.key, params]를 query key로 쓰고 initEnabled=false. request/refetch와 requestAsync(queryFn 직접 호출)의 cache 동작이 다르다. 여러 서비스의 key 누락 가능성을 실제 소비처별로 확인한다.
- useMutation wrapper의 mutate/mutateAsync 차이를 유지한다.
- useZuUser의 role/mmbrType/isB2CUser 계산과 API 회원 상태를 혼동하지 않는다.

## 기능 연결

| 화면·hook | service/API | 함께 볼 코드 |
|---|---|---|
| schedule/hook/useSchedule, PopupChangeJindo, PopupChangeSession | useTimeTableService → /student/schedule/timeTable·info·weekCntSave·progressSave·levelSave | API MmbrScheduleService, batch ScheduleTime |
| report 화면 | useReportService → /student/report/series·lesson·list·reportView·ai, /student/rank/list | API report mapper, batch ranking |
| note/question/detail/hook/useNoteQuestionDetail | useQuestionNoteService multipart | API NoteVO/NoteService, BO note |
| container/hooks/useViewerMessage | 학습 viewer bridge → useLearningService 등 | ContainerService, LrnService, page/content 저장 |

## 뷰어와 완료

useViewerMessage는 LRN_HST_REQUEST, LEARNING_GRADING_REQUEST, COMPLETE_LEARNING_REQUEST, CONTAINER_AUDIO_PLAY 등의 이벤트를 분기한다. postMessage target '*' 사용 지점도 있으므로 caller/origin/token 전달 경계를 읽는다. 메시지 수신, UI 완료 팝업, DB 학습 완료를 각각 확인한다.

homeLessonAllComplete, RelearningPopup, RankCard는 서로 다른 완료/재학습/진도 표시를 한다. 주간 진도 100%로 전 과정 완강을 결론내리지 않는다. notes 상세의 첨부 계약 불일치 후보는 [notes-files](notes-files.md) 참고.

package scripts: build-develop/build-staging/build-prod(env-cmd .env.*), lint, serve(node server.js). 브라우저 환경/빌드 모드가 다르므로 기본 npm build를 추정하지 않는다. 이번 지식 작업에서는 앱 빌드나 브라우저 통합 검증을 수행하지 않았다.
