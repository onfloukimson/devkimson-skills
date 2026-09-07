# 운영 #174: 초코클래스 LMS API

프로젝트 4271874883715387917 / post 4383612710882412425. 2026-09-07 본문·댓글 재조회. 번호 #174만으로 다른 프로젝트 티켓을 조회하지 않는다.

## 합의와 현재 구현

- today: 당일 진입/로그인 근거로 READY/OFFLINE 구분. 진단 테스트만으로 COMPLETE가 되지 않는다. readyCnt는 READY+OFFLINE 요구를 확인한다.
- weekly: incompleteCnt 포함, 월요일 키 MON, 요청 요일 범위 유지. 반 전체 비율의 분모는 요청 studentUids의 distinct non-null 학생 집합이다.
- weekly/students: completeRate의 이름과 달리 정답 문항/응답 문항 비율을 쓰는 합의·구현 맥락이 있다. 무응답 null과 모두 오답 0을 구분한다. 오래된 '학습 완료일/출석일' 정의와 합치지 않는다.
- 완료 집계는 개념/평가 완료와 첫 학습 ROUND=1 조건을 확인한다. 진단/재학습 중복 합산 금지.
- monthly: 요청 상대 주차로 묶는다. 예: 7/6~8/2는 4주이며 달력 월/주 bucket으로 5개가 되면 안 된다.
- monthly/students: 평가가 없으면 avgScore=null. learningRate는 완료 수와 응답 여부를 함께 확인한다.

b9313ab diff의 실제 동작:
MonthlyStudentLearningRowDto에 answerCnt를 추가했다. 이름과 달리 mapper는 EXISTS를 1/0으로 반환한다. 개념/평가, ROUND=1, CNTNT_LRN_TY=Q, ANSW_ST_CD=Y/N, 응답 갱신 기간을 검사한다.
completeCnt<=0이고 answerCnt<=0이면 learningRate=null. 시도 이력이 있으면 completeCnt/attendanceCnt를 반올림하고 100으로 제한한다. attendanceCnt<=0도 null. 반 learningRate는 학생 비율의 산술평균이 아니라 전체 completeCnt 합계/전체 attendanceCnt 합계다. 학생 중 learningRate!=null인 사람이 아무도 없으면 null이다. avgScore는 null을 제외한 평균이다. null→0 요청은 학생/반, 필드별로 평균 참여 여부까지 바뀌는지 확인한다. 화면 표시만 바꾸는 요구인지 API 계약을 바꾸는 요구인지 구분하고, 새 요청을 과거 계약만으로 일괄 거부하지 않는다. DTO nullable 타입과 JSON 직렬화도 확인한다.

## 확인 이력

| 날짜 | 댓글에서 확인된 단계 |
|---|---|
| 8/21 | today 상태·진단 완료·readyCnt 검수 지적 |
| 8/24 | 관련 수정 검증계 반영 |
| 8/25 | 검수/운영 배포 댓글 및 monthly learningRate null 후속 요구 |
| 8/26 | null 처리 수정 검증계 반영·확인 |
| 8/27 12:30 | 운영 배포 완료 댓글 |
| 8/28 | LMS 최종 QA 완료 댓글 |
| 9/3~9/4 | 이미 8/31 오픈한 서비스라 부하 테스트 생략하는 논의와 종료 확인 |

부하 테스트 통과 이력이 아니다. 배포 댓글도 현재 운영 SHA를 확인한 결과가 아니다.

## 코드 탐색

API chococlass/ChococlassExternalController, ChococlassExternal*ServiceImpl, *Dto, mapper/chococlass/ChococlassExternal*Mapper.xml. 오늘/주간/월간을 별도 서비스/mapper로 추적한다.
관련 커밋: 98fea86(today/weekly), 558fb55(monthly), b9313ab(monthly null).
오래된 TXT/XLSX/DOCX는 설계의 과거 근거다. 충돌 시 작성자 개인 이름으로 절대 우선순위를 만들지 않고 최신 티켓 합의 날짜·실제 코드·검수 결과를 함께 제시한다.
