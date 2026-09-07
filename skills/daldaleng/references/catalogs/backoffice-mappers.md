# backoffice MyBatis 탐색 인덱스

기준 HEAD f9a8f570a1683e08d6f714aecc034b45996f278a. Working tree XML에서 추출. 태그/ID/테이블은 탐색 단서이며 SQL 본문과 include, caller를 읽어 의미를 확인한다. select 태그도 procedure 등 쓰기 효과를 포함할 수 있다. 테이블 목록은 TB_ 패턴 추출로 view/동적 이름/include의 전개 결과를 모두 포함하지 않는다.

## AdminMapper.xml

원본: `src/main/resources/mapper/AdminMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `listAdminWhere` (sql·9) | — | endDate, roleType, searchKeyword, startDate, useYn |
| `getListAdmin` (select·67) | TB_ADMIN | limit, offset; include: listAdminWhere |
| `getListAdminTotCnt` (select·90) | TB_ADMIN | include: listAdminWhere |
| `getAdmin` (select·100) | TB_ADMIN | adminSeq |
| `setAddAdmin` (insert·131) | TB_ADMIN | email, id, ip, name, password, phoneNumber, regUser, roleType, teamName, useYn |
| `setUpdAdmin` (update·172) | TB_ADMIN | adminSeq, email, name, phoneNumber, roleType, teamName, updIp, updUser, useYn |
| `setUpdAdminPassword` (update·208) | TB_ADMIN | adminSeq, email, id, ip, password, updUser |
| `setDelAdmin` (update·231) | TB_ADMIN | adminSeq, updUser |
| `setUpdAdminApproval` (update·242) | TB_ADMIN | adminSeq, approvalUser, ip, roleType |
| `getDuplicateCheck` (select·255) | TB_ADMIN | id |
| `getIdEmailCheck` (select·265) | TB_ADMIN | email, id |

## AdminMenuMapper.xml

원본: `src/main/resources/mapper/AdminMenuMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getAdminPermission` (select·16) | TB_ADMIN, TB_ADMIN_MENU, TB_ADMIN_MENU_PERM | adminSeq |
| `getLoginPermUrl` (select·43) | TB_ADMIN, TB_ADMIN_MENU, TB_ADMIN_MENU_PERM | adminSeq |
| `getListAdminMenu` (select·68) | TB_ADMIN_MENU, TB_ADMIN_MENU_PERM | adminSeq |
| `getListChildAdminMenu` (select·89) | TB_ADMIN_MENU, TB_ADMIN_MENU_PERM | adminMenuSeq, adminSeq |
| `setAddUpdAdminMenu` (insert·113) | TB_ADMIN_MENU_PERM | adminMenuSeq, adminSeq, editYn, viewYn |

## AlimTalkMapper.xml

원본: `src/main/resources/mapper/AlimTalkMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getAlimTalkTemplate` (select·9) | TB_CMM_CODE | code_val |
| `setAlimtalkInsertLog` (insert·17) | TB_ALIMTALK_LOG | mmbrSeq, month, resultCode, resultMsg, scheduleType, sendStatus, templateCode, toName, toPhone, week, year |

## BoardMapper.xml

원본: `src/main/resources/mapper/BoardMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `listBoardWhere` (sql·10) | — | boardType, cardType, endDate, searchKeyword, startDate, targetTyCd, useYn |
| `getListBoard` (select·78) | TB_BOARD, TB_CMM_CODE, TB_FILE | limit, offset; include: listBoardWhere |
| `getListBoardTotCnt` (select·123) | TB_BOARD | include: listBoardWhere |
| `getBoard` (select·134) | TB_ADMIN, TB_BOARD, TB_FILE | boardSeq, boardType |
| `getBoardUseYn` (select·192) | TB_BOARD | boardSeq, boardType, cardTy |
| `setAddBoard` (insert·211) | TB_BOARD | boardType, cardTy, contents, ip, linkUrl, newWindowYn, regTy, regUser, sortOrd, targetTyCd, title, usePeriodYn, useYn, viewEndDt, viewStartDt |
| `setUpdBoard` (update·252) | TB_BOARD | boardSeq, cardTy, contents, ip, linkUrl, newWindowYn, regTy, sortOrd, targetTyCd, title, updUser, usePeriodYn, useYn, viewEndDt, viewStartDt |
| `setUpdBoardUseYn` (update·301) | TB_BOARD | boardSeq, ip, updUser, useYn |
| `setUpdBoardSortOrd` (update·313) | TB_BOARD | boardSeq, ip, sortOrd, updUser |
| `setUpdBoardUnused` (update·326) | TB_BOARD | boardSeq, boardType, ip, updUser |
| `setDelBoard` (update·340) | TB_BOARD | boardSeq, ip, updUser |

## CmmCodeMapper.xml

원본: `src/main/resources/mapper/CmmCodeMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getCode` (select·10) | TB_CMM_CODE | codeGrp |

## CmsSyncMapper.xml

원본: `src/main/resources/mapper/CmsSyncMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getMaxVersionByContentSeq` (select·9) | TB_CNTNT | contentSeq |
| `insertTbCntnt` (insert·13) | TB_CNTNT | cntntLrnTy, contentName, contentSeq, contentStatus, contentType, contentUrl, difficulty, downloadYn, educourseCode, educourseName, educourseName1, educourseName2, educourseName3, educourseName4, fileName, questionType, resourceStatus, serviceEndDate, serviceStartDate, serviceYn, solveTime, source, updateResourceStatus, version, viewerType |
| `insertTbCntntVersion` (insert·75) | TB_CNTNT_VERSION | contentSeq, version |
| `updateTbCntnt` (update·91) | TB_CNTNT | cntntSeq, contentName, contentSeq, contentStatus, contentType, difficulty, educourseCode, educourseName, educourseName1, educourseName2, educourseName3, educourseName4, fileName, ip, questionType, solveTime, source, updUser, useVersion, version, versionHoldYn, viewerType |

## CntntMapper.xml

원본: `src/main/resources/mapper/CntntMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `listCntntWhere` (sql·27) | — | act, category, cntntLrnTy, endDate, lesson, packageSeq, searchKeyword, series, startDate, state, unit, useVersion |
| `listPopupCntntWhere` (sql·103) | — | actText, cntntLrnTy, lessonText, searchKeyword, seriesText, state, unitText |
| `getListCntnt` (select·171) | TB_CNTNT, TB_LRN_ACT, TB_LRN_ACT_DTL, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT | limit, offset; include: listCntntWhere |
| `getListCntntTotCnt` (select·224) | TB_CNTNT, TB_LRN_ACT, TB_LRN_ACT_DTL, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT | include: listCntntWhere |
| `getListCntntExcelDL` (select·251) | TB_CNTNT, TB_LRN_ACT, TB_LRN_ACT_DTL, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT | include: listCntntWhere |
| `getListPopupCntnt` (select·337) | TB_CNTNT | limit, offset; include: listPopupCntntWhere |
| `getListPopupCntntTotCnt` (select·376) | TB_CNTNT | include: listPopupCntntWhere |
| `getViewCntntInfo` (select·390) | TB_ADMIN, TB_CNTNT | cntntSeq, contentSeq |
| `setAddCntnt` (insert·442) | TB_CNTNT | cntntLrnTy, contentName, contentSeq, contentStatus, contentType, contentUrl, downloadYn, educourseCode, educourseName, fileName, regUser, resourceStatus, serviceEndDate, serviceStartDate, serviceYn, source, updateResourceStatus, version, viewerType |
| `setUpdCntnt` (update·495) | TB_CNTNT | cntntLrnTy, cntntSeq, contentName, contentStatus, contentType, ip, source, updUser, useVersion, version, versionHoldYn, viewerType |
| `setAddCntntDtl` (insert·544) | TB_CNTNT_DTL | cntntDtlSeq, cntntSeq, contentKey, contentSeq, contentValue, extension, fileName, order, resolution, transYn |
| `setAddCntntKeyword` (insert·583) | TB_CNTNT_KEYWORD | cntntSeq, keyword |
| `setAddCntntTwinQuestion` (insert·596) | TB_CNTNT_TWIN_QUESTION | cntntSeq, relContentSeq |
| `setDelCntnt` (update·609) | TB_Cntnt | cntntSeq, updUser |
| `getListCntntDtl` (select·620) | TB_CNTNT_DTL | cntntSeq |
| `getListCntntKeyword` (select·637) | TB_CNTNT_KEYWORD | cntntSeq |
| `getListCntntTwinQuestion` (select·646) | TB_CNTNT_TWIN_QUESTION | cntntSeq |
| `getListEducourse` (select·654) | TB_CNTNT | educourseName |

## ExcelUploadMapper.xml

원본: `src/main/resources/mapper/ExcelUploadMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getLrnLesson` (select·8) | TB_LRN_LESSON | currCode |
| `getLrnAct` (select·20) | TB_LRN_ACT | currCode |
| `getLrnActDtlCheck` (select·30) | TB_CNTNT, TB_LRN_ACT_DTL | contentSeq, lrnActDtlSeq, lrnActSeq |
| `getCntntCheck` (select·44) | TB_CNTNT | contentSeq |
| `getCntntInfo` (select·55) | TB_CNTNT | contentSeq |
| `getScheduleCheck` (select·67) | TB_SCHEDULE_DTL | lrnLessonSeq, scheduleDtlSeq, scheduleSeq |

## FileMapper.xml

원본: `src/main/resources/mapper/FileMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `setInsertFile` (insert·9) | TB_FILE | fileExt, fileOrigNm, filePath, fileSize, refSeq, refTable, refType, regUser |
| `getListFile` (select·37) | TB_FILE, tb_mmbr_note_question, tb_mmbr_note_study | refSeq, refTable, refType |
| `getFile` (select·69) | TB_FILE | fileSeq |
| `setDelFile` (update·85) | TB_FILE | fileSeq, updUser |

## LoginMapper.xml

원본: `src/main/resources/mapper/LoginMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getLoginAdminInfo` (select·10) | TB_ADMIN | id |
| `setUpdateFailCnt` (update·29) | TB_ADMIN | id |
| `setUpdateLoginSuccess` (update·38) | TB_ADMIN | id |

## LrnActMapper.xml

원본: `src/main/resources/mapper/LrnActMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getLessonActInfo` (select·29) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT | lrnLessonSeq, lrnSeriesSeq, lrnUnitSeq |
| `getListLrnAct` (select·54) | TB_CMM_CODE, TB_LRN_ACT | lrnLessonSeq |
| `getListLrnActDtl` (select·74) | TB_CNTNT, TB_LRN_ACT_DTL | lrnActSeq |
| `getLrnActDtlCount` (select·91) | TB_CNTNT, TB_LRN_ACT_DTL | lrnActSeq |
| `getLrnActDtl` (select·102) | TB_LRN_ACT, TB_LRN_ACT_DTL, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT | cntntSeq |
| `getLrnAct` (select·127) | TB_ADMIN, TB_LRN_ACT, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT | lrnActSeq |
| `setUpdLrnLession` (update·166) | TB_LRN_LESSON | lrnLessonSeq, moduleCd, publicYn, updUser, useYn |
| `setUpdLrnAct` (update·190) | TB_LRN_ACT, TB_LRN_LESSON | actCurrCode, actName, actOrd, actTyCd, examFileSeq, lrnActSeq, lrnLessonSeq, updUser, useYn |
| `setDeleteLrnActDtl` (delete·226) | TB_LRN_ACT_DTL | lrnActSeq |
| `setDelLrnAct` (update·231) | TB_LRN_ACT | ip, lrnActSeq, updUser |
| `setAddLrnAct` (insert·244) | TB_LRN_ACT | actName, actOrd, actTyCd, ip, lrnLessonSeq, lrnPackageSeq, regUser |
| `setAddLrnActDtl` (insert·267) | TB_LRN_ACT_DTL | cntntId, contentNum, contentQstTy, dtlOrd, lrnActSeq, regUser |
| `setUpdLrnActDtl` (update·290) | TB_LRN_ACT_DTL | cntntId, dtlOrd, lrnActDtlSeq, updUser |
| `setDeleteUpdLrnActDtl` (update·303) | TB_LRN_ACT_DTL | lrnActDtlSeq |

## LrnCateMapper.xml

원본: `src/main/resources/mapper/LrnCateMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListCategory` (select·10) | TB_LRN_CATEGORY | lrnPackageSeq |
| `getListSeries` (select·28) | TB_LRN_SERIES | lrnPackageSeq |
| `getListUnit` (select·44) | TB_LRN_UNIT | lrnPackageSeq |
| `getListLesson` (select·61) | TB_LRN_LESSON | lrnPackageSeq |
| `getListAct` (select·77) | TB_LRN_ACT | lrnPackageSeq |
| `getListCurrExcelDL` (select·95) | TB_LRN_ACT, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT | lrnPackageSeq |

## LrnCategoryMapper.xml

원본: `src/main/resources/mapper/LrnCategoryMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getLrnCategory` (select·10) | TB_ADMIN, TB_LRN_CATEGORY | lrnCategorySeq |
| `setUpdLrnCategory` (update·28) | TB_LRN_CATEGORY | categoryName, currCode, lrnCategorySeq, sortOrd, updUser |
| `setAddLrnCategory` (insert·52) | TB_LRN_CATEGORY | categoryName, lrnPackageSeq, regIp, regUser, sortOrd |

## LrnLessonMapper.xml

원본: `src/main/resources/mapper/LrnLessonMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `listLessonWhere` (sql·16) | — | endDate, lrnCategorySeq, lrnPackageSeq, lrnSeriesSeq, lrnUnitSeq, searchKeyword, startDate, useYn |
| `getListLessonExcelDL` (select·86) | TB_CNTNT, TB_LRN_ACT, TB_LRN_ACT_DTL, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_PACKAGE, TB_LRN_SERIES, TB_LRN_UNIT | include: listLessonWhere |
| `getListLesson` (select·130) | TB_LRN_ACT, TB_LRN_ACT_DTL, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_PACKAGE, TB_LRN_SERIES, TB_LRN_UNIT | limit, offset; include: listLessonWhere |
| `getListLessonTotCnt` (select·177) | TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_PACKAGE, TB_LRN_SERIES, TB_LRN_UNIT | include: listLessonWhere |
| `getLrnLesson` (select·197) | TB_ADMIN, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT | lrnLessonSeq |
| `setUpdLrnLesson` (update·242) | TB_LRN_LESSON, TB_LRN_UNIT | colorCode, imgFileSeq, ip, lessonCurrCode, lessonName, lessonOrd, lessonTyCd, lrnLessonSeq, lrnUnitSeq, updUser, useYn |
| `setUpdLrnLessonUpdDt` (update·283) | TB_LRN_LESSON | ip, lessonCode, updUser |
| `setUpdLrnLessonFileSeq` (update·295) | TB_LRN_LESSON | imgFileSeq, lrnLessonSeq |
| `setDelLrnLesson` (update·305) | TB_LRN_LESSON | ip, lrnLessonSeq, updUser |
| `setAddLrnLesson` (insert·318) | TB_LRN_LESSON | colorCode, ip, lessonName, lessonOrd, lessonTyCd, lrnModuleCd, lrnPackageSeq, lrnUnitSeq, regUser, useYn |
| `getDelLrnLessonCheckCount` (select·347) | TB_SCHEDULE, TB_SCHEDULE_DTL | lrnLessonSeq |
| `getLrnActCount` (select·368) | TB_LRN_ACT | lrnLessonSeq |
| `getLrnActDtlCount` (select·378) | TB_LRN_ACT, TB_LRN_ACT_DTL | lrnLessonSeq |

## LrnSeriesMapper.xml

원본: `src/main/resources/mapper/LrnSeriesMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getLrnSeries` (select·9) | TB_ADMIN, TB_LRN_CATEGORY, TB_LRN_SERIES | lrnSeriesSeq |
| `setUpdLrnSeries` (update·34) | TB_LRN_SERIES | colorCode, lrnSeriesSeq, seriesName, sortOrd, updUser |
| `setAddLrnSeries` (insert·58) | TB_LRN_SERIES | colorCode, lrnCategorySeq, lrnPackageSeq, seriesCd, seriesName, seriesSeq, sortOrd |

## LrnUnitMapper.xml

원본: `src/main/resources/mapper/LrnUnitMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getLrnUnit` (select·9) | TB_ADMIN, TB_LRN_CATEGORY, TB_LRN_SERIES, TB_LRN_UNIT | lrnUnitSeq |
| `setUpdLrnUnit` (update·39) | TB_LRN_SERIES, TB_LRN_UNIT | cardFileSeq, colorCode, lrnSeriesSeq, lrnUnitSeq, unitCrrCode, unitName, unitOrd, updUser |
| `setAddLrnUnit` (insert·68) | TB_LRN_UNIT | colorCode, ip, lrnPackageSeq, lrnSeriesSeq, regUser, unitName, unitOrd |
| `getDelLrnUnitCheckCount` (select·91) | TB_LRN_LESSON | lrnUnitSeq |
| `setDelLrnUnit` (update·102) | TB_LRN_UNIT | ip, lrnUnitSeq, updUser |
| `getLrnUnitCurrCode` (select·117) | TB_LRN_UNIT | currCode |

## MmbrLrnAvgMapper.xml

원본: `src/main/resources/mapper/MmbrLrnAvgMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getMmbrScheduleDtlIncompleteCnt` (select·7) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endNum, mmbrScheduleSeq, mmbrSeq, startNum |
| `getWeekReport` (select·28) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | classSeq, teacherSeq |
| `getMonthReport` (select·84) | TB_LRN_LESSON, TB_MMBR_B2B, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | classSeq, teacherSeq |

## MmbrLrnMapper.xml

원본: `src/main/resources/mapper/MmbrLrnMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `listMmbrLrnWhere` (sql·43) | — | endDate, lrnActSeq, lrnLessonSeq, lrnSeriesSeq, lrnUnitSeq, mmbrSeq, round, startDate |
| `getListMmbrLrn` (select·128) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SELF_STUDY | limit, offset; include: listMmbrLrnWhere |
| `getListMmbrLrnTotCnt` (select·162) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SELF_STUDY | include: listMmbrLrnWhere |
| `getListMmbrLrnWrong` (select·180) | TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_WRONG, TB_MMBR_LRN_WRONG_CNTNT | limit, offset; include: listMmbrLrnWhere |
| `getListMmbrLrnWrongTotCnt` (select·220) | TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_WRONG, TB_MMBR_LRN_WRONG_CNTNT | include: listMmbrLrnWhere |
| `getListMmbrLrnPage` (select·251) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SELF_STUDY | mmbrLrnSeq |
| `getMmbrLrn` (select·282) | TB_MMBR_LRN | mmbrLrnSeq, mmbrSeq |
| `getListMmbrLrnPageInfo` (select·298) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SELF_STUDY | lrnActSeq, lrnModuleCd, mmbrLrnPageSeq, mmbrScheduleDtlSeq, mmbrSelfStudySeq, mmbrSeq |
| `getListMmbrLrnPageCntnt` (select·356) | TB_CNTNT, TB_MMBR_LRN_PAGE_CNTNT | mmbrLrnPageSeq |
| `getListMmbrLrnWrongInfo` (select·380) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_LRN_WRONG | mmbrLrnWrongSeq, mmbrSeq |
| `getListMmbrLrnWrongCntnt` (select·413) | TB_CNTNT, TB_MMBR_LRN_WRONG_CNTNT | mmbrLrnWrongSeq |

## MmbrMapper.xml

원본: `src/main/resources/mapper/MmbrMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `lastLoginDtWhere` (sql·16) | — | endDate, startDate |
| `listB2bMemberWhere` (sql·25) | — | agcyType, endDate, gradeCode, prodCode, prodNm, searchKeyword, startDate |
| `listB2cMemberWhere` (sql·101) | — | endDate, gradeCode, prodCode, prodNm, searchKeyword, startDate |
| `getListB2bMember` (select·160) | TB_MMBR, TB_MMBR_AGENCYS, TB_MMBR_B2B, TB_MMBR_LOGIN_HST, TB_MMBR_PROD | limit, offset; include: listB2bMemberWhere, lastLoginDtWhere |
| `getListB2bMemberTotCnt` (select·197) | TB_MMBR, TB_MMBR_AGENCYS, TB_MMBR_B2B, TB_MMBR_PROD | include: listB2bMemberWhere |
| `getListB2bMemberExcelDL` (select·211) | TB_MMBR, TB_MMBR_AGENCYS, TB_MMBR_B2B, TB_MMBR_LOGIN_HST, TB_MMBR_PROD | include: listB2bMemberWhere, lastLoginDtWhere |
| `getListB2cMember` (select·247) | TB_MMBR, TB_MMBR_B2C, TB_MMBR_LOGIN_HST, TB_MMBR_PROD | limit, offset; include: listB2cMemberWhere, lastLoginDtWhere |
| `getListB2cMemberTotCnt` (select·278) | TB_MMBR, TB_MMBR_B2C, TB_MMBR_LOGIN_HST, TB_MMBR_PROD | include: listB2cMemberWhere, lastLoginDtWhere |
| `getListB2cMemberExcelDL` (select·297) | TB_MMBR, TB_MMBR_B2C, TB_MMBR_LOGIN_HST, TB_MMBR_PROD | include: listB2cMemberWhere, lastLoginDtWhere |
| `getB2cMember` (select·331) | TB_MMBR, TB_MMBR_B2C, TB_MMBR_LOGIN_HST, TB_MMBR_PROD | mmbrSeq |
| `getB2bMember` (select·367) | TB_MMBR, TB_MMBR_AGENCYS, TB_MMBR_B2B, TB_MMBR_LOGIN_HST, TB_MMBR_PROD | mmbrSeq |
| `getListMmbrLoginHst` (select·410) | TB_MMBR_LOGIN_HST | mmbrSeq |
| `getListMmbrAttendance` (select·424) | TB_MMBR, TB_MMBR_LOGIN_HST | limit, loginDate, offset |
| `getListMmbrAttendanceTotCnt` (select·439) | TB_MMBR, TB_MMBR_LOGIN_HST | loginDate |
| `getB2bClassMmbr` (select·451) | TB_LRN_LESSON, TB_MMBR, TB_MMBR_B2B, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | classSeq |
| `getMmbrWeekLrnInfo` (select·486) | TB_LRN_LESSON, TB_MMBR, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrSeq |
| `setMmbrAnswYn` (update·519) | TB_MMBR | mmbrSeq |
| `getMemberToken` (select·525) | TB_MMBR | mmbrSeq |
| `getMemberType` (select·533) | TB_MMBR | mmbrSeq |

## MmbrNoteQuestionBestMapper.xml

원본: `src/main/resources/mapper/MmbrNoteQuestionBestMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getMmbrNoteQuestionBest` (select·9) | TB_MMBR_NOTE_QUESTION_BEST | mmbrNoteQuestionSeq |
| `getMmbrNoteQuestionBestCheck` (select·25) | TB_MMBR_NOTE_QUESTION, TB_MMBR_NOTE_QUESTION_BEST | bestOrd, mmbrType |
| `setUpdMmbrNoteQuestionBest` (update·42) | TB_MMBR_NOTE_QUESTION_BEST | mmbrNoteQuestionBestSeq, mmbrNoteQuestionSeq |
| `setMmbrNoteQuestionBest` (insert·52) | TB_MMBR_NOTE_QUESTION_BEST | bestOrd, ip, mmbrNoteQuestionSeq, mmbrType, regUser |

## MmbrNoteQuestionMapper.xml

원본: `src/main/resources/mapper/MmbrNoteQuestionMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `listMmbrNoteQuestionWhere` (sql·19) | TB_MMBR_NOTE_QUESTION_BEST | answYn, endDate, lrnActSeq, lrnCategorySeq, lrnLessonSeq, lrnSeriesSeq, lrnUnitSeq, mmbrSeq, mmbrType, noteType, publicYn, searchKeyword, startDate |
| `getListMmbrNoteQuestion` (select·139) | TB_ADMIN, TB_FILE, TB_LRN_ACT, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_PACKAGE, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION, TB_MMBR_NOTE_QUESTION_BEST, tb_mmbr_note_question | limit, offset; include: listMmbrNoteQuestionWhere |
| `getListMmbrNoteQuestionTotCnt` (select·202) | TB_ADMIN, TB_FILE, TB_LRN_ACT, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_PACKAGE, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_NOTE_QUESTION, TB_MMBR_NOTE_QUESTION_BEST, tb_mmbr_note_question | include: listMmbrNoteQuestionWhere |
| `getListMmbrNoteStudy` (select·229) | TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_PACKAGE, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_NOTE_QUESTION | limit, offset; include: listMmbrNoteQuestionWhere |
| `getListMmbrNoteStudyTotCnt` (select·262) | TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_PACKAGE, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_NOTE_QUESTION | include: listMmbrNoteQuestionWhere |
| `getMmbrNoteQuestion` (select·279) | TB_ADMIN, TB_CNTNT, TB_FILE, TB_LRN_ACT, TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_PACKAGE, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR, TB_MMBR_AGENCYS, TB_MMBR_B2B, TB_MMBR_B2C, TB_MMBR_LOGIN_HST, TB_MMBR_NOTE_QUESTION, TB_MMBR_NOTE_QUESTION_BEST, tb_mmbr_note_question | mmbrNoteQuestionSeq |
| `setUpdMmbrNoteQuestion` (update·380) | TB_MMBR_NOTE_QUESTION | answContent, answTitle, bestOrd, ip, mmbrNoteQuestionSeq, publicYn, updUser |
| `setUpdMmbrNoteQuestionAnsw` (update·414) | TB_MMBR_NOTE_QUESTION | answContent, answTitle, mmbrNoteQuestionSeq, updUser |
| `setUpdMmbrNoteQuestionBestCancel` (update·435) | TB_MMBR_NOTE_QUESTION | mmbrNoteQuestionSeq |

## MmbrPointHstMapper.xml

원본: `src/main/resources/mapper/MmbrPointHstMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `listMmbrPointHstWhere` (sql·9) | — | endDate, mmbrSeq, pointGrpTy, pointRewardTy, searchKeyword, startDate |
| `getListMmbrPointHst` (select·61) | TB_CMM_CODE, TB_MMBR_B2C, TB_MMBR_POINT_HST, TB_POINT_CODE | limit, offset; include: listMmbrPointHstWhere |
| `getListMmbrPointHstTotCnt` (select·97) | TB_MMBR_B2C, TB_MMBR_POINT_HST, TB_POINT_CODE | include: listMmbrPointHstWhere |
| `getMmbrPointHst` (select·110) | TB_CMM_CODE, TB_MMBR, TB_MMBR_B2C, TB_MMBR_POINT_HST, TB_POINT_CODE | mmbrPointHstSeq |
| `setAddMmbrPointHst` (insert·146) | TB_MMBR_POINT_HST | code, mmbrSeq, point, pointRewardTy, reason |
| `getListMmbrPointHstExcelDL` (select·168) | TB_CMM_CODE, TB_MMBR_B2C, TB_MMBR_POINT_HST, TB_POINT_CODE | include: listMmbrPointHstWhere |

## MmbrProdGrpMapper.xml

원본: `src/main/resources/mapper/MmbrProdGrpMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListMmbrProdGrp` (select·9) | TB_MMBR_PROD_GRP | mmbrType |
| `getMmbrProdGrp` (select·21) | TB_MMBR_PROD_GRP | mmbrProdGrpSeq |

## MmbrScheduleMapper.xml

원본: `src/main/resources/mapper/MmbrScheduleMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListWeekMmbrLrn` (select·10) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL, TB_MMBR_SELF_STUDY | endNum, mmbrSeq, startNum |
| `getListMmbrScheduleWeekInfo` (select·41) | TB_LRN_LESSON, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endNum, mmbrSeq, startNum |
| `getMmbrScheduleInfo` (select·66) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrSeq |
| `getMmbrScheduleDtlIncompleteCnt` (select·98) | TB_LRN_LESSON, TB_MMBR_LRN, TB_MMBR_LRN_PAGE, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | endNum, mmbrScheduleSeq, startNum |
| `getListMmbrScheduleDtl` (select·136) | TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_MMBR_LRN, TB_MMBR_SCHEDULE, TB_MMBR_SCHEDULE_DTL | mmbrSeq |
| `getListMmbrScheduleHist` (select·210) | TB_ADMIN, TB_MMBR_SCHEDULE_HIST | mmbrSeq |
| `getMmbrScheduleDiag` (select·234) | TB_MMBR_LRN, TB_MMBR_LRN_PAGE | mmbrSeq |
| `getMmbrScheduleWait` (select·252) | TB_MMBR_SCHEDULE_WAIT | mmbrSeq, waitTpCd |

## PointCodeMapper.xml

원본: `src/main/resources/mapper/PointCodeMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `listPointCodeWhere` (sql·9) | — | endDate, pointGrpTy, searchKeyword, startDate, useYn |
| `getListPointCode` (select·37) | TB_CMM_CODE, TB_POINT_CODE | limit, offset; include: listPointCodeWhere |
| `getListPointCodeTotCnt` (select·61) | TB_POINT_CODE | include: listPointCodeWhere |
| `getPointCode` (select·72) | TB_ADMIN, TB_CMM_CODE, TB_POINT_CODE | code |
| `setUpdPointCode` (update·98) | TB_POINT_CODE | code, ip, updUser, useYn |

## PointMissionMapper.xml

원본: `src/main/resources/mapper/PointMissionMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `listPointMissionWhere` (sql·9) | — | endDate, rewardTy, searchKeyword, startDate, useYn |
| `getListPointMission` (select·86) | TB_CMM_CODE, TB_POINT_CODE, TB_POINT_MISSION | limit, offset; include: listPointMissionWhere |
| `getListPointMissionTotCnt` (select·128) | TB_POINT_CODE, TB_POINT_MISSION | include: listPointMissionWhere |
| `getPointMission` (select·140) | TB_ADMIN, TB_CMM_CODE, TB_POINT_CODE, TB_POINT_MISSION | pointMissionSeq |
| `getPointMissionCode` (select·182) | TB_POINT_CODE, TB_POINT_MISSION | missionCode |
| `setAddPointMission` (insert·200) | TB_POINT_MISSION | cntnt, code, endDate, pointMissionNm, regUser, rewardCompltYn, rewardPoint, rewardProd, rewardTy, startDate, useYn |
| `setUpdPointMission` (update·233) | TB_POINT_MISSION | cntnt, endDate, ip, pointMissionNm, pointMissionSeq, rewardCompltYn, rewardProd, startDate, updUser, useYn |
| `setUpdPointMissionCompltYn` (update·262) | TB_POINT_MISSION | pointMissionSeq |

## PointMissionMmbrMapper.xml

원본: `src/main/resources/mapper/PointMissionMmbrMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListPointMissionMmbr` (select·9) | TB_ADMIN, TB_MMBR, TB_MMBR_B2C, TB_POINT_MISSION_MMBR | limit, offset, pointMissionSeq, rewardCompltYn, searchKeyword |
| `getListPointMissionMmbrTotCnt` (select·42) | TB_ADMIN, TB_MMBR, TB_MMBR_B2C, TB_POINT_MISSION_MMBR | pointMissionSeq, rewardCompltYn, searchKeyword |
| `getListPointMissionMmbrExcelDL` (select·64) | TB_ADMIN, TB_MMBR, TB_MMBR_B2C, TB_POINT_MISSION_MMBR | pointMissionSeq, rewardCompltYn, searchKeyword |
| `getPointMissionMmbrComplt` (select·94) | TB_MMBR, TB_POINT_MISSION, TB_POINT_MISSION_MMBR | pointMissionMmbrSeq |
| `getPointMissionMmbrMultiComplt` (select·113) | TB_MMBR, TB_POINT_MISSION_MMBR | seq |
| `setUpdPointMissionMmbrComplt` (update·140) | TB_POINT_MISSION_MMBR | ip, mmbrPointHstSeq, pointMissionMmbrSeq, updUser |
| `setAddPointMissionMmbrComplt` (insert·158) | TB_POINT_MISSION_MMBR | ip, mmbrPointHstSeq, mmbrSeq, pointMissionSeq, regUser |

## QuoteMapper.xml

원본: `src/main/resources/mapper/QuoteMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListQuote` (select·10) | TB_QUOTE |  |
| `getListQuoteTotCnt` (select·22) | TB_QUOTE |  |
| `setDelQuote` (update·31) | TB_QUOTE | ip, quoteSeq, updUser |
| `setAddQuote` (insert·44) | TB_QUOTE | content, description, ip, regUser |

## ScheduleDtlMapper.xml

원본: `src/main/resources/mapper/ScheduleDtlMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListScheduleDtlExcelDL` (select·10) | TB_LRN_CATEGORY, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_SCHEDULE_DTL | scheduleSeq |
| `getListScheduleDtl` (select·42) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_SCHEDULE_DTL | scheduleSeq |
| `getDiagScheduleDtl` (select·68) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT | diagLrnLessonSeq |
| `setCopyScheduleDtl` (insert·89) | TB_SCHEDULE_DTL | copyScheduleSeq, regUser, scheduleSeq |
| `setAddScheduleDtl` (insert·109) | TB_SCHEDULE_DTL | lrnLessonSeq, regUser, scheduleOrd, scheduleSeq |
| `setUpdScheduleDtl` (update·126) | TB_SCHEDULE_DTL | lrnLessonSeq, scheduleDtlSeq, scheduleOrd, scheduleSeq, updUser |
| `setDelAllScheduleDtl` (update·140) | TB_SCHEDULE_DTL | scheduleSeq, updUser |
| `setDelScheduleDtl` (update·152) | TB_SCHEDULE_DTL | scheduleDtlSeq, updUser |

## ScheduleMapper.xml

원본: `src/main/resources/mapper/ScheduleMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `listScheduleWhere` (sql·19) | — | searchKeyword, useYn |
| `getListSchedule` (select·36) | TB_LRN_CATEGORY, TB_SCHEDULE | limit, offset; include: listScheduleWhere |
| `getListScheduleTotCnt` (select·58) | TB_LRN_CATEGORY, TB_SCHEDULE | include: listScheduleWhere |
| `getViewSchedule` (select·70) | TB_ADMIN, TB_LRN_CATEGORY, TB_SCHEDULE | scheduleSeq |
| `getScheduleUsedCount` (select·96) | TB_LRN_CATEGORY, TB_SCHEDULE | scheduleSeq |
| `getViewScheduleLrnCate` (select·111) | TB_LRN_CATEGORY | lrnCategorySeq |
| `setAddSchedule` (insert·124) | TB_SCHEDULE | diagLrnLessonSeq, ip, lrnCategorySeq, regUser, scheduleName, useYn |
| `setCopySchedule` (insert·147) | TB_SCHEDULE | ip, regUser, scheduleSeq |
| `setUpdSchedule` (update·172) | TB_SCHEDULE | diagLrnLessonSeq, ip, scheduleName, scheduleSeq, updUser, useYn |
| `setUpdScheduleUnused` (update·197) | TB_SCHEDULE | ip, scheduleSeq, updUser |
| `setDelSchedule` (update·210) | TB_SCHEDULE | scheduleSeq, updUser |

## StatLrnMapper.xml

원본: `src/main/resources/mapper/StatLrnMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListStatLrn` (select·9) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_STAT_LRN | lrnCategorySeq, lrnLessonSeq, lrnSeriesSeq, lrnUnitSeq, statDt, statTy |
| `getListStatLrnSelfStudy` (select·57) | TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_STAT_LRN | statDt |
| `getListStatNote` (select·85) | TB_LRN_ACT, TB_LRN_LESSON, TB_LRN_SERIES, TB_LRN_UNIT, TB_STAT_NOTE | statDt |
| `getListStatEngWord` (select·111) | TB_MMBR_ENG_WORD, TB_MMBR_ENG_WORD_CNT |  |
| `getDateInfo` (select·131) | TB_STAT_LRN | statTy |
| `getWeeklyDashboard` (select·149) | TB_STAT_LRN | statDt |
| `getSupplementaryDashboard` (select·165) | TB_STAT_NOTE | statDt |

## StatPointMapper.xml

원본: `src/main/resources/mapper/StatPointMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListStatPoint` (select·9) | TB_CMM_CODE, TB_POINT_CODE, TB_STAT_POINT | statDt |
| `getDateInfo` (select·35) | TB_STAT_POINT |  |

## StatUsageMapper.xml

원본: `src/main/resources/mapper/StatUsageMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListService` (select·9) | TB_STAT_USAGE | endDate, grade, mmbrType, startDate |
| `getYearMonthlyActiveUserStat` (select·42) | TB_STAT_USAGE |  |
| `getStatUsagePrevDay` (select·62) | TB_STAT_USAGE |  |

## StatisticsMapper.xml

원본: `src/main/resources/mapper/StatisticsMapper.xml`

| ID (태그·줄) | 직접 나타난 테이블 | 바인딩 입력 / include |
|---|---|---|
| `getListService` (select·11) | TB_STAT_USAGE | endDate, startDate |
| `getListServiceTotCnt` (select·35) | TB_BOARD | boardSeq |
