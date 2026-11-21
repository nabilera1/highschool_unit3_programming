> **3부 테스트하고 공유하기** · 8차시 · 수업 단계: **공유·확장**  
> 핵심 개념: 프로젝트, 기능 설계, 발표, 동료 피드백, 형성평가, 글자 빈도

## 학습 목표

1. 5~7차시에 해결한 실습 미션을 바탕으로 나만의 영단어 구조대를 완성하고 바꾼 기능과 이유를 발표할 수 있다.
2. 동료의 프로그램을 실행해 보고 근거를 들어 피드백할 수 있다.
3. 형성평가로 8차시 동안 배운 개념을 점검하고 스스로 보완할 점을 찾을 수 있다.

## 핵심 질문

> **우리가 만든 영단어 구조대는 누구를, 무엇으로 도울 수 있을까?**

단어장 주제를 과학 용어, 진로 단어, 환경 단어로 바꾸면 영단어 구조대는 친구들의 공부를 '구조'하는 학습 게임이 됩니다.

## 프로젝트 정리 순서

| 단계 | 할 일 | 산출물 |
| --- | --- | --- |
| 1. 기능 고르기 | 아래 미션 메뉴에서 2개 이상 고르기 (5~7차시에 해결한 것 포함) | 기획 메모 |
| 2. 구현 | `lesson08_project.py`에서 출발, 바꾼 줄에 주석 | .py 파일 |
| 3. 테스트 | 정상·경계·예외 입력으로 시험, 고친 점 기록 | 테스트 기록 |
| 4. 발표 | 바꾼 기능 1가지 시연 + 바꾼 줄과 이유 설명 (2분) | 발표 |
| 5. 피드백 | 칭찬 1 + 제안 1, 퀴즈앤보드에 남기기 | 피드백 카드 |

## 실습 미션 메뉴 (기본 · 응용 · 심화)

| 수준 | 미션 | 쓰는 개념 |
| --- | --- | --- |
| 기본 | ① 단어장을 모둠 주제의 `{영단어: 뜻}`으로 바꾸기 | 딕셔너리 |
| 기본 | ② 쉬운 모드: `MAX_BATTERY = 8` | 상수 |
| 응용 | ③ 출동이 끝나면 틀린 글자 기록과 남은 배터리 출력 (함수로) | 리스트 순회, 조건, 함수 |
| 응용 | ④ 3번 출동 뒤 기록표를 한 번만 출력 | for 문, 들여쓰기 |
| 심화 | ⑤ 성공한 출동만 골라 출력하고 성공률 계산 | 2차원 리스트, 조건, 함수 |
| 심화 | ⑥ 나만의 아이디어: 힌트 아이템(배터리 1칸과 뜻 교환), 글자 수로 난이도 고르기, 구조대 위치 막대 | 설계 |

> 수준별 산출물 예시(상·중·하)와 교사 피드백은 **부록 04-7. 학생 산출물 예시**에 있습니다.

## 심화: 어떤 글자부터 말할까? (글자 빈도 분석)

1차시에 '처음 말하면 좋은 글자'를 짐작으로 이야기했습니다. 이제 **데이터**로 확인합니다. 단어장의 각 알파벳이 들어 있는 단어가 몇 개인지 세면, 그 글자를 처음 말했을 때 맞힐 확률을 알 수 있습니다.

```text
단어 8개 기준, 처음에 말하면 맞힐 확률 (상위 5개)
e: 8개 단어 (100.0%) ■■■■■■■■
h: 4개 단어 (50.0%) ■■■■
r: 4개 단어 (50.0%) ■■■■
s: 4개 단어 (50.0%) ■■■■
a: 2개 단어 (25.0%) ■■

잘 나오지 않는 글자
z: 0개 단어 (0.0%)
q: 0개 단어 (0.0%)
x: 0개 단어 (0.0%)
j: 0개 단어 (0.0%)
```

우리 단어장 8개에는 모두 e가 들어 있습니다! 모둠 단어장으로 바꾸면 결과가 어떻게 달라지는지 확인해 보세요. 이 파일은 `from word_rescue import WORDS`로 게임의 단어장을 가져옵니다(4차시에 배운 '함수 파일을 가져다 쓰기').

### lesson08_letter_freq.py

```python
"""영단어 구조대 심화 - 글자 빈도로 '먼저 말할 글자' 찾기         [8차시 심화]

질문: 처음에 어떤 알파벳을 말하면 맞힐 가능성이 가장 높을까?
방법: 단어장의 각 알파벳이 '들어 있는 단어'가 몇 개인지 센다.
      (한 단어에 같은 글자가 여러 번 나와도 1번만 센다 → set(word) 사용)
      확률(%) = 그 글자가 들어 있는 단어 수 / 전체 단어 수 × 100

배우는 것: 딕셔너리로 개수 세기(get), 중첩 for, 정렬, 확률, 데이터에 근거한 전략
실행 방법: python lesson08_letter_freq.py
"""
from word_rescue import WORDS      # 게임과 같은 단어장을 가져온다 (함수 파일의 장점!)

freq = {}                                      # 딕셔너리: 글자 → 그 글자가 들어 있는 단어 수
for word in WORDS:                             # 바깥 for: 단어 하나씩
    for ch in set(word):                       # 안쪽 for: 그 단어의 '서로 다른' 글자 하나씩
        freq[ch] = freq.get(ch, 0) + 1         # 처음 나온 글자면 0 + 1

# (글자, 개수) 쌍을 개수가 큰 순서로 정렬 (개수가 같으면 알파벳 순)
ranking = sorted(sorted(freq.items()), key=lambda pair: pair[1], reverse=True)

print(f"단어 {len(WORDS)}개 기준, 처음에 말하면 맞힐 확률 (상위 5개)")
for ch, count in ranking[:5]:
    print(f"{ch}: {count}개 단어 ({count / len(WORDS) * 100:.1f}%) " + "■" * count)

print("\n잘 나오지 않는 글자")
for ch in "zqxj":
    print(f"{ch}: {freq.get(ch, 0)}개 단어 ({freq.get(ch, 0) / len(WORDS) * 100:.1f}%)")
```

## 발표와 동료 피드백

| 발표 순서 (2분) | 피드백 카드 |
| --- | --- |
| ① 우리 구조대가 돕는 대상과 단어장 주제 | 칭찬 1: 가장 좋았던 기능과 이유 |
| ② 바꾼 기능 1가지 시연 | 제안 1: '이렇게 하면 더 좋겠다' (코드 수준으로 구체적으로) |
| ③ 바꾼 줄과 이유 (코드 화면) | 테스트 1: 이상한 입력을 넣어 본 결과 |
| ④ 테스트에서 찾고 고친 점 | |

## 형성평가 안내 (15분)

아래 **형성평가 1~10번**(객관식 8 + 단답형 2)과 **11·12번 코딩 문항**은 교육청 수업 모형 문서의 8차시 형성평가와 같습니다. 개인별로 풀고, 정답·해설은 부록 04-1-08에서 확인합니다. 형성평가는 성적이 아니라 **피드백**을 위한 것입니다.

활동지: [lesson08_share_assessment.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson08_share_assessment.md)

## 형성평가 1~10번 (객관식 8 · 단답형 2)

**1번.** `word = "rescue"`일 때 `word[2]`의 값은?

- ① `"r"`
- ② `"e"`
- ③ `"s"`
- ④ `"c"`

**2번.** `records = [[1, "help", "성공", 1], [2, "safe", "실패", 6], [3, "rescue", "성공", 2]]`일 때 `records[1][2]`의 값은?

- ① `"help"`
- ② `"성공"`
- ③ `"실패"`
- ④ 6

**3번.** 2번 문제의 records에서 `records[0]`이 뜻하는 것은?

- ① 1번 출동의 기록 전체 (한 행)
- ② 모든 출동의 암호 목록 (한 열)
- ③ 1번 출동의 결과 칸
- ④ 기록표의 행 개수

**4번.** `WORDS = {"help": "도움", "safe": "안전한"}`일 때 `WORDS["safe"]`의 값은?

- ① `"help"`
- ② `"safe"`
- ③ `"안전한"`
- ④ 오류

**5번.** (단답형) 2번 문제의 records로 `print_records(records)`를 실행할 때, 안쪽 for 문(칸 하나를 처리하는 반복)은 모두 몇 번 반복될까?

- 답: ____________________

**6번.** 단어장 `WORDS`에 "together"(함께)를 추가하는 코드로 알맞은 것은?

- ① `WORDS.append("together")`
- ② `WORDS["together"] = "함께"`
- ③ `WORDS["함께"] = "together"`
- ④ `WORDS = {"together": "함께"}`

**7번.** `make_board("help", ["p"])`의 결과는?

- ① `"h e l p"`
- ② `"_ _ _ p"`
- ③ `"p _ _ _"`
- ④ `"p"`

**8번.** `"z" in "rescue"`의 결과는?

- ① `True`
- ② `False`
- ③ `"z"`
- ④ 0

**9번.** `MAX_BATTERY = 6`일 때 `make_battery(4)`의 결과는?

- ① ■■■■□□
- ② ■■□□□□
- ③ ■■■■■■
- ④ □□□□■■

**10번.** (단답형) play() 안에서 암호를 모두 맞혔는지(구조 성공) 확인하는 조건식을 쓰시오. (`board = make_board(word, guessed)`)

- 답: ____________________

## 형성평가 11·12번 (코딩)

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. print_success 함수 (형성평가 11번) (기본)

출동 기록표 records를 받아 결과가 `성공`인 출동의 암호만 한 줄씩 출력하는 함수 `print_success(records)`를 만드세요. 첫째 줄에 n, 다음 n줄에 `출동번호 암호 결과 틀린횟수`가 주어집니다. 성공한 출동이 없으면 아무것도 출력하지 않습니다.

- 입력: n, n줄의 기록
- 출력: 성공한 출동의 암호 (한 줄에 하나)

예제 입력 1

```text
3
1 help 성공 1
2 safe 실패 6
3 rescue 성공 2
```

예제 출력 1

```text
help
rescue
```

### 문제 2. count_wrong 함수 (형성평가 12번) (도전)

암호 word와 말한 글자 리스트 guessed를 받아 틀린 글자의 개수를 돌려주는 함수 `count_wrong(word, guessed)`를 만드세요. 첫째 줄에 암호, 둘째 줄에 말한 글자들이 공백으로 구분되어 주어지면 함수의 결과를 출력합니다.

- 입력: 암호, 말한 글자들 (공백 구분)
- 출력: 틀린 글자 수

예제 입력 1

```text
help
e a h x
```

예제 출력 1

```text
2
```

예제 입력 2

```text
rescue
r e s c u
```

예제 출력 2

```text
0
```

정답과 해설은 **[부록] 04-1-08. 8차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-08-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리 – 8차시 동안 배운 것

| 차시 | 배운 것 | 영단어 구조대에서 |
| --- | --- | --- |
| 1 | 알고리즘, 입력–자료–처리–출력 | 게임 규칙 분석 |
| 2 | 리스트, random, 문자열 | 단어장, 말한 글자, 배터리 그림 |
| 3 | for, 딕셔너리 | 암호판, 뜻이 있는 단어장 |
| 4 | 함수 (함수 없는 코드와 비교) | 함수 8개로 나누기 |
| 5 | while, return | play() 한 판 완성 |
| 6 | 2차원 리스트, 중첩 for | 출동 기록표 |
| 7 | 테스트, 입력 검사 | ask_letter() |
| 8 | 프로젝트, 발표, 데이터 분석 | 나만의 영단어 구조대 |

## 수업 흐름 (50분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 3분 | 발표 순서·피드백 카드 안내 |
| 발표 | 20분 | 짝별 2분 시연, 칭찬 1 + 제안 1 (퀴즈앤보드) |
| 형성평가 | 15분 | 1~12번 개인별 풀이 |
| 확인·성찰 | 10분 | 정답·해설 확인, 틀린 문항의 개념을 위키독스 해당 차시에서 다시 보기 |
| 정리 | 2분 | 8차시 정리, 수행평가 제출 안내 |

## 교사용 메모

- 발표 시간이 부족하면 모둠 안에서 돌아가며 시연하고, 모둠 대표 1명만 전체 발표합니다.
- 수행평가 제출물: `.py` 파일 + 활동지(바꾼 곳·이유·테스트·AI 활용 기록). 설명하지 못하는 코드는 구술로 확인합니다(부록 04-2 채점 시 확인 질문).
- 형성평가 결과에서 정답률이 낮은 문항은 다음 시간 첫 5분에 다시 짚습니다. 2차원 리스트 문항(2·3·5번)이 가장 많이 틀리는 경향이 있습니다.
- 글자 빈도 분석은 수학(확률)·데이터 분석과 연결되는 심화 활동입니다. 시간이 부족하면 과제로 냅니다.

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `lesson08_project.py` | [lesson08_project.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/lesson08_project.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/lesson08_project.py) |
| 소스코드 `lesson08_letter_freq.py` | [lesson08_letter_freq.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/lesson08_letter_freq.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/lesson08_letter_freq.py) |
| 소스코드 `word_rescue.py` | [word_rescue.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/word_rescue.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/word_rescue.py) |
| 학습용 PPT | [lesson08_share_assessment.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/lesson08_share_assessment.pptx) |
| 학생 활동지 | [lesson08_share_assessment.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson08_share_assessment.md) |
| 코딩 테스트 1 정답 코드 | [lesson08_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson08_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson08_test1.py) |
| 코딩 테스트 2 정답 코드 | [lesson08_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson08_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson08_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
