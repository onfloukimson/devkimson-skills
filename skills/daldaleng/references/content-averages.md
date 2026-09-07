# 콘텐츠 확장·평균 데이터·쌍둥이: 운영 #198

projectId 4271874883715387917 / postId 4412581622138809017.
이 티켓은 소스에 평균 batch가 있는데 신규 콘텐츠 평균이 0으로 보이는 이유를 추적할 때 가장 먼저 읽을 근거다.

## 2026-09-07 확인한 댓글의 의미

- 9/3: 과거 학습 표본이 부족해 **기초 진단 평가만 집계하도록 DB 이벤트 조건을 제한**했다는 이력 설명. 여러 job이 있는 배치 서버 배포 대신 DB 이벤트로 운용했다는 배경.
- 9/4: 진단 외 평균 데이터의 적합성을 확인하고 운영 batch의 scheduleModuleAvgJob으로 옮기는 방향 검토.
- 9/4: 초기 기본값은 평균 점수 60점, 문항당 평균 시간 2분이었다는 운영 설명. 기존 학습은 실제 평균으로, 앞으로 신규 콘텐츠도 수동 변경 없이 집계되도록 요청.
- 9/4: 뒤늦게 등록된 쌍둥이 수업의 연결 누락을 응답 시 보정하는 수정이 검증계 반영됐고 9/9 전 추가 재현/검토 예정이라는 댓글.

**요청·검토 단계와 적용 완료를 구분한다.** DB 이벤트 정의/활성 상태를 직접 조회하지 않았고, scheduleModuleAvgJob의 운영 등록/기존 이벤트 중단 완료를 확인하지 않았다. 60점/2분은 과거 기본값 설명이며 모든 모듈의 현재 강제 정책이 아니다.

## 현재 batch 소스

process/ModuleAvgService.avgProcess:
1. ModuleAvgMapper.avgReset으로 TB_LRN_AVG의 USE_YN=Y 행을 전부 N으로 변경.
2. getAvgList로 활동별 평균 후보 조회.
3. processInsert로 TB_LRN_AVG insert 및 TB_LRN_ACT.USR_AVG_SCORE/USR_AVG_ELAPSED_TIME update.
4. 개별 실패는 JobFailMapper에 남기는 경로; 상위 catch는 오류 로그 후 반환.

getAvgList의 실제 조건:
- MC001 OR (MC002/MC003 AND ACT_TY_CD IN(P03,P05)). MC001에는 활동 유형 제한이 없다.
- P.CNTNT_PAGE_TY=Q, P.MARK_YN=Y, P.LRN_ST_CD=S, A.DEL_YN=N
- LRN_ACT_SEQ별 SCORE/ELAPSED_TIME 합계÷건수를 정수 변환
- inner join이므로 학습 페이지가 0건인 활동은 결과가 없다. COUNT(*)=0 fallback 식이 있어도 그런 group이 생성되지는 않는다.
- 이 SELECT에는 학습 ROUND=1, lesson USE_YN/DEL_YN, 기간 범위 조건이 직접 없다. 다른 ranking의 조건을 이미 공유한다고 가정하지 않는다.

전체 reset 후 부분 insert 구조이고 확인한 service에 전체 작업을 감싸는 @Transactional이 없다. 후보 0건이면 그대로 반환하므로 TB_LRN_AVG 활성 행은 꺼지지만 TB_LRN_ACT.USR_AVG_*는 이전 값이 남는다. 부분 실패에서도 두 저장 위치가 다른 상태가 될 수 있다. 평균 0 문제를 확인하려고 수동 실행하면 기존 유효 평균을 비활성화할 수 있다. 단순 조회 도구로 안내하지 않는다.
인덱스 [batch ModuleAvgMapper](catalogs/batch-mappers.md)와 원본 caller를 읽고 집계 대상/활성 전환/실패 복구를 검토한다.

## 평균을 소비하는 코드

API MmbrLrnMapper는 USR_AVG_* > 0일 때만 실평균을 사용하고, 아니면 활동 기본값→연결 차시 기본값으로 대체하는 경로가 있다. batch MemoryQuiz.xml/RelearnMapper.xml도 실평균이 양수인지에 따라 기본값을 선택한다. 따라서 재집계 0이 화면 0으로 그대로 보인다고 단정하지 않는다. 평균 변경은 리포트뿐 아니라 기억 퀴즈/취약 재학습 선정에도 영향을 준다.

## 연관 작업

- #199(post 4412584663626038893): 콘텐츠 DB 업데이트는 학습 상태를 바꾸지 않는 요청. 9/7 17:02 검증계 테마독해 8단원 매핑 완료 댓글, 운영은 영역별 학습 8단원 콘텐츠가 아직 없어 대기 중. 운영 전체 완료로 쓰지 않는다.
- #15: 평가/종합 리포트 실제 평균 반영의 과거 상위 근거.
- 쌍둥이 연결은 [schedule-learning](schedule-learning.md), 리포트 평균 소비는 [reports-ranking](reports-ranking.md).
