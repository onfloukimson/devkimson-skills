# 시스템 연결

```text
학생/부모 React 화면
  → services / useAxios (token, 응답 envelope)
  → API Controller → Service → MyBatis → 업무 DB
                         ↘ 파일 저장, 외부 회원/포인트 연동

BO Thymeleaf → BO Controller/Service/Mapper → 콘텐츠·공통 시간표·노트 답변
                                    ↘ 답변 알림톡

Quartz job → batch Service/Mapper → 랭킹·진도·통계·회원 동기화
                           ↘ front API 호출 → 학생 리포트 저장
```

BO가 공통 커리큘럼을 변경하고 API가 학생별 누락 편성을 반영하며 batch가 주차 전환·랭킹·리포트를 처리한다. 공유 테이블을 사용하므로 저장소 하나의 함수 수정만으로 영향 분석을 끝내지 않는다.

| 흐름 | 연결점 | 흔한 오판 |
|---|---|---|
| 시간표 변경 | BO ScheduleServiceImpl → 공통 매핑 → API setStudentScheduleCheckSchedule → 학생 상세 | BO 변경 즉시 모든 학생 이력이 덮임 |
| 학습 저장 | viewer message → frontend learning service → API Container/Lrn → LRN/PAGE/CNTNT | UI 종료 이벤트만으로 DB 완료 판단 |
| 리포트 생성 | batch ReportWeek/MonthService → API report endpoint → TB_MMBR_REPORT | batch에 있는 모든 report SQL이 직접 실행됨 |
| 질문/답변 | front 질문 등록·수정 → API 파일 / BO 답변·파일·알림 | 질문 이미지·음성·답변 첨부가 같은 계약 |
| 랭킹 | batch 집계 → rank rows → API 조회 → front RankCard, B2C 적립 | 재집계는 순위 값만 변경 |
| LMS | external API → MmbrReport/LMS 집계 → 별도 ready/status/null 규칙 | 학생 화면 표시 기준을 그대로 적용 |

관련 소스의 정확한 위치는 [코드 지도](code-map.md), 관계/코드 값은 [데이터 모델](domain-model.md)을 읽는다.
