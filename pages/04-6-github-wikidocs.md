## 저장소 구조 (위키독스 연동 규칙)

위키독스에서 깃허브 권한을 승인하면 저장소, `README.md`, `TOC.md`, 첫 페이지, push 웹훅이 자동으로 만들어집니다. 이 자료는 그 틀에 맞춰 만들었습니다.

| 파일/폴더 | 역할 |
| --- | --- |
| `README.md` | 책 요약 (첫 번째 `#` 제목을 제외한 내용이 책 소개로 사용됨) |
| `TOC.md` | 목차. 2칸 들여쓰기 = 하위 페이지, 4칸 = 하위의 하위 |
| `pages/` | 실제 페이지 md 파일 |
| `source/` | 게임 코드 (`word_rescue.py` 함수 버전, `word_rescue_nofunc.py` 함수 없는 버전, 차시별 단계 코드) |
| `source/examples/` | 학생 산출물 예시 6개 (과제 A·B × 상·중·하) |
| `source/solutions/` | 코딩 테스트 정답 코드 16개 |
| `slides/`, `worksheets/`, `teacher/` | 내려받기용 PPT, 활동지, 교사 자료 (위키독스 페이지가 아니라 깃허브 링크로 제공) |

## md 작성 시 지킨 규칙

- 1레벨 `#` 제목은 **페이지 제목으로 자동 생성**되므로 페이지 본문에서 쓰지 않고 `##`부터 사용했습니다.
- 모든 제목(헤딩)의 **위아래에 빈 줄**을 넣었습니다. (빈 줄이 없으면 전자책 PDF 변환 오류)
- 위키독스는 페이지를 **제목 순으로 정렬**하므로 `00.`, `01차시.`처럼 **제목에 번호**를 붙였습니다.
- 페이지 파일 이름은 영문으로 만들었습니다. 내려받기용 자료는 `lesson차시_내용`(차시별 자료), `word_rescue`(기준 게임 코드), `task과제_수준`(산출물 예시)처럼 짧고 뜻이 드러나게 지었습니다.

## 이번 개정에서 바뀐 파일 이름

교육청 수업 모형 문서와 차시 순서를 맞추면서 페이지와 코드 파일 이름이 바뀌었습니다. 위키독스에서 예전 페이지가 남아 있으면 삭제하세요.

| 예전 | 지금 |
| --- | --- |
| 01-01-play-algorithm.md | 01-01-play-rules.md |
| 01-02-list-random-string.md | 01-02-data-structure.md |
| 01-03-for-board.md | 01-03-string-list-dict.md |
| 01-04-while-basic-game.md | 01-04-function-compare.md (함수 비교) |
| 02-05-test-input-check.md | 03-07-test-input.md |
| 02-06-function.md | 01-04-function-compare.md에 통합 |
| 03-07-dict-2d-list.md | 01-03 (딕셔너리) + 02-06-records-2d-list.md (2차원 리스트) |
| 03-08-project-share.md | 03-08-share-assessment.md |
| (없음) | 02-05-while-play.md, 04-7-student-work.md, 04-8-lesson-model.md |
| 예전 코드·PPT·활동지 (파일 이름이 new_로 시작) | `source`·`slides`·`worksheets`·`teacher` 폴더 전체를 새 파일로 교체 |

## 올리는 방법

```bash
git clone https://github.com/nabilera1/highschool_unit3_programming.git
cd highschool_unit3_programming
git rm -r pages source slides worksheets teacher   # 예전 파일 정리
# 이 자료의 파일을 모두 복사한 뒤
git add .
git commit -m "영단어 구조대: 수업 모형 차시 순서·함수 비교 수업 반영"
git push origin main
```

push하면 웹훅이 위키독스에 동기화합니다. 위키독스가 자동으로 만든 첫 페이지 파일이 남아 있다면 `TOC.md`에서 빠져 있는지 확인하세요.

## 링크 규칙

- 소스코드·PPT·활동지 링크는 위키독스에서도 동작하도록 **깃허브 절대 주소**를 사용했습니다.
- 기본 브랜치를 `main`으로 가정했습니다. 다른 이름이면 링크의 `/main/`을 바꿔야 합니다.
- 저장소 주소: https://github.com/nabilera1/highschool_unit3_programming
