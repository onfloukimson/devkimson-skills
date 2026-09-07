# 배치 실행과 운영

근거: batch src/main/java/com/miraenchoco/job/daldaleng, QuartzConfig, JobController, JobService, 각 Job/Service/Mapper. 다음은 **2026-09-07 HEAD의 cron 의도**이며 실제 운영 활성 trigger 목록이 아니다. 시간대는 애플리케이션/서버에서 확인한다.

| job 이름 | 예정 실행 | 역할 |
|---|---|---|
| scheduleModuleAvgJob | 월 00:00 | 모듈 평균. HEAD job.enabled=false, matchIfMissing=false. [#198 DB 이벤트 이력](content-averages.md) |
| lessonRankJob | 월 00:10 | 수업 랭킹 |
| unitRankJob | 월 00:15 | 단원 랭킹 |
| scheduleReportWeekRkJob | 월 00:20 | 주간 리포트 순위 |
| scheduleReportMonthRkJob | 첫 월요일 00:25 | 월간 리포트 순위 |
| reportWeekJob | 월 00:40 | 주간 리포트 API 호출 |
| reportMonthJob | 첫 월요일 00:50 | 월간 리포트 API 호출 |
| scheduleRelearnJob | 월 01:20 | 재학습 편성 |
| scheduleMemoryQuizJob | 월 02:20 | 기억 퀴즈 편성 |
| scheduleRoundJob | 월 02:40 | 회차 처리 |
| scheduleJob | 월 02:50 | 시간표/주차 전환(ScheduleTimeJob) |
| totalCmsJob | 매일 04~21시, 10/25/40/55분 | 콘텐츠 동기화 |
| alimtalkReportJob | 월 20:00 + 첫 월요일 20:00 | 코드에 남은 리포트 알림. #81 운영 중지 근거 있음 |
| statisticsJob | 첫 월요일 20:00 | 월간 통계 |
| scheduleMmbrSyncJob | 화~금 00:00 | 회원 상태 동기화 |

대부분 일반 job은 HEAD의 job.enabled=true 조건이다. **working tree에는 여러 조건을 false로 바꾸는 사용자 변경이 있었다.** 공통 job.enabled와 matchIfMissing 조합이 실제 등록 결과에 영향을 준다. 로컬 설정만 보고 운영 배치가 전부 꺼졌다고 결론내리지 않는다.

## 스케줄러 함정

- application.yml은 Quartz memory job store, threadCount=20, misfireThreshold=60000 설정. 재시작 후 수동 pause/변경이 영속될 것이라 가정하지 않는다.
- JobService job 목록/수정은 첫 trigger 위주인 경로가 있다. 여러 trigger가 붙은 job의 전체 상태를 목록 한 줄로 판단하지 않는다.
- POST /job/status 실제 명령은 STOP/START. 주석의 PAUSE/RESUME와 구분.
- /job/runNow는 Quartz trigger 호출이 아니라 controller에서 service 메서드로 직접 분기한다. Quartz pause나 Job 동시실행 제약이 수동 경로도 보호한다고 가정하지 않는다.
- ReportWeek/MonthService는 API 응답 HTTP+statusCode를 모두 확인한다. 내부 reportMakeKey/JWT 값은 문서에 복사하지 않는다.
- reportMonthJob 수동 실행은 sendMonthReports()를 인자 없이 호출한다. 실행일의 지난달을 계산하며 STATUS_YN=Y/BASIC_TEST_YN=Y 전체 회원을 대상으로 한다. 특정 학생/임의 과거 월 복구용 endpoint가 아니다. runNow의 nowDateYn은 랭킹 두 분기에만 전달된다.
- 월간 서비스는 학생별 실패를 catch/log하고 계속 처리하며 void를 반환한다. runNow의 JOB TRIGGERED SUCCESS는 개별 생성 완료 보장이 아니다. 회원별 API 업무응답·실패 로그·생성 행을 확인한다.
- 월간 재실행은 출석 통계 비활성화/삽입과 성공 회원의 알림 대상(SEND_STATUS=N) 삽입도 수반한다. 발송 중지 상태여도 대기 대상이 쌓일 수 있다. 운영 DB의 중복 제약/재처리 정책은 확인되지 않았다.
- rank 재실행은 reset/insert와 B2C 포인트에 영향을 준다.
- ScheduleTimeService는 대상 목록 → 각 processSingleSchedule → master/time/details 변경 및 실패 기록. 부분 성공 후 재실행의 효과를 실제 트랜잭션 경계로 판단한다.

## 언제 배포하는가

구축 #59의 main/staging push→pipeline 가이드는 [external-systems](external-systems.md)를 참고한다. 정례 배포 시각을 확정할 문서/댓글은 발견한 근거만으로 부족하다. 과거 12시대 배포 사례는 관행의 증거가 아니다. '월요일 몇 시 이후면 안전'이라고 단정하지 않는다. 월요일 새벽 연결 작업, 매일 CMS, 저녁 통계 등 수정 대상과 겹치는 실행을 확인한다.

인수인계 질문:
- 실제 정례/긴급 배포 시간과 승인/담당자, 배포본 SHA 확인 방법은?
- 실행 중 작업 종료를 기다리는가, 중지/재기동 시 다음 trigger와 misfire를 어떻게 처리하는가?
- 수동 변경한 cron/STOP 상태의 재기동 후 복원 절차는?
- 주·월 리포트 실패 시 어느 순서로 어느 기간을 재처리하는가? 포인트·알림 중복 방지는?
- #81 알림 중지는 현재도 유지되는가? 별도 발송 대상 누적은 어떤 목적인가?
- 외부 API timeout/부분 실패 로그와 운영 확인 화면은 어디인가?

배포 실행은 별도 요청 범위다. 이번 스킬 분석에서는 배포·수동 배치를 실행하지 않았다.
