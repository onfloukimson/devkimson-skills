# API/BO/batch endpoint와 frontend 요청 탐색

2026-09-07 working tree annotation/문자열 추출. Controller의 class base path와 method path가 따로 나열되며 결합된 OpenAPI 명세가 아니다. 동적 URL, method 제한, params/header 조건, 인증/부작용은 실제 메서드를 읽는다.

## api

### BoardController.java

`src/main/java/com/miraenchoco/frontApi/board/controller/v1/BoardController.java`

- Request `${apiVersion.api-v1-path}/board` (줄 24)
- Post `/list` (줄 37)
- Post `/quote` (줄 48)
- Post `/viewsCnt` (줄 58)

### ChococlassExternalController.java

`src/main/java/com/miraenchoco/frontApi/chococlass/controller/v1/ChococlassExternalController.java`

- Request `/v1/api/learning` (줄 30)
- Post `/today` (줄 48)
- Post `/weekly` (줄 62)
- Post `/weekly/students` (줄 76)
- Post `/monthly` (줄 89)
- Post `/monthly/students` (줄 102)

### ContainerController.java

`src/main/java/com/miraenchoco/frontApi/container/controller/v1/ContainerController.java`

- Request `${apiVersion.api-v1-path}/student` (줄 37)
- Get `/reset` (줄 51)
- Post `/container` (줄 69)
- Post `/container/page` (줄 121)
- Post `/container/page/content/save` (줄 135)
- Post `/container/page/video/progress` (줄 165)
- Post `/container/done` (줄 195)
- Post `/container/init` (줄 224)
- Get `/container/result` (줄 253)
- Get `/container/report` (줄 266)
- Get `/container/weekRwd` (줄 279)
- Get `/container/cfg` (줄 293)
- Post `/container/cfgSave` (줄 306)
- Get `/container/checkWeekRwd` (줄 335)

### FileController.java

`src/main/java/com/miraenchoco/frontApi/file/controller/v1/FileController.java`

- Request `${apiVersion.api-v1-path}/file` (줄 33)
- Post `/upload` (줄 46)
- Post `/delete` (줄 68)
- Get `/download` (줄 86)
- Post `/reportUpload` (줄 117)
- Post `/get` (줄 123)

### IntgApiController.java

`src/main/java/com/miraenchoco/frontApi/intg/controller/v1/IntgApiController.java`

- Request `${apiVersion.api-v1-path}/student` (줄 15)
- Get `/intg/week` (줄 24)
- Get `/intg/week/report` (줄 31)
- Get `/intg/month/report` (줄 38)

### LrnController.java

`src/main/java/com/miraenchoco/frontApi/lrn/controller/v1/LrnController.java`

- Request `${apiVersion.api-v1-path}/student` (줄 15)
- Get `/series` (줄 28)
- Get `/lesson` (줄 41)
- Get `/lesson/cntnt` (줄 54)

### MainController.java

`src/main/java/com/miraenchoco/frontApi/main/controller/v1/MainController.java`

- Request `${apiVersion.api-v1-path}/student/` (줄 18)
- Post `/getAnsw` (줄 32)
- Post `/info` (줄 45)
- Post `/attsDays` (줄 59)
- Post `/getReport` (줄 72)
- Post `/challenge` (줄 85)
- Post `/challengeList` (줄 98)
- Post `/challengeAdd` (줄 112)
- Post `/attsList` (줄 125)
- Post `/cardList` (줄 138)
- Post `/menu` (줄 151)
- Get `/studyThemeList` (줄 164)

### ChocoB2BController.java

`src/main/java/com/miraenchoco/frontApi/member/controller/v1/ChocoB2BController.java`

- Request `/member/api/b2b` (줄 19)
- Get `/organization/{userSeq}` (줄 24)
- Get `/class/{classSeq}/students` (줄 29)
- Get `/student/{studentSeq}` (줄 34)
- Get `/contract/{studentSeq}` (줄 39)
- Get `/teacher/{teacherSeq}/{userSeq}` (줄 44)
- Get `/organization/{orgSeq}/teachers` (줄 49)

### ChocoB2CController.java

`src/main/java/com/miraenchoco/frontApi/member/controller/v1/ChocoB2CController.java`

- Request `/member/api/b2c` (줄 15)
- Get `/parent/{childId}` (줄 23)
- Get `/child/{childId}` (줄 30)
- Get `/child/payment/{childId}` (줄 37)
- Get `/chocoChip/code` (줄 61)
- Post `/chocoChip/paid` (줄 67)

### MemberController.java

`src/main/java/com/miraenchoco/frontApi/member/controller/v1/MemberController.java`

- Request `${apiVersion.api-v1-path}/student` (줄 18)
- Post `/login` (줄 34)
- Post `/logout` (줄 46)
- Post `/impersonate/{mmbrSeq}/{adminSeq}` (줄 55)
- Post `/refreshToken` (줄 64)
- Post `/dupl_check` (줄 70)
- Post `/attend_check` (줄 77)
- Post `/attsSheet` (줄 90)
- Get `/lrnclub/status` (줄 103)
- Post `/lrnclub/accuracy` (줄 116)
- Get `/lrnclub/weekly-goal` (줄 129)

### NoteController.java

`src/main/java/com/miraenchoco/frontApi/note/controller/v1/NoteController.java`

- Request `${apiVersion.api-v1-path}/note` (줄 18)
- Post `/series_list` (줄 46)
- Post `/unit_list` (줄 51)
- Post `/lesson_list` (줄 56)
- Post `/note_add` (줄 61)
- Post `/note_list` (줄 72)
- Post `/my_question_list` (줄 82)
- Post `/note_mod` (줄 88)
- Post `/note_view` (줄 93)
- Post `/note_delete` (줄 102)
- Post `/note_best` (줄 111)
- Post `/inc_answer_list` (줄 116)
- Post `/basic` (줄 121)
- Post `/share_view` (줄 126)
- Post `/noteRead` (줄 136)

### PlayerController.java

`src/main/java/com/miraenchoco/frontApi/player/controller/v1/PlayerController.java`

- Request `${apiVersion.api-v1-path}` (줄 16)
- Post `/player/moduleInfo` (줄 30)

### MmbrReportController.java

`src/main/java/com/miraenchoco/frontApi/report/controller/v1/MmbrReportController.java`

- Request `${apiVersion.api-v1-path}/student` (줄 16)
- Get `/report/series` (줄 26)
- Get `/report/lesson` (줄 36)
- Get `/rank/list` (줄 42)
- Get `/report/list` (줄 49)
- Get `/report/reportView` (줄 60)
- Get `/report/ai` (줄 83)

### MmbrScheduleController.java

`src/main/java/com/miraenchoco/frontApi/schedule/controller/v1/MmbrScheduleController.java`

- Request `${apiVersion.api-v1-path}/student` (줄 35)
- Post `/schedule/create` (줄 49)
- Get `/schedule/timeTable/week` (줄 76)
- Get `/schedule/timeTable` (줄 89)
- Get `/schedule/info` (줄 102)
- Get `/schedule/timeTable/info` (줄 115)
- Post `/schedule/timeTable/weekCntSave` (줄 130)
- Post `/schedule/timeTable/progressSave` (줄 158)
- Post `/schedule/timeTable/levelSave` (줄 186)
- Post `/teacher/studentInfo` (줄 214)
- Post `/schedule/checkSchedule` (줄 228)

### MmbrSelfStudyController.java

`src/main/java/com/miraenchoco/frontApi/schedule/controller/v1/MmbrSelfStudyController.java`

- Request `${apiVersion.api-v1-path}/student` (줄 27)
- Get `/selfStudy` (줄 41)
- Get `/selfStudy/lesson` (줄 54)

### EngWordController.java

`src/main/java/com/miraenchoco/frontApi/word/controller/v1/EngWordController.java`

- Request `${apiVersion.api-v1-path}/student` (줄 22)
- Post `/word/{text}` (줄 35)
- Post `/word/list` (줄 62)
- Post `/word/dibs/delete` (줄 75)
- Post `/word/dibs/update` (줄 88)
- Post `/word/dibs/save` (줄 101)
- Get `/word/autocomplete` (줄 108)

## backoffice

### AdminController.java

`src/main/java/com/miraenchoco/bo/daldaleng/account/controller/AdminController.java`

- Get `/account/admin-list` (줄 35)
- Get `/account/admin-form` (줄 51)
- Post `/api/account/admin-upd` (줄 71)
- Post `/api/account/admin-add` (줄 88)
- Post `/api/account/admin-del` (줄 104)
- Post `/api/account/admin-approval-upd` (줄 114)
- Post `/api/account/admin-password-upd` (줄 126)
- Post `/api/mypage/password-upd` (줄 138)
- Post `/api/mypage/myinfo-upd` (줄 150)

### CmmCodeController.java

`src/main/java/com/miraenchoco/bo/daldaleng/common/controller/CmmCodeController.java`

- Get `/api/common/code-list` (줄 33)
- Post `/api/common/curriculum` (줄 46)
- Post `/api/common/educourse-list` (줄 56)

### CmmController.java

`src/main/java/com/miraenchoco/bo/daldaleng/common/controller/CmmController.java`

- Post `/api/common/contentUrl` (줄 48)
- Get `/common/content-viewer` (줄 53)
- Post `/api/common/lnb-toggle` (줄 59)
- Post `/api/upload/editor-image` (줄 65)
- Get `/api/common/download` (줄 75)

### CustomErrorController.java

`src/main/java/com/miraenchoco/bo/daldaleng/common/controller/CustomErrorController.java`

- Get `/error` (줄 14)

### HealthCheckController.java

`src/main/java/com/miraenchoco/bo/daldaleng/common/controller/HealthCheckController.java`

- Request `/healthcheck.html` (줄 9)

### CntntController.java

`src/main/java/com/miraenchoco/bo/daldaleng/content/controller/CntntController.java`

- Get `/content/resources-list` (줄 39)
- Get `/content/resources-form` (줄 52)
- Get `content/resources-excel-download` (줄 69)
- Post `/api/content/resources-upd` (줄 83)
- Post `/api/content/resources-sync-upd` (줄 95)
- Post `/api/content/resources-key-create` (줄 107)

### LrnActController.java

`src/main/java/com/miraenchoco/bo/daldaleng/content/controller/LrnActController.java`

- Get `/content/lessonAct-popup` (줄 35)
- Post `/api/content/lessonAct-popup` (줄 50)
- Post `/api/content/lessonAct-get` (줄 62)
- Post `/api/content/lessonAct-upd` (줄 75)

### LrnLessonController.java

`src/main/java/com/miraenchoco/bo/daldaleng/content/controller/LrnLessonController.java`

- Get `/content/curr-form` (줄 44)
- Get `/content/curr-excel-download` (줄 59)
- Post `/api/content/curr-lrncate-list` (줄 71)
- Post `/api/content/curr-del` (줄 83)
- Post `/api/content/curr-upd` (줄 115)
- Post `/api/content/curr-add` (줄 166)
- Post `/api/content/curr-info` (줄 200)
- Get `/content/lessonAct-excel-download` (줄 227)
- Get `/content/lessonAct-list` (줄 239)
- Get `/content/lessonAct-form` (줄 253)

### BoardController.java

`src/main/java/com/miraenchoco/bo/daldaleng/display/controller/BoardController.java`

- Post `/api/display/{page}-add` (줄 43)
- Post `/api/display/{page}-upd` (줄 66)
- Post `/api/display/{page}-del` (줄 86)
- Post `/api/display/maintheme-character-upd` (줄 101)
- Post `/api/display/{page}UseYn-upd` (줄 119)
- Get `/api/display/{page}UseYn-count` (줄 133)
- Post `/api/display/{page}-sort-upd` (줄 150)
- Get `/display/{page}-list` (줄 166)
- Get `/display/{page}-form` (줄 187)
- Get `/display/maintheme-popup` (줄 208)

### QuoteController.java

`src/main/java/com/miraenchoco/bo/daldaleng/display/controller/QuoteController.java`

- Get `/display/study-quote-popup` (줄 29)
- Post `/api/display/study-quote-add` (줄 43)
- Post `/api/display/study-quote-del` (줄 57)

### ExcelController.java

`src/main/java/com/miraenchoco/bo/daldaleng/excel/controller/ExcelController.java`

- Get `/{menu}/{page}-upload-popup` (줄 47)
- Post `/api/{menu}/{page}-excel-upload` (줄 66)
- Post `/api/{menu}/{page}-bulk-process` (줄 90)
- Post `/api/{menu}/{page}-result-download` (줄 111)

### HomeController.java

`src/main/java/com/miraenchoco/bo/daldaleng/home/controller/HomeController.java`

- Get `/` (줄 16)

### LoginController.java

`src/main/java/com/miraenchoco/bo/daldaleng/login/controller/LoginController.java`

- Get `/login` (줄 28)
- Post `/ex-login` (줄 42)
- Post `/signup/signup-request` (줄 60)
- Post `/signup/duplicate-check` (줄 72)
- Post `/signup/password-reset-check` (줄 84)
- Post `/signup/password-upd` (줄 96)

### MmbrController.java

`src/main/java/com/miraenchoco/bo/daldaleng/member/controller/MmbrController.java`

- Get `/member/{mmbrType}mmbr-list` (줄 36)
- Get `/member/{mmbrType}mmbr-form` (줄 56)
- Get `/api/member/{mmbrType}mmbrLoginHst-list` (줄 80)
- Get `/member/{mmbrType}mmbr-excel-download` (줄 96)
- Get `/member/b2bmmbr-popup` (줄 120)
- Get `/api/member/b2bmmbr-class-list` (줄 136)
- Get `/api/member/b2bmmbr-classLrn-view` (줄 151)
- Get `/api/member/{mmbrType}mmbr-token-get` (줄 161)
- Get `/api/statistics/attendance-list` (줄 177)

### MmbrTabController.java

`src/main/java/com/miraenchoco/bo/daldaleng/member/controller/MmbrTabController.java`

- Get `/member/{mmbrType}mmbr-tab{tabNumber}-view` (줄 58)
- Post `/api/member/{mmbrType}mmbr-wrong-list` (줄 87)
- Get `/member/{mmbrType}mmbr-wrong-popup` (줄 102)
- Post `/api/member/{mmbrType}mmbr-question-list` (줄 120)
- Post `/api/member/{mmbrType}mmbr-study-list` (줄 133)
- Get `/member/{mmbrType}mmbr-lrn-popup` (줄 147)
- Post `/api/member/{mmbrType}mmbr-mmbrlrn-list` (줄 168)
- Post `/api/member/{mmbrType}mmbr-weeklrn-list` (줄 184)
- Post `/api/member/{mmbrType}mmbr-lrncate-list` (줄 200)
- Post `/api/member/b2cmmbr-reward-list` (줄 217)
- Post `/api/member/{mmbrType}mmbr-schedule-list` (줄 233)
- Post `/api/member/{mmbrType}mmbr-schedule-upd` (줄 250)
- Post `/api/member/{mmbrType}mmbr-scheduleHist-list` (줄 266)
- Post `/api/member/{mmbrType}mmbr-wait-get` (줄 283)

### AdminMenuController.java

`src/main/java/com/miraenchoco/bo/daldaleng/menu/controller/AdminMenuController.java`

- Post `/api/account/admin-menu-list` (줄 25)

### MmbrNoteQuestionController.java

`src/main/java/com/miraenchoco/bo/daldaleng/note/controller/MmbrNoteQuestionController.java`

- Get `/note/question-list` (줄 34)
- Get `/note/question-form` (줄 48)
- Get `/note/questionAnsw-popup` (줄 62)
- Post `/api/note/question-upd` (줄 77)
- Post `/api/note/question-upd` (줄 84)
- Post `/api/note/questionAnsw-upd` (줄 101)
- Post `/api/note/question-bestCancel-upd` (줄 118)

### MmbrPointHstController.java

`src/main/java/com/miraenchoco/bo/daldaleng/reward/controller/MmbrPointHstController.java`

- Get `/reward/history-list` (줄 31)
- Get `/reward/history-form` (줄 45)
- Post `/api/reward/history-list` (줄 54)
- Get `/reward/history-excel-download` (줄 59)

### PointCodeController.java

`src/main/java/com/miraenchoco/bo/daldaleng/reward/controller/PointCodeController.java`

- Get `/reward/code-list` (줄 32)
- Get `/reward/code-form` (줄 46)
- Post `/api/reward/code-upd` (줄 60)

### PointMissionController.java

`src/main/java/com/miraenchoco/bo/daldaleng/reward/controller/PointMissionController.java`

- Get `/reward/mission-list` (줄 34)
- Get `/reward/mission-form` (줄 47)
- Post `/api/reward/mission-add` (줄 69)
- Post `/api/reward/mission-upd` (줄 86)

### PointMissionMmbrController.java

`src/main/java/com/miraenchoco/bo/daldaleng/reward/controller/PointMissionMmbrController.java`

- Get `/reward/missionMmbr-popup` (줄 29)
- Get `/reward/missionMmbrComplt-popup` (줄 40)
- Get `/reward/missionMmbr-excel-download` (줄 51)
- Get `/api/reward/missionMmbr-get` (줄 63)
- Post `/api/reward/missionMmbrPoint-add` (줄 76)
- Post `/api/reward/missionMultiMmbrPoint-add` (줄 89)

### ScheduleController.java

`src/main/java/com/miraenchoco/bo/daldaleng/schedule/controller/ScheduleController.java`

- Get `/schedule/setting-list` (줄 36)
- Get `/schedule/setting-form` (줄 50)
- Get `/schedule/setting-excel-download` (줄 68)
- Post `/api/schedule/setting-add` (줄 81)
- Post `/api/schedule/setting-upd` (줄 95)
- Post `/api/schedule/setting-del` (줄 110)
- Post `/api/schedule/setting-info-upd` (줄 124)
- Get `/api/schedule/setting-used-count` (줄 137)
- Get `/schedule/setting-lesson-popup` (줄 149)
- Post `/api/schedule/setting-lesson-get` (줄 170)
- Post `/api/schedule/setting-schedule-copy` (줄 183)
- Post `/api/schedule/setting-lesson-upd` (줄 194)

### StatLrnController.java

`src/main/java/com/miraenchoco/bo/daldaleng/statistics/controller/StatLrnController.java`

- Request `/api/statistics` (줄 16)
- Post `/weekly-list` (줄 22)
- Post `/area-list` (줄 28)
- Post `/weekly-dashboard-info` (줄 34)
- Post `/supplementary-self-list` (줄 40)
- Post `/supplementary-note-list` (줄 46)
- Post `/supplementary-eng-list` (줄 52)
- Post `/supplementary-dashboard-info` (줄 58)

### StatPointController.java

`src/main/java/com/miraenchoco/bo/daldaleng/statistics/controller/StatPointController.java`

- Request `/api/statistics` (줄 16)
- Post `/chocochip-list` (줄 22)

### StatUsageController.java

`src/main/java/com/miraenchoco/bo/daldaleng/statistics/controller/StatUsageController.java`

- Request `/api/statistics` (줄 18)
- Post `/service-list` (줄 25)
- Get `/service-usercnt-get` (줄 32)

### StatisticsController.java

`src/main/java/com/miraenchoco/bo/daldaleng/statistics/controller/StatisticsController.java`

- Request `/statistics` (줄 17)
- Get `/service-view` (줄 39)
- Get `/weekly-view` (줄 52)
- Get `/area-view` (줄 65)
- Get `/supplementary-view` (줄 78)
- Get `/chocochip-view` (줄 91)

## batch

### JobController.java

`src/main/java/com/miraenchoco/job/daldaleng/controller/JobController.java`

- Request `/job` (줄 23)
- Get `/list` (줄 44)
- Post `/status` (줄 51)
- Post `/reschedule` (줄 75)
- Post `/runNow` (줄 92)

## frontend 서비스 요청

### src/services/useCommonService.jsx

- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/file/reportUpload` (줄 12)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/file/get?fileSeq=${fileSeq}` (줄 33)
- GET `${import.meta.env.VITE_APP_API_URL}/maintenance` (줄 53)

### src/services/useEventService.jsx

- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/attsList` (줄 12)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/attsSheet` (줄 31)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/lrnclub/status` (줄 47)

### src/services/useHomeService.jsx

- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/schedule/info?timeType=${timeType}` (줄 13)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/getAnsw` (줄 33)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/noteRead?answYn=${answYn}` (줄 52)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/info` (줄 71)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/attsDays` (줄 90)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/challenge` (줄 109)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/board/list?boardType=${boardType}` (줄 129)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/challengeList` (줄 148)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/challengeAdd?pointMissionSeq=${pointMissionSeq}` (줄 167)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/getReport` (줄 186)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/board/quote` (줄 205)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/menu?linkTp=${linkTp}&path=${path}&isNative=${isNative}` (줄 224)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/board/list?boardType=popup` (줄 243)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/board/list?boardType=character` (줄 262)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/studyThemeList` (줄 281)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/board/viewsCnt?boardSeq=${boardSeq}` (줄 300)

### src/services/useLearningService.jsx

- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/series?seriesType=normal` (줄 10)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/lesson?seriesType=normal&lrnUnitSeq=${lrnUnitSeqArea}` (줄 29)

### src/services/useQuestionNoteService.jsx

- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/series_list?noteType=${noteType}` (줄 12)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/unit_list?lrnSeriesSeq=${lrnSeriesSeq}` (줄 27)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/lesson_list?${queryString}` (줄 51)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/note_list?${queryString}` (줄 93)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/note_view?noteType=${noteType}&mmbrNoteQuestionSeq=${mmbrNoteQuestionSeq}&mmbrNoteQuestionGroupSeq=${mmbrNoteQuestionGroupSeq}&actTyCd=${actTyCd}` (줄 118)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/share_view?noteType=${noteType}&mmbrNoteQuestionSeq=${mmbrNoteQuestionSeq}&mmbrNoteQuestionGroupSeq=${mmbrNoteQuestionGroupSeq}&actTyCd=${actTyCd}` (줄 142)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/inc_answer_list?${queryString}` (줄 172)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/note_best` (줄 192)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/note_add` (줄 211)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/note_mod` (줄 231)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/note_delete?mmbrNoteQuestionSeq=${mmbrNoteQuestionSeq}&noteType=${noteType}` (줄 251)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/lesson/cntnt?mmbrLrnPageSeq=${mmbrLrnPageSeq}&lrnInning=${lrnInning}` (줄 270)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/note/my_question_list` (줄 285)

### src/services/useReportService.jsx

- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/report/series` (줄 12)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/report/lesson?lrnUnitSeq=${lrnUnitSeqReport}` (줄 28)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/report/list?${queryString}` (줄 52)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/report/reportView?${queryString}` (줄 90)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/report/ai?lrnLessonSeq=${lrnLessonSeq}` (줄 106)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/rank/list?${queryString}` (줄 146)

### src/services/useSelfStudyService.jsx

- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/selfStudy/lesson` (줄 12)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/selfStudy?${queryString}` (줄 34)

### src/services/useStudentService.jsx

- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/schedule/timeTable` (줄 12)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/schedule/timeTable/weekCntSave` (줄 62)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/schedule/timeTable/progressSave` (줄 84)

### src/services/useStudyModuleService.jsx

- POST `${import.meta.env.VITE_APP_API_STG_URL}/api/v1/player/moduleInfo?moduleCd=${moduleCd}&lrnSeq=${lrnSeq}&round=${round}` (줄 45)
- POST `${import.meta.env.VITE_APP_API_STG_URL}/api/v1/student/container/page?mmbrLrnSeq=${mmbrLrnSeq}&mmbrLrnPageSeq=${mmbrLrnPageSeq}` (줄 145)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/container/page?mmbrLrnSeq=${mmbrLrnSeq}&mmbrLrnPageSeq=${mmbrLrnPageSeq}` (줄 156)
- POST `${API_URL}/api/v1/student/container/page/content/save` (줄 205)
- POST `${API_URL}/api/v1/student/container/done` (줄 239)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/container/report?mmbrLrnPageSeq=${mmbrLrnPageSeq}` (줄 264)
- GET `${API_URL}/api/v1/student/container/result?mmbrLrnPageSeq=${mmbrLrnPageSeq}` (줄 288)
- GET `${API_URL}/api/v1/student/container/weekRwd?timeType=${timeType}` (줄 313)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/schedule/create` (줄 332)
- POST `${API_URL}/api/v1/student/container/page/video/progress` (줄 362)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/container/init` (줄 389)

### src/services/useTimeTableService.jsx

- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/schedule/timeTable` (줄 12)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/schedule/timeTable/info` (줄 32)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/schedule/timeTable/weekCntSave` (줄 52)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/schedule/timeTable/progressSave` (줄 75)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/schedule/timeTable/levelSave` (줄 99)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/series` (줄 123)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/lesson?lrnUnitSeq=${lrnUnitSeqArea}` (줄 143)

### src/services/useUserService.jsx

- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/login?moveType=${moveType}` (줄 13)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/refreshToken` (줄 33)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/dupl_check?mmbrSeq=${mmbrSeq}` (줄 52)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/container/cfg?cfgTy=${type}` (줄 72)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/container/cfgSave` (줄 94)

### src/services/useWordBookService.jsx

- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/word/${text}` (줄 12)
- GET `${import.meta.env.VITE_APP_API_URL}/api/v1/student/word/autocomplete?wordEng=${text}&pageSize=${pageSize}` (줄 31)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/word/dibs/save?wordKor=${wordKor}&wordEng=${wordEng}&cefrLevel=${cefrLevel}&partOfSpeach=${partOfSpeach}` (줄 51)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/word/dibs/update?mmbrEngSeq=${mmbrEngSeq}` (줄 70)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/word/dibs/delete?mmbrEngSeqList=${mmbrEngSeqList}` (줄 89)
- POST `${import.meta.env.VITE_APP_API_URL}/api/v1/student/word/list?pageSize=${pageSize}&pageNo=${pageNo}&sortType=${sortType}` (줄 108)
