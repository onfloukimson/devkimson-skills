# 저장소와 소스 기준

기준일: 2026-09-07. 기본 루트는 `C:/devkimson/02_workspace/02_miraen`. 경로가 바뀌었으면 사용자가 지정한 루트를 우선한다. 과거 D: 드라이브 경로는 현재 기준이 아니다.

| 별칭 | 폴더 | 당시 develop HEAD | 역할 |
|---|---|---|---|
| api | daldal-english-api | 9dee01b5efae | 학생 API, 학습·시간표·리포트·LMS |
| bo | daldal-english-backoffice | f9a8f570a168 | 운영 화면, 콘텐츠·시간표·질문 답변 |
| batch | daldal-english-batch | 8d97e5414cc3 | Quartz 정기 작업과 수동 실행 |
| front | daldal-english-frontend | 718bf43a2e9b | 학생/부모 React UI와 학습 뷰어 연계 |
| capture | daldal-english-capture | 이번 분석 제외 | API 연결 흔적만 확인. 폐기 확정 아님 |

API/BO/batch는 Java 17, Spring Boot 3.5.4, Gradle, MyBatis, MariaDB driver. BO는 Thymeleaf. Front는 React 19, Vite 7, React Router 7, Zustand 5, React Query 5, Axios 1. 이 버전들은 당시 manifest 기준이며 다음 작업에서 실제 파일을 확인한다.

분석 도중 API 학습/시간표 서비스, batch QuartzConfig/JobController, 각 로컬 환경 설정, frontend .env에 사용자 변경이 있었다. 인벤토리의 소스는 working tree, Git 이력은 로컬 전체 ref 기준이다. 로컬 커밋 수는 api 510 / bo 200 / batch 129 / front 3060. 배포 SHA나 원격 최신성을 증명하지 않는다. 별도 fetch/pull/checkout은 수행하지 않았다.

## 읽기 전용 탐색

```bash
git -C "$repo" status --short
git -C "$repo" rev-parse HEAD
git -C "$repo" log -15 --oneline
python scripts/inspect_repository.py "$repo" --mode catalog --query MmbrSchedule
python scripts/inspect_repository.py "$repo" --mode history --query '리포트' --limit 30
git -C "$repo" show <sha> -- <관련파일>
git -C "$repo" grep -n 'getAllLessonEndYn' -- src
```

`repo`는 실제 폴더를 지정한다. 스크립트는 설정 파일 본문을 출력하지 않고 Git/소스 메타데이터만 stdout에 쓴다. catalog는 정규식/XML 탐색 인덱스이며 실제 호출 그래프나 SQL 실행 계획이 아니다. history의 `reachableFromHead`로 다른 ref에만 있는 커밋을 구분한다. Git ownership 오류는 폴더 소유/실행 계정을 확인하고 해결하며 전역 safe.directory 완화로 숨기지 않는다.
