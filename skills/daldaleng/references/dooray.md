# Dooray와 MCP 지식 찾기

Daldal Dooray accountKey: `acc_dr_044c7a2011667802`(계정 B). Cardtalk 계정 A와 다르다.

| 프로젝트 | projectId | 조사 목록 수 |
|---|---|---:|
| (달달영어)서비스-검수 | 4208825534638869505 | 798 |
| 달달영어 구축 | 4126897959619709624 | 84 |
| 2026 서비스 운영 | 4271874883715387917 | 193 |
| 운영 가이드 | 4249504835355939761 | 0 |
| 2026 콘텐츠 운영 | 4211151804512904165 | 95 |

연계 플랫폼 4206032861978589038도 목록 760건을 탐색해 65건의 본문/댓글을 추가 확인했다. 알려진 외부 링크 2건은 projectId를 확인하지 못했다. 자세한 한계는 coverage에 기록했다.

표시 번호는 프로젝트 안에서만 유일하다. #174는 운영 프로젝트의 postId 4383612710882412425, #183은 4401688154468678124이다.

## 도구 순서

1. Agent MCP resource_search/context_resolve로 도메인·심볼·티켓 번호를 검색한다.
2. 인덱스의 projectId/postId로 Dooray get_post와 list_post_logs를 읽는다. 목록 제목만으로 정책을 확정하지 않는다.
3. 로그는 totalCount를 확인해 끝까지 페이지 처리한다. 댓글의 요청/합의/수정/배포/검수 단계를 구분한다.
4. 연결 티켓은 다른 프로젝트일 수 있다. 정확한 projectId를 확인해 접근하고, 실패한 401/403/404는 그대로 기록한다.
5. wiki는 list_wikis → root → list_wiki_pages(parentPageId)로 계층 탐색한다. top-level 1개가 전체 문서 1개를 뜻하지 않는다.

첨부 메타데이터 조회는 다운로드나 본문 분석을 뜻하지 않는다. 링크가 있다는 것만으로 파일 접근 가능을 주장하지 않는다. 보안키/계정이 든 내용은 지식 문서에 복사하지 않는다.

## MCP 저장 경로

- 분석 기준: `ai-workspace/70-knowledge/domains/onflou/projects/daldal-english/engineering/2026-09-07/`
- coverage.json: 저장소 SHA, 소스/커밋/티켓 탐색 단계와 미확인 범위
- catalogs/*.json: 파일·Controller·MyBatis·frontend 요청 인덱스
- git/<repo>-NN.json: 전체 로컬 Git 이력과 변경 파일, HEAD 포함 여부
- dooray/*.json: 티켓 식별자·주제·댓글 수·기술 키워드와 탐색 범위. 원문은 Dooray에서 다시 조회
- references/*.md: 정책·코드 관계·운영 이력 분석
- index.md: 해당 분석의 진입점
- 배포용 스킬 기록: `ai-workspace/60-skills/daldaleng/`

MCP가 KPA 지식의 기준이다. 로컬 ai-workspace mirror를 기본 경로로 읽거나 쓰지 않는다. 사용자가 요청한 devkimson-skills 로컬 skill 업데이트와 MCP 분석 저장은 이번 작업에서 명시적으로 허용된 별도 산출물이다.

운영 지식이 바뀌면 날짜와 근거를 남겨 갱신한다. 전체 티켓 원문을 로컬 skill에 복제하지 않는다. 이번 수집/심층 분석의 차이는 [coverage](coverage.md)를 확인한다.
