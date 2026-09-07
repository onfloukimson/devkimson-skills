# api MyBatis 탐색 인덱스

기준 HEAD 9dee01b5efae401c0666628852fd5a7b0fb30eea. Working tree XML에서 추출. 태그/ID/테이블은 탐색 단서이며 SQL 본문과 include, caller를 읽어 의미를 확인한다. select 태그도 procedure 등 쓰기 효과를 포함할 수 있다. 테이블 목록은 TB_ 패턴 추출로 view/동적 이름/include의 전개 결과를 모두 포함하지 않는다.

## board/BoardMapper.xml

원본: `src/main/resources/mapper/board/BoardMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getBoardNoticeList` (select·17) | TB_BOARD | include: inc_col, inc_where |
| `getBoardMainPopupList` (select·26) | TB_BOARD, TB_FILE | include: inc_col, inc_where, inc_file |
| `getBoardCharacterList` (select·38) | TB_BOARD, TB_FILE | boardType; include: inc_col, inc_file |
| `getBoardThemeList` (select·55) | TB_BOARD | boardType; include: inc_col |
| `getBoardMainthemeList` (select·65) | TB_BOARD | boardType; include: inc_col |
| `getThemeFileList` (select·77) | TB_FILE | boardSeq |
| `getMainThemeFileList` (select·82) | TB_FILE | boardSeq |
| `inc_file` (sql·88) | — | refType |
| `inc_col` (sql·93) | — |  |
| `inc_where` (sql·105) | — | boardType, mmbrType |
| `getBoardStudyList` (select·116) | TB_BOARD, TB_FILE, TB_SPEECH | month, rt, week |
| `getSpeechTypeList` (select·229) | TB_SPEECH | month, rt, week |
| `getPromotionChekck` (select·247) | TB_BOARD |  |
| `getQuote` (select·262) | TB_QUOTE |  |
| `updateBoardViewCnt` (update·273) | TB_BOARD | boardSeq |

## chococlass/ChococlassExternalMonthMapper.xml

원본: `src/main/resources/mapper/chococlass/ChococlassExternalMonthMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getMonthlyAttendance` (select·9) | TB_MMBR_B2B, TB_MMBR_LOGIN_HST | endDate, startDate, studentUid |
| `getMonthlyComplete` (select·33) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LRN | endDate, startDate, studentUid |
| `selectMonthlyStudentLearning` (select·63) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LOGIN_HST, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_REPORT | reportMonth, reportYear, request.endDate, request.startDate, studentUid |

## chococlass/ChococlassExternalTodayMapper.xml

원본: `src/main/resources/mapper/chococlass/ChococlassExternalTodayMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getTodayLearningStudents` (select·9) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LOGIN_HST, TB_MMBR_LRN | studentUid |
| `getLoginDt` (select·112) | TB_MMBR_B2B, TB_MMBR_LOGIN_HST | studentUid |
| `getAvgScore` (select·125) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LRN, TB_MMBR_LRN_PAGE | studentUid |

## chococlass/ChococlassExternalWeekMapper.xml

원본: `src/main/resources/mapper/chococlass/ChococlassExternalWeekMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getWeeklyAttendance` (select·9) | TB_MMBR_B2B, TB_MMBR_LOGIN_HST | endDate, startDate, studentUid |
| `getWeeklyComplete` (select·32) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LRN | endDate, startDate, studentUid |
| `getWeeklyStudentAttendance` (select·59) | TB_MMBR_B2B, TB_MMBR_LOGIN_HST | endDate, startDate, studentUid |
| `getWeeklyStudentLearning` (select·82) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LRN | endDate, startDate, studentUid |
| `getWeeklyStudentAnswerRate` (select·111) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | endDate, startDate, studentUid |

## common/CommonMapper.xml

원본: `src/main/resources/mapper/common/CommonMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getMaintenanceInfo` (select·9) | TB_MAINTENANCE_NOTICE |  |

## file/FileMapper.xml

원본: `src/main/resources/mapper/file/FileMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `setInsertFile` (insert·8) | TB_FILE | fileExt, fileOrigNm, filePath, fileSize, refSeq, refTable, refType, regUser |
| `setDeleteFile` (update·35) | TB_FILE | refSeq, refTable, refType |
| `getFileData` (select·48) | TB_FILE | fileSeq |
| `setInsertTbMmbrFile` (insert·53) | TB_MMBR_FILE | mmbrSeq, path |
| `getMmbrFileData` (select·66) | TB_FILE, tb_mmbr_file | mfSeq, path |

## intg/IntgApiMapper.xml

원본: `src/main/resources/mapper/intg/IntgApiMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getBasicTest` (select·8) | TB_LRN_LESSON |  |
| `getListWeekReport` (select·16) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | teacherSeq |
| `getMonthReport` (select·72) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | classSeq, teacherSeq |

## lrn/LrnPackageMapper.xml

원본: `src/main/resources/mapper/lrn/LrnPackageMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListLrnAct` (select·8) | TB_LRN_ACT | lrnLessonSeq |
| `getListLrnActDtl` (select·27) | TB_LRN_ACT_DTL | contentQstTy, lrnActSeq |
| `getLrnAct` (select·47) | TB_CNTNT, TB_LRN_ACT, TB_LRN_ACT_DTL, TB_LRN_LESSON, TB_LRN_UNIT | contentSeq |
| `getListLrnUnit` (select·66) | TB_FILE, TB_LRN_SERIES, TB_LRN_UNIT | lrnSeriesSeq, seriesCd |
| `getListLrnUnitSelfStudy` (select·90) | TB_FILE, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN | lrnSeriesSeq, mmbrSeq, seriesCd |
| `getListLrnLessonSelfStudy` (select·117) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SELF_STUDY | lessonTyCd, lrnUnitSeq, mmbrSeq |
| `getLrnLessonSchedule` (select·144) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | lrnLessonSeq, mmbrSeq |
| `getListLrnLessonSchedulePage` (select·187) | TB_CNTNT, TB_LRN_ACT, TB_LRN_ACT_DTL, TB_LRN_LESSON | lessonOrd, lrnUnitSeq |

## lrn/MmbrLrnMapper.xml

원본: `src/main/resources/mapper/lrn/MmbrLrnMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getMmbrLrnInfo` (select·29) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SELF_STUDY | lrnLessonSeq, lrnModuleCd, mmbrLrnSeq, mmbrSelfStudySeq, mmbrSeq |
| `getMmbrLrnWrongInfo` (select·105) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN | lrnLessonSeq, mmbrLrnSeq, mmbrSeq |
| `getListMmbrLrnPageResult` (select·132) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE | mmbrLrnPageSeq, mmbrSeq |
| `getListMmbrLrnPage` (select·155) | TB_MMBR_LRN_PAGE | mmbrLrnSeq |
| `getMmbrLrnPage` (select·170) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE | actTyCd, mmbrLrnPageSeq, mmbrLrnSeq |
| `getCheckCountMmbrLrn` (select·204) | TB_MMBR_LRN | lrnLessonSeq, lrnModuleCd, mmbrSeq, round |
| `setUpdMmbrLrnSt` (update·232) | TB_MMBR_LRN | lrnStCd, mmbrLrnSeq |
| `setUpdMmbrLrn` (update·240) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE | lrnStCd, mmbrLrnSeq |
| `inc_setUpdMmbrLrnInfo_Item` (sql·259) | — |  |
| `inc_setUpdMmbrLrnInfo_table` (sql·278) | TB_LRN_LESSON, TB_MMBR_SCHEDULE_DTL |  |
| `inc_setUpdMmbrLrnInfo_json` (sql·283) | — |  |
| `setUpdMmbrLrnInfo` (update·298) | TB_LRN_ACT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | mmbrLrnSeq, mmbrScheduleDtlSeq, twinMmbrScheduleDtlSeq; include: inc_setUpdMmbrLrnInfo_Item, inc_setUpdMmbrLrnInfo_table, inc_setUpdMmbrLrnInfo_Item, inc_setUpdMmbrLrnInfo_table, inc_setUpdMmbrLrnInfo_json, inc_setUpdMmbrLrnInfo_json, inc_setUpdMmbrLrnInfo_json, inc_setUpdMmbrLrnInfo_json |
| `setUpdMmbrScheduleDtlInfo` (update·362) | TB_LRN_ACT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SCHEDULE_DTL | mmbrScheduleDtlSeq, twinMmbrScheduleDtlSeq; include: inc_setUpdMmbrLrnInfo_Item, inc_setUpdMmbrLrnInfo_table, inc_setUpdMmbrLrnInfo_Item, inc_setUpdMmbrLrnInfo_table, inc_setUpdMmbrLrnInfo_json, inc_setUpdMmbrLrnInfo_json, inc_setUpdMmbrLrnInfo_json, inc_setUpdMmbrLrnInfo_json |
| `setInsertMmbrLrn` (insert·425) | TB_MMBR_LRN | lessonName, lrnLessonSeq, lrnModuleCd, mmbrSelfStudySeq, mmbrSeq, round, seriesName, unitName |
| `setInsertMmbrLrnGetSchedule` (insert·455) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SCHEDULE_DTL | mmbrScheduleDtlSeq, mmbrSeq, round |
| `getMmbrLrn` (select·491) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SELF_STUDY | mmbrLrnPageSeq, mmbrLrnSeq, mmbrSeq |
| `getMmbrLrnCountInfo` (select·557) | TB_LRN_LESSON, TB_MMBR_LRN | endDt, mmbrSeq, startDt |
| `getMmbrLrnCountTeacherInfo` (select·574) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | classSeq, endDt, startDt, teacherSeq |
| `getListMmbrLrnSeries` (select·622) | TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | item, mmbrSeq |
| `getListMmbrLrnSeriesReportWeek` (select·644) | TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | item, mmbrScheduleSeq, mmbrSeq |
| `getListMmbrLrnUnit` (select·664) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_SCHEDULE, TB_SCHEDULE_DTL | lrnSeriesSeq, mmbrSeq |
| `getListMmbrLrnUnitReport` (select·692) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | lrnSeriesSeq, mmbrScheduleSeq, mmbrSeq |
| `getMmbrLrnUnit` (select·723) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | lrnUnitSeq, mmbrSeq |
| `getListMmbrLrnLesson` (select·744) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endDt, endNum, lrnLessonSeq, lrnUnitSeq, mmbrScheduleSeq, mmbrSeq, startDt, startNum |
| `getMmbrLrnMission` (select·881) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE_DTL | mmbrLrnSeq, mmbrSeq |
| `getMmbrLrnCnt` (select·916) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | lrnUnitSeq, mmbrSeq |
| `setUpdMmbrLrnInit` (update·940) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | mmbrLrnSeq, mmbrSeq |
| `setUpdMmbrLrnRwdData` (update·974) | TB_MMBR_LRN | mmbrLrnSeq, mmbrSeq, rwdData |
| `setUpdMmbrLrnUseDt` (update·983) | TB_MMBR_LRN | mmbrLrnSeq, mmbrSeq |
| `getListMmbrLrnLessonReportWeek` (select·994) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SCHEDULE_WEEK | endDt, lrnUnitSeq, mmbrSeq, startDt |
| `getListMmbrLrnInfoRepair` (select·1057) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrScheduleDtlSeq, mmbrSeq |

## lrn/MmbrLrnPageMapper.xml

원본: `src/main/resources/mapper/lrn/MmbrLrnPageMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getCountMmbrLrnPage` (select·10) | TB_MMBR_LRN_PAGE | lrnActSeq, mmbrLrnSeq, mmbrSeq |
| `getListMmbrLrnPageCntnt` (select·21) | TB_CNTNT, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_NOTE_QUESTION | mmbrLrnPageSeq |
| `setDeleteMmbrLrnPageCntnt` (delete·56) | TB_MMBR_LRN_PAGE_CNTNT | mmbrLrnPageSeq |
| `getListMmbrLrnPageCntntWrong` (select·63) | TB_CNTNT, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | item, mmbrLrnPageSeq, mmbrSeq |
| `getListMmbrLrnPageCntntResponse` (select·104) | TB_MMBR_LRN_PAGE_CNTNT | mmbrLrnPageSeq |
| `getMmbrLrnPageCntnt` (select·115) | TB_CNTNT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_NOTE_QUESTION | lrnInning, mmbrLrnPageSeq |
| `getMmbrLrnPageComplt` (select·156) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE | mmbrLrnPageSeq |
| `getMmbrLrnPageCntntNoteInfo` (select·178) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_NOTE_QUESTION, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endDt, mmbrSeq, startDt |
| `getMmbrLrnPageEndCntntNoteInfo` (select·193) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endDt, mmbrSeq, startDt |
| `setInsertMmbrLrnPage` (insert·209) | TB_MMBR_LRN_PAGE | actOrd, actTyCd, lrnActSeq, lrnStCd, mmbrLrnSeq, mmbrSeq, pageName |
| `setInsertMmbrLrnPageGetLrnAct` (insert·238) | TB_LRN_ACT, TB_MMBR_LRN_PAGE | lrnActSeq, lrnStCd, mmbrLrnSeq, mmbrSeq |
| `setInsertMmbrLrnPageCntnt` (insert·269) | TB_CNTNT, TB_LRN_ACT_DTL, TB_MMBR_LRN_PAGE_CNTNT | cntntSeq, lrnActSeq, lrnInning, mmbrLrnPageSeq |
| `setInsertMmbrLrnPageCntntGetAct` (insert·298) | TB_CNTNT, TB_LRN_ACT_DTL, TB_MMBR_LRN_PAGE_CNTNT | lrnActSeq, mmbrLrnPageSeq |
| `setInsertMmbrLrnPageCntntGetSelfStudy` (insert·330) | TB_CNTNT, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SELF_STUDY_DTL | mmbrLrnPageSeq, mmbrSelfStudySeq |
| `setUpdMmbrLrnPageCntntSave` (update·363) | TB_MMBR_LRN_PAGE_CNTNT | answ, answStCd, elapsedTime, fAnswStCd, lrnInning, lrnProgress, markYn, mmbrLrnPageSeq |
| `setUpdMmbrLrnPageCntntComplt` (update·392) | TB_MMBR_LRN_PAGE_CNTNT | mmbrLrnPageSeq |
| `setUpdMmbrLrnPage` (update·402) | TB_MMBR_LRN_PAGE | elapsedTime, lrnStCd, mmbrLrnPageSeq, score |
| `setUpdMmbrLrnPageCntntTy` (update·427) | TB_CNTNT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SCHEDULE_DTL | mmbrLrnSeq, mmbrSeq |
| `getMmbrLrnPageCntntComptInfo` (select·454) | TB_MMBR_LRN_PAGE_CNTNT | mmbrLrnPageSeq |
| `getMmbrLrnPageResult` (select·479) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | actTyCd, lrnActSeq, mmbrLrnSeq, mmbrSeq |
| `getMmbrLrnPageScheduleResulInfo` (select·515) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | actTyCd, mmbrLrnSeq, mmbrSeq |
| `getMmbrLrnPageResulInfo` (select·549) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | actTyCd, mmbrLrnSeq, mmbrSeq |
| `getMmbrLrnPageMarkCnt` (select·584) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE | mmbrLrnSeq, mmbrSeq |

## lrn/MmbrLrnWrongMapper.xml

원본: `src/main/resources/mapper/lrn/MmbrLrnWrongMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `setInsertMmbrLrnWrong` (insert·9) | TB_MMBR_LRN_WRONG | actOrd, actTyCd, cntntPageTy, lrnActSeq, mmbrLrnSeq, mmbrSeq, pageName |
| `setInsertMmbrLrnWrongCntnt` (insert·40) | TB_CNTNT, TB_MMBR_LRN_WRONG_CNTNT | cntntSeq, lrnInning, mmbrLrnWrongSeq |
| `getMmbrLrnWrong` (select·66) | TB_MMBR_LRN, TB_MMBR_LRN_WRONG, TB_MMBR_LRN_WRONG_CNTNT | mmbrLrnSeq |
| `getListMmbrLrnWrongCntnt` (select·91) | TB_CNTNT, TB_MMBR_LRN_WRONG_CNTNT | mmbrLrnPageSeq |
| `getMmbrLrnWrongCntnt` (select·117) | TB_CNTNT, TB_MMBR_LRN, TB_MMBR_LRN_WRONG, TB_MMBR_LRN_WRONG_CNTNT | lrnInning, mmbrLrnPageSeq |
| `setUpdMmbrLrnWrongCntntSave` (update·147) | TB_MMBR_LRN_WRONG_CNTNT | answ, answStCd, elapsedTime, lrnInning, lrnProgress, markYn, mmbrLrnPageSeq |
| `setUpdMmbrLrnWrong` (update·174) | TB_MMBR_LRN_WRONG | elapsedTime, lrnStCd, mmbrLrnPageSeq, score |
| `setUpdMmbrLrnWrongCntntComplt` (update·192) | TB_MMBR_LRN_WRONG_CNTNT | mmbrLrnPageSeq |
| `getMmbrLrnWrongCntntComptInfo` (select·202) | TB_MMBR_LRN_WRONG_CNTNT | mmbrLrnPageSeq |
| `setUpdMmbrLrnWrongComplt` (update·221) | TB_MMBR_LRN, TB_MMBR_LRN_WRONG | mmbrLrnSeq, mmbrSeq |

## main/MainMapper.xml

원본: `src/main/resources/mapper/main/MainMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getAnswYn` (select·13) | TB_MMBR | mmbrSeq |
| `getStudentInfo` (select·21) | TB_MMBR, TB_MMBR_B2B, TB_MMBR_B2C, TB_MMBR_LOGIN_HST | mmbrSeq |
| `getAttsDays` (select·42) | TB_MMBR_LOGIN_HST | mmbrSeq |
| `getAttsList` (select·71) | TB_MMBR_LOGIN_HST | mmbrSeq |
| `getListMainReport` (select·102) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_REPORT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | lastMonth, lastYear, mmbrSeq, month, week, year |
| `getListMainChallenge` (select·187) | TB_MMBR_SELF_STUDY, TB_POINT_MISSION, TB_POINT_MISSION_MMBR | lastMonthMonth, lastMonthYear, lastWeekMonth, lastWeekWeek, lastWeekYear, mmbrSeq, month, week, year |
| `attendanceCodeList` (sql·254) | — | rt |
| `getListChallenge` (select·258) | TB_MMBR_POINT_HST, TB_MMBR_SELF_STUDY, TB_POINT_MISSION, TB_POINT_MISSION_MMBR | endDt, lastEndDt, lastMonthMonth, lastMonthYear, lastStartDt, lastWeekMonth, lastWeekWeek, lastWeekYear, mmbrSeq, month, startDt, week, year; include: attendanceCodeList, attendanceCodeList, attendanceCodeList, attendanceCodeList, attendanceCodeList, attendanceCodeList |
| `setInsertChallenge` (insert·407) | TB_POINT_MISSION_MMBR | mmbrSeq, pointMissionSeq |
| `getChallengeCheck` (select·423) | TB_POINT_MISSION_MMBR | mmbrSeq, pointMissionSeq |
| `getAttsDayB2CList` (select·428) | TB_MMBR, TB_MMBR_POINT_HST, TB_POINT_CODE | mmbrSeq; include: attendanceCodeList, attendanceCodeList |
| `getAttsDayB2BList` (select·482) | TB_MMBR, TB_MMBR_LOGIN_HST | mmbrSeq |
| `getStudentMainCardList` (select·512) | TB_MMBR_LRN, TB_MMBR_REPORT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrSeq, month, week, year |
| `getMmbrToken` (select·563) | TB_MMBR | mmbrSeq |

## member/MemberMapper.xml

원본: `src/main/resources/mapper/member/MemberMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getMemberCheck` (select·8) | TB_MMBR | child_id, mmbr_type, sub_role |
| `setInsertTbMmbr` (insert·18) | TB_MMBR | grade, miraenchildid, mmbrType, profileName, subRole, thumbnailNumber, thumbnailPath, userId |
| `setInsertTbMmbrB2B` (insert·44) | TB_MMBR_B2B | className, classSeq, grade, gradeCode, miraenchildid, mmbrSeq, pPhoneNum, parentsName, profileName, teacherSeq, userId |
| `setInsertTbMmbrB2C` (insert·78) | TB_MMBR_B2C | age, cPhoneNum, chocoPoint, gender, grade, gradeCode, miraenchildid, miraenparentsid, mmbrSeq, pPhoneNum, profileName, schoolAddr, schoolName, userId |
| `setInsertTbMmbrProd` (insert·119) | TB_MMBR_PROD | mmbrSeq, paymentCode, paymentEndDt, paymentName, paymentStartDt, prodCount, prodStatus, transCode |
| `setInsertTbMmbrAgeny` (insert·146) | TB_MMBR_AGENCYS | adminEmail, adminId, adminName, adminPhoneNumber, agcyAddr, agcyName, agcyTel, agcyType, miraenagcyid, mmbrSeq, teacherEmail, teacherId, teacherName, teacherPhoneNum |
| `getTbMmbrid` (select·184) | TB_MMBR | child_id, mmbr_type |
| `setUpdMmbrlogin` (update·193) | TB_MMBR | mmbrId, sub_role, token, usrCookie |
| `setInsertLoginHistory` (insert·203) | TB_MMBR_LOGIN_HST | ip, login_br, login_dv, mmbrId |
| `getUserData` (select·209) | TB_MMBR, TB_MMBR_AGENCYS, TB_MMBR_B2B, TB_MMBR_B2C | mmbrId |
| `getListUserLoginDateInfo` (select·246) | TB_MMBR_LOGIN_HST | endDt, mmbrSeq, startDt |
| `setUpdMmbrBasicTestYn` (update·288) | TB_MMBR | basicTestYn, mmbrSeq |
| `getMmbrCfg` (select·298) | TB_MMBR_CFG | cfgTy, mmbrSeq |
| `getMmbrCfgCheckCount` (select·311) | TB_MMBR_CFG | cfgTy, mmbrSeq |
| `setUpdMmbrCfg` (update·327) | TB_MMBR_CFG | mmbrCfgSeq, value |
| `setInsertMmbrCfg` (insert·335) | TB_MMBR_CFG | cfgTy, mmbrSeq, value |
| `getClassInfo` (select·348) | TB_MMBR, TB_MMBR_AGENCYS, TB_MMBR_B2B | mmbrSeq |
| `setMmbrUpdate` (update·366) | TB_MMBR | grade, mmbrSeq, profileName, thumbnailNumber, thumbnailPath |
| `setMmbrB2CUpdate` (update·377) | TB_MMBR_B2C | age, cPhoneNum, chocoPoint, gender, grade, gradeCode, mmbrSeq, pPhoneNum, profileName, schoolAddr, schoolName |
| `setMmbrB2BUpdate` (update·393) | TB_MMBR_B2B | className, grade, gradeCode, mmbrSeq, pPhoneNum, parentsName, profileName |
| `setMmbrB2BTeacherUpdate` (update·405) | TB_MMBR_B2B | className, gradeCode, mmbrSeq |
| `getLoginCheck` (select·413) | TB_MMBR | mmbrSeq, usrCookie |
| `setUpdMmbrLastLogin` (update·423) | TB_MMBR | mmbrId |
| `getMmbrUserId` (select·431) | TB_MMBR, TB_MMBR_B2B, TB_MMBR_B2C | userId |
| `setInsertTbMmbrProdGroup` (insert·458) | TB_MMBR_PROD_GRP | mmbrType, paymentCode, paymentName |
| `getB2BTodayLoginCount` (select·465) | TB_MMBR_LOGIN_HST | mmbrId |
| `setUpdMmbrB2BloginCnt` (update·472) | TB_MMBR | mmbrId |
| `setTbMmbrAgenyUpdate` (update·478) | TB_MMBR_AGENCYS | mmbrSeq, teacherEmail, teacherId, teacherName, teacherPhoneNum |
| `setUpdateTeacherId` (update·489) | TB_MMBR_AGENCYS | mmbrId, teacherId |
| `setUpdateMmbrProd` (update·497) | TB_MMBR_PROD | mmbrSeq, paymentCode, paymentEndDt, paymentName, paymentStartDt, transCode |
| `getLearningAccuracyData` (select·509) | TB_LRN_ACT, TB_MMBR, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | childId |
| `getWeeklyGoals` (select·560) | TB_MMBR, TB_MMBR_SCHEDULE | childId |
| `getUserByChildId` (select·578) | TB_MMBR, TB_MMBR_B2B, TB_MMBR_B2C | childId |

## note/NoteMapper.xml

원본: `src/main/resources/mapper/note/NoteMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `inc_query` (sql·56) | — | endDate, lrnLessonSeq, lrnSeriesSeq, lrnUnitSeq, mmbrSeq, month, noteType, searchRegDt, startDate |
| `inc_query_study` (sql·112) | — | endDate, lrnLessonSeq, lrnSeriesSeq, lrnUnitSeq, mmbrSeq, month, noteType, searchRegDt, startDate |
| `getIncAnswerSeriesList` (select·169) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrSeq, rt |
| `getUnitList` (select·193) | TB_LRN_UNIT | lrnSeriesSeq |
| `getLessonList` (select·207) | TB_LRN_LESSON | lrnUnitSeq |
| `setInsertQuestion` (insert·221) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_NOTE_QUESTION | content, contentPage, contentSeq, lrnActSeq, lrnInning, lrnLessonSeq, lrnSeriesSeq, lrnUnitSeq, mmbrLrnPageSeq, mmbrLrnSeq, mmbrNoteQuestionGroupSeq, mmbrSeq, noteType, publicYn |
| `getListQuestion` (select·290) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION | mmbrType, offset, pageSize; include: inc_query |
| `getListQuestionStatusCnt` (select·320) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION | include: inc_query |
| `getQuestionCnt` (select·342) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION | mmbrSeq, mmbrType; include: inc_query |
| `setUpdQuestion` (update·363) | TB_MMBR_NOTE_QUESTION | content, mmbrNoteQuestionSeq, mmbrSeq, publicYn |
| `getQuestionView` (select·375) | TB_FILE, TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION | mmbrNoteQuestionSeq, mmbrSeq |
| `getBestCheck` (select·421) | TB_MMBR_NOTE_QUESTION | mmbrNoteQuestionSeq, mmbrSeq |
| `setDeleteQuestion` (update·432) | TB_MMBR_NOTE_QUESTION | mmbrNoteQuestionSeq, mmbrSeq |
| `getListQuestionBest` (select·443) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION | mmbrType |
| `getListStudy` (select·471) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION | mmbrSeq, offset, pageSize; include: inc_query |
| `getStudyView` (select·498) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION | mmbrNoteQuestionSeq, mmbrSeq |
| `getNoteShareView` (select·524) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION | mmbrNoteQuestionSeq, mmbrSeq |
| `getListStudyFile` (select·551) | TB_FILE | mmbrNoteQuestionSeq |
| `getWorngAnswerUnit` (select·556) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endDate, filterLessonSeq, lrnLessonSeq, lrnUnitSeq, mmbrSeq, sortType, startDate |
| `getListWorngAnswerLesson` (select·581) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endDate, filterLessonSeq, lrnUnitSeq, mmbrSeq, startDate |
| `getListWorngAnswerPage` (select·612) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endDate, lrnLessonSeq, mmbrSeq, startDate |
| `getListWorngAnswer` (select·674) | TB_CNTNT, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | lrnLessonSeq, mmbrLrnPageSeq |
| `getBasicTy` (select·697) | TB_MMBR_SCHEDULE | mmbrSeq |
| `setInsertStudyNoteScanBatch` (insert·702) | TB_BATCH_NOTE_SCAN | height, linkUrl, mmbrNoteQuestionSeq, mmbrSeq, width |
| `getAnswData` (select·728) | TB_FILE, TB_MMBR_NOTE_QUESTION | mmbrNoteQuestionSeq |
| `setUpdateNoteRead` (update·745) | TB_MMBR | mmbrSeq |
| `setInsertStudyGorup` (insert·749) | TB_MMBR_NOTE_QUESTION_GROUP | mmbrScheduleDtlSeq |
| `getStudyVocaReviewCnt` (select·760) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION, TB_MMBR_NOTE_QUESTION_GROUP | mmbrSeq; include: inc_query_study |
| `getStudyVocaReviewList` (select·781) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION, TB_MMBR_NOTE_QUESTION_GROUP | mmbrSeq, offset, pageSize; include: inc_query_study |
| `getStudyVocaReviewViewList` (select·811) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION | mmbrNoteQuestionGroupSeq, mmbrSeq |
| `getStudyVocaReviewViewShareList` (select·839) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION | mmbrNoteQuestionGroupSeq, mmbrSeq |
| `setDelStudy` (update·865) | TB_FILE, TB_MMBR_NOTE_QUESTION | mmbrNoteQuestionSeq, mmbrSeq |

## player/PlayerMapper.xml

원본: `src/main/resources/mapper/player/PlayerMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getModuleInfo` (select·8) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT | lrnLessonSeq, lrnModuleCd |
| `listLrnAct` (select·44) | TB_LRN_ACT | lrnLessonSeq |

## point/PointMapper.xml

원본: `src/main/resources/mapper/point/PointMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getPointCode` (select·8) | TB_POINT_CODE | code |
| `getWeekPointInfo` (select·22) | TB_MMBR_B2C, TB_MMBR_POINT_HST, TB_POINT_CODE | endDt, mmbrSeq, startDt |
| `callAttendPointReq` (select·34) | — | mmbrId |
| `setInsertPointMissionMmbr` (insert·38) | TB_POINT_MISSION_MMBR | endDt, endOrd, mmbrPointHstSeq, mmbrScheduleSeq, mmbrSeq, month, pointMissionSeq, rewardCompltYn, startDt, startOrd, week, weekCnt, year |
| `viewPointCodeInfo` (select·86) | TB_POINT_CODE, TB_POINT_MISSION | mgCode |
| `getPointMissionMmbr` (select·100) | TB_POINT_MISSION, TB_POINT_MISSION_MMBR | mgCode, mmbrSeq, month, week, year |
| `getListPointMissionMmbrCode` (select·117) | TB_POINT_MISSION, TB_POINT_MISSION_MMBR | mgCode, mmbrSeq |
| `getPointMissionMmbrWeekMonthCheck` (select·135) | TB_POINT_MISSION, TB_POINT_MISSION_MMBR | mmbrSeq |
| `addMmbrPointHistory` (insert·158) | TB_MMBR_POINT_HST | mgCode, mmbrSeq, point, pointRewardTy, reasonDetail |
| `mmbrUpdatePoint` (update·178) | TB_MMBR_B2C | mmbrSeq, point |

## report/MmbrRankMapper.xml

원본: `src/main/resources/mapper/report/MmbrRankMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `incViewMmbrRank` (sql·9) | — |  |
| `incViewMmbrRankWhere` (sql·31) | — | lrnLessonSeq, lrnUnitSeq, mmbrType, month, rankTy, week, year |
| `getListMmbrRank` (select·62) | TB_MMBR, TB_MMBR_RANK | limit, startNum; include: incViewMmbrRank, incViewMmbrRankWhere |
| `getListMmbrRankCnt` (select·74) | TB_MMBR, TB_MMBR_RANK | include: incViewMmbrRankWhere |
| `getMmbrRank` (select·84) | TB_MMBR, TB_MMBR_RANK | mmbrSeq; include: incViewMmbrRank, incViewMmbrRankWhere |
| `getMmbrSt` (select·96) | TB_MMBR_ST | stTy |

## report/MmbrReportMapper.xml

원본: `src/main/resources/mapper/report/MmbrReportMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `setInertMmbrReport` (insert·9) | TB_MMBR_REPORT | lrnLessonSeq, lrnUnitSeq, mmbrScheduleSeq, mmbrSeq, month, reportSubTy, reportTy, repotCntnt, repotTitle, week, year |
| `getMmbrReport` (select·46) | TB_MMBR_REPORT | lrnLessonSeq, lrnUnitSeq, mmbrSeq, month, reportTy, week, year |
| `setDeleteMmbrReport` (delete·78) | TB_MMBR_REPORT | lrnLessonSeq, lrnUnitSeq, mmbrSeq, month, reportTy, week, year |
| `getListMmbrReportInfo` (select·102) | TB_MMBR_REPORT | mmbrSeq, month, reportTy, year |
| `getSelfStudyCheck` (select·177) | TB_MMBR_SELF_STUDY | mmbrSeq, month, selfStudyTy, week, year |
| `getFirstReportCheck` (select·189) | TB_MMBR_REPORT | mmbrSeq, month, reportTy, week, year |

## schedule/MmbrScheduleMapper.xml

원본: `src/main/resources/mapper/schedule/MmbrScheduleMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `setInsertMmbrSchedule` (insert·9) | TB_MMBR_SCHEDULE, TB_SCHEDULE | levelOrder, levelWrite, mmbrSeq |
| `getMmbrSchedule` (select·39) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrSeq |
| `getMmbrScheduleInfo` (select·139) | TB_LRN_LESSON, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SCHEDULE_WEEK | mmbrScheduleSeq, mmbrSeq, month, week, year |
| `getMmbrScheduleDtl` (select·183) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | lessonTyCd, lrnUnitSeq, mmbrScheduleDtlSeq, mmbrScheduleSeq, mmbrSeq, scheduleOrd |
| `getMmbrScheduleDtlTwin` (select·233) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrScheduleDtlSeq, mmbrScheduleSeq, mmbrSeq |
| `getListMmbrScheduleDtlUptCheck` (select·266) | TB_LRN_LESSON, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_SCHEDULE_DTL | mmbrScheduleSeq, mmbrSeq |
| `setInsertMmbrScheduleDtlUptCheck` (insert·287) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_SCHEDULE_DTL | lrnLessonSeq, mmbrScheduleSeq, scheduleOrd |
| `setInsertMmbrScheduleDtl` (insert·350) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_SCHEDULE_DTL, TB_SCHEDULE, TB_SCHEDULE_DTL | mmbrScheduleSeq |
| `setInsertMmbrScheduleDtlDx` (insert·425) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_SCHEDULE_DTL | mmbrScheduleSeq, round |
| `setInsertMmbrScheduleDtlDxCopy` (insert·458) | TB_LRN_LESSON, TB_MMBR_SCHEDULE_DTL | mmbrScheduleSeq, preMmbrScheduleSeq |
| `setUpdMmbrScheduleDtlPageCnt` (update·513) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SCHEDULE_DTL | mmbrLrnSeq, mmbrSeq, scheduleStCd |
| `setUpdMmbrScheduleUseYn` (update·548) | TB_MMBR_SCHEDULE | mmbrScheduleSeq, mmbrSeq, useYn |
| `getMmbrScheduleDtlResult` (select·555) | TB_LRN_LESSON, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrScheduleDtlSeq, mmbrSeq |
| `getMmbrScheduleDtlLessonTyCd` (select·583) | TB_LRN_LESSON, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | lessonTyCd, lrnUnitSeq, mmbrScheduleSeq |
| `getMmbrScheduleDtlPageResult` (select·612) | TB_LRN_ACT, TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SCHEDULE_DTL | mmbrLrnPageSeq, mmbrSeq |
| `getListMmbrScheduleLessonWeekInfo` (select·649) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endWeekNum, mmbrScheduleSeq, startWeekNum |
| `getListMmbrScheduleLessonWeek` (select·678) | TB_FILE, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_POINT_CODE | endNum, mmbrScheduleSeq, startNum |
| `setUpdMmbrScheduleDtlResetInfo` (update·747) | TB_MMBR_SCHEDULE_DTL | mmbrScheduleSeq, preMmbrScheduleSeq |
| `setUpdMmbrScheduleDtlMmbrLrnSeq` (update·761) | TB_MMBR_SCHEDULE_DTL | mmbrLrnSeq, mmbrScheduleDtlSeq, round |
| `setUpdMmbrScheduleSetup` (update·771) | TB_LRN_LESSON, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | basicTy, mmbrScheduleSeq, weekCnt |
| `setUpdMmbrScheduleWeekSetup` (update·788) | TB_MMBR_SCHEDULE | mmbrScheduleSeq, nowWeekNum |
| `setUpdMmbrScheduleDtlTwin` (update·796) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrScheduleSeq, mmbrSeq |
| `setUpdMmbrScheduLevel` (update·844) | TB_MMBR_SCHEDULE | levelOrder, levelWrite, mmbrScheduleSeq, mmbrSeq |
| `setUpdMmbrScheduleDtl` (update·852) | TB_MMBR_LRN, TB_MMBR_SCHEDULE_DTL | mmbrLrnSeq, mmbrSeq, scheduleStCd |
| `setReset` (delete·862) | TB_MMBR, TB_MMBR_B2B, TB_MMBR_B2C | mmbrSeq |
| `setDeleteMmbrScheduleWait` (delete·918) | TB_MMBR_SCHEDULE_WAIT | mmbrSeq, month, waitTpCd, week, year |
| `setInsertMmbrScheduleWait` (insert·925) | TB_MMBR_SCHEDULE_WAIT | afterIntYn, mmbrScheduleSeq, mmbrSeq, month, nowScheduleOrd, useYn, waitTpCd, week, weekCnt, year |
| `getMmbrScheduleWait` (select·957) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SCHEDULE_WAIT | mmbrSeq, month, waitTpCd, week, year |
| `getMmbrScheduleDtlCnt` (select·990) | TB_LRN_LESSON, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | lrnUnitSeq, mmbrScheduleSeq, mmbrSeq |
| `getMmbrScheduleDtlIncompleteCnt` (select·1020) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endNum, lrnSeriesSeq, mmbrScheduleSeq, mmbrSeq, startNum |
| `getMmbrScheduleReportWeekIncompleteCnt` (select·1044) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SCHEDULE_WEEK | endDt, lrnSeriesSeq, mmbrSeq, startDt |
| `getMmbrScheduleDtlTimeTableIncompleteCnt` (select·1074) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endNum, mmbrScheduleSeq, mmbrSeq, startNum |
| `getMmbrScheduleDtlTimeTableIncompleteWeekCnt` (select·1095) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_POINT_MISSION_MMBR | mmbrScheduleSeq, mmbrSeq |
| `getMmbrScheduleDtlIncomplete` (select·1135) | TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endNum, mmbrScheduleSeq, mmbrSeq, startNum |
| `getMmbrScheduleChocoMainWeekApi` (select·1156) | TB_FILE, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_POINT_CODE | endNum, mmbrScheduleSeq, startNum |
| `setInsertMmbrScheduleWeek` (insert·1210) | TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_WEEK | endDt, endOrd, mmbrScheduleSeq, mmbrSeq, month, startDt, startOrd, week, weekNum, year, yearWeek |
| `getMmbrScheduleWeek` (select·1247) | TB_MMBR_SCHEDULE_WEEK | mmbrScheduleSeq, mmbrSeq, month, week, year |
| `getListMmbrScheduleWeek` (select·1271) | TB_MMBR_SCHEDULE_WEEK | endDt, mmbrSeq, startDt |
| `setUpdMmbrScheduleWeekStartNum` (update·1308) | TB_MMBR_SCHEDULE | mmbrScheduleSeq, mmbrSeq, weekStartNum |
| `setUpdMmbrScheduleOrdChangYn` (update·1315) | TB_MMBR_SCHEDULE | mmbrScheduleSeq, mmbrSeq, ordChangYn |
| `setInsertMmbrScheduleDtlData` (insert·1322) | TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SCHEDULE_DTL_DATA | actTyCd, mmbrScheduleDtlSeq |
| `setInsertMmbrScheduleHist` (insert·1373) | TB_MMBR_SCHEDULE_HIST | basicTy, changeDesc, changeType, levelOrder, levelWrite, mmbrScheduleSeq, mmbrSeq, regIp, regType, regUser, startNum, weekCnt |
| `setUpdMmbrScheduleWaitProcess` (update·1405) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SCHEDULE_WAIT | mmbrScheduleWaitSeq |
| `setUpdMmbrScheduleEndInitProcess` (update·1490) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrScheduleSeq |
| `setUpdMmbrScheduleDtlTwinAdd` (update·1523) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrScheduleDtlSeq, mmbrScheduleSeq |
| `setUpdMmbrScheduleDtlTwinSync` (update·1576) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrScheduleDtlSeq, mmbrScheduleSeq |

## schedule/MmbrSelfStudyMapper.xml

원본: `src/main/resources/mapper/schedule/MmbrSelfStudyMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListMmbrSelfStudy` (select·9) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT, TB_MMBR_SELF_STUDY, TB_MMBR_SELF_STUDY_DTL, TB_POINT_CODE | lrnModuleCd, mmbrSeq, pointCd, selfStudyTy |
| `getMmbrSelfStudy` (select·71) | TB_MMBR_SELF_STUDY | lrnModuleCd, mmbrSelfStudySeq, mmbrSeq |
| `getLrnLessonSelfStudy` (select·93) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SELF_STUDY | lrnLessonSeq, lrnModuleCd, mmbrLrnSeq, mmbrSeq |
| `setUpdMmbrSelfStudySt` (update·119) | TB_MMBR_SELF_STUDY | mmbrSelfStudySeq, mmbrSeq, scheduleStCd |
| `setUpdMmbrSelfStudyRound` (update·129) | TB_MMBR_SELF_STUDY | mmbrSelfStudySeq, mmbrSeq, round, scheduleStCd |
| `setInsertMmbrSelfStudy` (insert·140) | TB_MMBR_SELF_STUDY | lrnLessonSeq, lrnModuleCd, mmbrSeq, round, selfStudySubTy, selfStudyTy, title |
| `setUpdMmbrSelfStudylPageCnt` (update·170) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SELF_STUDY | mmbrLrnSeq, mmbrSeq |
| `setUpdMmbrSelfStudyMmbrLrnSeq` (update·191) | TB_MMBR_SELF_STUDY | lrnStCd, mmbrLrnSeq, mmbrSelfStudySeq |

## word/EngWordMapper.xml

원본: `src/main/resources/mapper/word/EngWordMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `inc_query` (sql·7) | — |  |
| `getMyEngWordList` (select·23) | TB_MMBR_ENG_WORD | mmbrSeq, offset, pageSize; include: inc_query |
| `getMyEngWordListCount` (select·40) | TB_MMBR_ENG_WORD | mmbrSeq |
| `myEngWordDibsDelete` (update·51) | TB_MMBR_ENG_WORD | id, mmbrSeq |
| `myEngWordDibsUpdate` (update·64) | TB_MMBR_ENG_WORD | mmbrEngSeq, mmbrSeq |
| `myEngWordDibsSave` (insert·73) | TB_MMBR_ENG_WORD | cefrLevel, mmbrSeq, partOfSpeach, wordEng, wordKor |
| `viewCount` (insert·98) | TB_MMBR_ENG_WORD_CNT | cefrLevel, meaning, partOfSpeach, word |
| `getEngWordUseYnCheck` (select·106) | TB_MMBR_ENG_WORD | mmbrSeq, word |
| `getEngDuplicate` (select·123) | TB_MMBR_ENG_WORD | mmbrSeq, wordEng |
