# 데이터와 상태

물리 스키마를 운영 DB에서 조회한 결과가 아닌 Mapper/VO/Service 기반 지도다. FK, 인덱스, nullability, 실제 코드 값 분포는 별도 스키마 확인이 필요하다.

| 영역 | 주요 테이블/식별자 | 의미와 주의점 |
|---|---|---|
| 회원 | TB_MMBR / MMBR_SEQ | 내부 학생 식별자. B2C child 식별자와 B2B student/teacher/class를 혼용하지 않음 |
| 콘텐츠 | TB_LRN_LESSON / LRN_LESSON_SEQ, TB_CNTNT, TB_CNTNT_VERSION | 공통 수업과 콘텐츠 버전. 사용/삭제 조건과 버전 연결 확인 |
| 공통 편성 | SCHEDULE_SEQ 및 공통 schedule mapper | 운영자가 편집하는 원본. 학생 schedule seq와 다름 |
| 학생 시간표 | TB_MMBR_SCHEDULE / MMBR_SCHEDULE_SEQ | 회차·주당 횟수·현재 주/진도·basic 포함 여부 |
| 학생 편성 상세 | TB_MMBR_SCHEDULE_DTL | lesson별 순서·진행·완료 회차. END_ROUND만으로 전체 완강 확정 불가 |
| 학습 기록 | TB_MMBR_LRN / MMBR_LRN_SEQ | 수업 학습 단위, round/reset 및 쌍둥이 연결 정보 |
| 페이지 기록 | TB_MMBR_LRN_PAGE, TB_MMBR_LRN_PAGE_CNTNT | 페이지 완료와 콘텐츠 답안. 상위 완료만 맞춰서 복구하지 않음 |
| 리포트 | TB_MMBR_REPORT | REPORT_TY, YEAR/MONTH/WEEK, REG_DT, USE_YN/DEL_YN |
| 질문 | TB_MMBR_NOTE_QUESTION | 학생 질문과 운영자 답변; 파일은 별도 reference로 연결 |
| 파일 | REF_TABLE / REF_SEQ / REF_TYPE | 질문 voice/image와 답변 answ를 구분. prefix가 다른 과거 데이터 존재 |

대표 코드: MC003 main, MC002 basic; LTC001/LTC002는 완강 대상 수업 종류, LTC005는 쌍둥이 관련. 세부 역할은 실제 코드 분기와 함께 읽는다. 리포트 RT00W=주간, RT00M=월간, RT00U=단원. 상태 R, READY, OFFLINE, LEARNING, COMPLETE는 서로 다른 계층/계약에서 쓰인다. 문자열이 비슷해도 동일한 상태 집합으로 합치지 않는다.

삭제는 여러 곳에서 DEL_YN을 바꾸는 논리 삭제다. '최신'은 MAX(seq), 날짜 정렬, active 조건 등 쿼리마다 기준이 다르다. 최신 회원 시간표와 과거 리포트를 무조건 seq로 inner join하면 누락될 수 있다.

개인정보 없이 MMBR_SEQ 등의 필요 최소 식별자와 상태/count를 출력한다. 계정/이메일/음성 URL은 재현에 필요한 경우에만 취급하고 스킬·공유 예제에는 넣지 않는다.
