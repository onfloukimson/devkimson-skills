# batch MyBatis 탐색 인덱스

기준 HEAD 8d97e5414cc377f1a68b916d6ac80bd240851f61. Working tree XML에서 추출. 태그/ID/테이블은 탐색 단서이며 SQL 본문과 include, caller를 읽어 의미를 확인한다. select 태그도 procedure 등 쓰기 효과를 포함할 수 있다. 테이블 목록은 TB_ 패턴 추출로 view/동적 이름/include의 전개 결과를 모두 포함하지 않는다.

## AlimtalkMapper.xml

원본: `src/main/resources/mapper/AlimtalkMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getAlimTalkTemplate` (select·8) | TB_CMM_CODE | code_val |
| `setAlimtalkInsertLog` (insert·12) | TB_ALIMTALK_LOG | mmbrSeq, month, resultCode, resultMsg, scheduleType, sendStatus, templateCode, toName, toPhone, week, year |
| `setAlimtalkTargetInsert` (insert·43) | TB_ALIMTALK_TARGET | mmbrSeq, month, pPhoneNum, profileName, reportType, week, year |
| `getAlimtalkTargetList` (select·67) | TB_ALIMTALK_TARGET, TB_MMBR | month, reportType, week, year |
| `updateAlimtalkTargetStatus` (update·92) | TB_ALIMTALK_TARGET | atSeq, sendStatus |
| `getDateWeekUtil` (select·99) | — |  |
| `getDateMonthUtil` (select·122) | — |  |

## JobFailMapper.xml

원본: `src/main/resources/mapper/JobFailMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `insertFailLog` (insert·8) | TB_BATCH_FAIL_LOG | bncSeq, errorMsg, jobName |

## MemoryQuiz.xml

원본: `src/main/resources/mapper/MemoryQuiz.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getMemoryQuizUserList` (select·9) | TB_MMBR, TB_MMBR_SCHEDULE, TB_MMBR_SELF_STUDY, TB_POINT_MISSION, TB_POINT_MISSION_MMBR | month, week, year |
| `getMemoryQuizWrongYn` (select·62) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | endDate, mmbrSeq, startDate |
| `getContentsList` (select·90) | TB_LRN_ACT, TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SCHEDULE_DTL | endDate, endOrd, limit, mmbrSeq, seq, startDate, startOrd |
| `insertSelfStudyMaster` (insert·172) | TB_MMBR_SELF_STUDY | lrnModuleCd, mmbrSeq, month, scheduleStCd, selfStudyTy, title, week, wrongYn, year |
| `insertSelfStudyDetail` (insert·201) | TB_MMBR_SELF_STUDY_DTL | cntntSeq, dtlOrd, mmbrSelfStudySeq |
| `updateSelfStudyMasterTitle` (update·210) | TB_MMBR_SELF_STUDY | mmbrSelfStudySeq, title |
| `getWeekRwdUserList` (select·218) | TB_POINT_MISSION, TB_POINT_MISSION_MMBR | mmbrSeq |

## MmbrSyncMapper.xml

원본: `src/main/resources/mapper/MmbrSyncMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getMmbrSyncTargetList` (select·8) | TB_MMBR, TB_MMBR_PROD |  |
| `updateMmbrStatus` (update·27) | TB_MMBR | mmbrSeq, statusYn |
| `updateMmbrProd` (update·35) | TB_MMBR_PROD | mmbrSeq, prodStatus |
| `insertMmbrSyncLog` (insert·42) | TB_MMBR_SYNC_LOG | logData, logTy, mmbrSeq |

## ModuleAvgMapper.xml

원본: `src/main/resources/mapper/ModuleAvgMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `avgReset` (update·7) | TB_LRN_AVG |  |
| `getAvgList` (select·11) | TB_LRN_ACT, TB_LRN_LESSON, TB_MMBR_LRN_PAGE |  |
| `processInsert` (insert·31) | TB_LRN_ACT, TB_LRN_AVG | avgElapsedTime, avgScore, avgSubTy, avgTy, lrnActSeq, lrnLessonSeq, lrnUnitSeq |

## PointMapper.xml

원본: `src/main/resources/mapper/PointMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getPointCode` (select·8) | TB_POINT_CODE | code |
| `setInsertPointMissionMmbr` (insert·21) | TB_POINT_MISSION_MMBR | mmbrPointHstSeq, mmbrSeq, month, pointMissionSeq, week, year |
| `viewPointCodeInfo` (select·55) | TB_POINT_CODE, TB_POINT_MISSION | mgCode |
| `getPointMissionMmbr` (select·69) | TB_POINT_MISSION, TB_POINT_MISSION_MMBR | mgCode, mmbrSeq, month, week, year |
| `addMmbrPointHistory` (insert·87) | TB_MMBR_POINT_HST | mgCode, mmbrSeq, point, pointRewardTy, reasonDetail |
| `mmbrUpdatePoint` (update·107) | TB_MMBR_B2C | mmbrSeq, point |

## RankMapper.xml

원본: `src/main/resources/mapper/RankMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `rankReset` (update·8) | TB_MMBR_RANK | month, rankTy, week, year |
| `getLessonRankList` (select·26) | TB_MMBR, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL_DATA | month, week, year |
| `getUnitRankList` (select·94) | TB_LRN_LESSON, TB_MMBR, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SCHEDULE_DTL_DATA | month, week, year |
| `insertRankBatch` (insert·205) | TB_MMBR_RANK | elapsedTime, endScore, loginScore, lrnLessonSeq, lrnUnitSeq, mmbrSeq, mmbrType, month, rankTy, rowNum, score, totalScore, week, year |
| `getMmbrWeekRkList` (select·249) | TB_LRN_LESSON, TB_MMBR, TB_MMBR_LOGIN_HST, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SCHEDULE_WEEK |  |
| `getMmbrMonthRkList` (select·365) | TB_LRN_LESSON, TB_MMBR, TB_MMBR_LOGIN_HST, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SCHEDULE_WEEK |  |

## RelearnMapper.xml

원본: `src/main/resources/mapper/RelearnMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getRelearnUserList` (select·8) | TB_MMBR, TB_MMBR_SELF_STUDY, TB_POINT_MISSION, TB_POINT_MISSION_MMBR | month, week, year |
| `getRecentMemoryQuizSeqs` (select·64) | TB_MMBR_SELF_STUDY, TB_MMBR_SELF_STUDY_DTL | endDate, mmbrSeq, startDate |
| `getRelearnWrongYn` (select·75) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | endDate, mmbrSeq, startDate |
| `getWeaknessContentsList` (select·102) | TB_LRN_ACT, TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SCHEDULE_DTL, TB_POINT_MISSION, TB_POINT_MISSION_MMBR | endDate, limit, mmbrSeq, seq, startDate |
| `insertSelfStudyMaster` (insert·202) | TB_MMBR_SELF_STUDY | lrnModuleCd, mmbrSeq, month, scheduleStCd, selfStudyTy, title, week, wrongYn, year |
| `insertSelfStudyDetail` (insert·231) | TB_MMBR_SELF_STUDY_DTL | cntntSeq, dtlOrd, mmbrSelfStudySeq |
| `getMonthRwdUserDate` (select·241) | TB_POINT_MISSION, TB_POINT_MISSION_MMBR | mmbrSeq |

## ReportMapper.xml

원본: `src/main/resources/mapper/ReportMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getTotalWeekMmbrList` (select·12) | TB_MMBR, TB_MMBR_B2B, TB_MMBR_B2C | month, reportType, week, year |
| `getListMmbrRank` (select·43) | TB_MMBR, TB_MMBR_RANK |  |
| `getMmbrRank` (select·68) | TB_MMBR, TB_MMBR_RANK | mmbrSeq |
| `getListUserLoginDateInfo` (select·93) | TB_MMBR_LOGIN_HST | endDt, mmbrSeq, startDt |
| `getListMmbrLrnSeries` (select·137) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | item, mmbrSeq |
| `getListMmbrLrnUnitReport` (select·159) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | lrnSeriesSeq, mmbrSeq |
| `getMmbrLrnPageScheduleResulInfo` (select·182) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | actTyCd, mmbrLrnSeq, mmbrSeq |
| `getMmbrLrnLessonList` (select·214) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | lrnUnitSeq, mmbrSeq |
| `setInertMmbrReport` (insert·270) | TB_MMBR_REPORT | lrnLessonSeq, lrnUnitSeq, mmbrScheduleSeq, mmbrSeq, month, reportSubTy, reportTy, repotCntnt, repotTitle, week, year |
| `getAttendSt` (select·306) | TB_MMBR_ST | month, stTy, week, year |
| `getAttendStCount` (select·315) | TB_MMBR, TB_MMBR_LOGIN_HST | endDate, startDate |
| `setMmbrStInsert` (insert·329) | TB_MMBR_ST | data, month, stSubTy, stTy, value, week, year |
| `getAttendStAvgLast` (select·345) | TB_MMBR_ST | month, stTy, week, year |
| `getListMmbrLrnLesson` (select·357) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endDt, endNum, lrnLessonSeq, lrnUnitSeq, mmbrScheduleSeq, mmbrSeq, startDt, startNum |
| `getMmbrSchedule` (select·443) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrSeq |
| `getMmbrScheduleDtlIncompleteCnt` (select·501) | TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endNum, mmbrScheduleSeq, mmbrSeq, startNum |
| `getMmbrLrnCountInfo` (select·513) | TB_LRN_LESSON, TB_MMBR_LRN | endDt, mmbrSeq, startDt |
| `getMmbrLrnPageCntntNoteInfo` (select·528) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_NOTE_QUESTION, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endDt, mmbrSeq, startDt |
| `getCommonDateWeekUtil` (select·542) | — |  |
| `getCommonDateUtil` (select·565) | — |  |

## Schedule.xml

원본: `src/main/resources/mapper/Schedule.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getScheduleTimeList` (select·8) | TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_WAIT |  |
| `updateScheduleMaster` (update·44) | TB_MMBR_SCHEDULE_WAIT | mmbrScheduleWaitSeq, waitTpCd |
| `updateScheduleTime` (update·51) | TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_WAIT | mmbrScheduleWaitSeq, newBasicTy, newNowScheduleOrd, newWeekStartNum, nowWeekNum |
| `resetScheduleDetails` (update·67) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SCHEDULE_WAIT | mmbrScheduleWaitSeq |
| `insertScheduleFailLog` (insert·92) | TB_BATCH_FAIL_LOG | errorMsg, jobName, mmbrScheduleWaitSeq |
| `getScheduleRoundList` (select·106) | TB_LRN_LESSON, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SCHEDULE_WAIT |  |
| `updateScheduleRound` (update·158) | TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_WAIT | mmbrScheduleWaitSeq, nowWeekNum, weekCnt |

## TotalCmsMapper.xml

원본: `src/main/resources/mapper/TotalCmsMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getMaxVersionByContentSeq` (select·8) | TB_CNTNT | contentSeq |
| `insertTbCntnt` (insert·13) | TB_CNTNT | cntntLrnTy, contentName, contentSeq, contentStatus, contentType, contentUrl, difficulty, downloadYn, educourseCode, educourseName, educourseName1, educourseName2, educourseName3, educourseName4, fileName, questionType, resourceStatus, serviceEndDate, serviceStartDate, serviceYn, solveTime, source, updateResourceStatus, version, viewerType |
| `insertTbCntntVersion` (insert·75) | TB_CNTNT_VERSION | contentSeq, version |
| `updateTbCntnt` (update·91) | TB_CNTNT | contentName, contentSeq, contentStatus, difficulty, educourseCode, educourseName, educourseName1, educourseName2, educourseName3, educourseName4, fileName, questionType, solveTime, source, version, viewerType |
