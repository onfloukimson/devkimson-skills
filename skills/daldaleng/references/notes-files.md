# 질문노트·파일·답변

| 주체 | 실제 경로/처리 | 계약 |
|---|---|---|
| 학생 질문 생성 | API NoteServiceImpl.setNoteNoteAdd | student role/학습 행 확인 후 질문, voice와 imageFile list |
| 학생 질문 수정 | API NoteVO + setNoteNoteMod | voiceFileUpdateYn, imageFileUpdateYn, imageFile |
| frontend 상세 수정 | pages/note/question/detail/hook/useNoteQuestionDetail.jsx | fileDeleteYn, attachFileDeleteYn, attachFile 전송 지점 |
| 운영 답변 | BO updMmbrNoteQuestionAnsw | answFileDelYn 또는 새 파일로 기존 첨부 처리; 답변 알림톡 |

**소스 계약 불일치 후보**: front 상세의 필드명과 API 수정 VO/Service 필드가 다르다. 이것만으로 운영 장애 확정은 아니다. 실제 multipart 요청, 현재 branch/배포 조합, service adapter/다른 경로를 확인하고 삭제만/유지/교체/다중 이미지/음성 단독 사례로 검증한다. 학습 도구 내부 useStudyToolQuestion.jsx도 fileDeleteYn/voiceFile/imageFile을 보내지만 voiceFileUpdateYn/imageFileUpdateYn을 보내지 않는 경로가 있다. 상세 화면만 고치면 이 경로가 남을 수 있다.

삭제 flag를 update flag로 단순 개명하는 것만으로 충분하지 않다. front NoteQuestionDetailFile은 새 파일 선택 시 isAttachFileDelete=false로 설정한다. API의 imageFileUpdateYn=Y는 삭제뿐 아니라 교체를 포함한다. 유지=N, 삭제=Y+새 파일 없음, 교체=Y+새 파일 있음의 의미를 맞추고 음성도 별도 검증한다.

API uploadNoteFile은 upload/note/<noteType>와 REF_TABLE=mmbr_note_<noteType>, REF_TYPE=<noteType>_voice 또는 _image 형태를 사용한다. 수정 flag=Y면 관련 파일 그룹을 논리 삭제한 뒤 업로드하는 경로다. DB rollback과 외부 파일 저장 rollback을 동일시하지 않는다.

API NoteMapper 질문 파일 조회는 REF_TABLE='mmbr_note_question'; BO MmbrNoteQuestionMapper는 'mmbr_note_question'와 'tb_mmbr_note_question'를 모두 허용하는 부분이 있다. 과거 데이터가 보이는 화면과 안 보이는 화면의 차이를 이 조건부터 확인한다. API imageFiles 배열과 BO GROUP_CONCAT 출력도 다르다. frontend preview가 첫 파일을 사용하는 코드와 전체 첨부 개수를 분리한다.

BO 답변 REF_TYPE=answ는 학생의 question_image/question_voice와 별개다. 질문 이미지 삭제를 위해 답변 첨부까지 지우지 않는다.

capture: API 질문 등록에서 setInsertStudyNoteScanBatch enqueue가 주석인 경로를 확인했다. capture 저장소는 분석하지 않았다. 다른 caller/환경까지 서버 전체 미사용 또는 폐기를 확정하지 않는다.

관련 이력: API f2bfcd2(9/4 수정 첨부/음성), 7cdb5fe(8/20 등록 첨부); BO 612bca9/6688a72/6360dea(첨부 표시), frontend 718bf43(9/4 생성/수정 작업). 각 diff가 실제 배포에 포함됐는지는 별도 확인한다.
