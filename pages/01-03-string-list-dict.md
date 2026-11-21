> **1부 게임을 분석하고 설계하기** · 3차시 · 수업 단계: **컴퓨팅 설계**  
> 핵심 개념: for 문, 문자열 순회, 리스트 누적, join, 딕셔너리(키·값), 추가, list(딕셔너리)

## 학습 목표

1. for 문으로 문자열의 글자를 하나씩 꺼내 암호판을 만들 수 있다.
2. 딕셔너리로 영단어와 뜻을 짝지어 저장하고, 키로 값을 찾고 추가할 수 있다.
3. 리스트와 딕셔너리 중 상황에 알맞은 자료구조를 고를 수 있다.

## 핵심 질문

> **암호가 4글자일 때도, 8글자일 때도 똑같은 코드로 암호판을 만들려면? 영단어와 뜻을 짝지어 두려면 어떤 그릇이 좋을까?**

## for 글자 in 문자열

```python
for ch in "help":
    print(ch)          # h, e, l, p 가 차례로 한 줄씩
```

for 문은 문자열의 글자를 **앞에서부터 하나씩** 꺼냅니다. 글자 수가 몇 개든 같은 코드로 처리할 수 있습니다.

## 암호판 알고리즘

```python
board = []
for ch in word:                 # 암호의 글자를 하나씩
    if ch in guessed:           # 말한 글자면 보여 주고
        board.append(ch)
    else:                       # 아니면 가린다
        board.append("_")
print(" ".join(board))          # ["h", "_", "_", "p"] → "h _ _ p"
```

| ch | `ch in guessed` (guessed = `["h", "p"]`) | board |
| --- | --- | --- |
| h | True | `["h"]` |
| e | False | `["h", "_"]` |
| l | False | `["h", "_", "_"]` |
| p | True | `["h", "_", "_", "p"]` |

`" ".join(board)`는 리스트의 글자들을 공백으로 이어 붙여 `"h _ _ p"`를 만듭니다.

## 딕셔너리: 키로 값을 찾는다

2차시의 단어장은 영단어만 있었습니다. 구조에 성공했을 때 **뜻**도 알려 주려면 영단어와 뜻을 짝지어 두어야 합니다.

```python
WORDS = {"help": "도움", "safe": "안전한", "hope": "희망"}
print(WORDS["help"])          # 도움     ← 키(영단어)로 값(뜻)을 찾는다
WORDS["care"] = "돌봄"         # 새 단어 추가
print(list(WORDS))            # ['help', 'safe', 'hope', 'care']  ← 키만 모은 리스트
word = random.choice(list(WORDS))
```

| 자료구조 | 모양 | 찾는 방법 | 영단어 구조대에서 |
| --- | --- | --- | --- |
| 리스트 | `["h", "x"]` | 번호(인덱스) `guessed[0]` | 말한 글자, 암호판 |
| 딕셔너리 | `{"help": "도움"}` | 이름(키) `WORDS["help"]` | 단어장 (영단어 → 뜻) |

> **주의** 없는 키를 꺼내면 `KeyError`가 납니다. `if w in WORDS:`로 먼저 확인합니다. 딕셔너리의 `in`은 **키**에 있는지를 봅니다.

## 실행 예시

`lesson03_board.py`를 실행한 화면입니다. 아직 반복 횟수는 3번으로 정해 두었습니다.

```text
[SOS] 4글자 암호, 뜻 힌트: 희망
알파벳 한 글자 > e
암호판: _ _ _ e
알파벳 한 글자 > h
암호판: h _ _ e
알파벳 한 글자 > p
암호판: h _ p e
정답 확인(교사용): hope
```

## 전체 코드

### lesson03_board.py

```python
"""영단어 구조대 - 2단계: 뜻이 있는 단어장과 암호판             [3차시]

이번 단계에서 배우는 것
  - 딕셔너리        : {영단어(키): 뜻(값)}  WORDS["help"] → "도움"
  - 딕셔너리에 추가 : WORDS["thanks"] = "고마움"
  - list(WORDS)     : 딕셔너리의 키(영단어)만 모은 리스트
  - for ch in word  : 암호의 글자를 앞에서부터 하나씩 꺼낸다
  - " ".join(board) : ["h", "_", "_", "p"] → "h _ _ p"

암호판이 만들어지는 원리 (word = "help", guessed = ["h", "p"])
  h → guessed에 있음 → h
  e → 없음           → _
  l → 없음           → _
  p → 있음           → p          암호판:  h _ _ p

※ 4차시에는 이 암호판 코드를 make_board(word, guessed) 함수로 만듭니다.
실행 방법: python lesson03_board.py
"""
import random

WORDS = {"help": "도움", "safe": "안전한", "hope": "희망", "rescue": "구조하다",
         "friend": "친구", "share": "나누다", "smile": "미소"}
WORDS["together"] = "함께"                 # 딕셔너리에 새 단어 추가

word = random.choice(list(WORDS))          # 키(영단어) 중 하나를 고른다
print(f"[SOS] {len(word)}글자 암호, 뜻 힌트: {WORDS[word]}")

guessed = []
for turn in range(3):                      # 이번 단계에서는 3번만 입력 (횟수가 정해진 반복 → for)
    g = input("알파벳 한 글자 > ")
    guessed.append(g)

    board = []                             # 암호판 만들기
    for ch in word:
        if ch in guessed:
            board.append(ch)
        else:
            board.append("_")
    print("암호판:", " ".join(board))

print("정답 확인(교사용):", word)
```

## 실습 활동

1. 단어장을 '영단어 | 뜻' 표로 그린 뒤, 서로 돕는 말 3개를 딕셔너리에 추가하세요.
2. `word = "together"`, `guessed = ["t", "e"]`일 때 암호판을 손으로 먼저 써 보고 실행해 확인하세요.
3. `range(3)`을 `range(5)`로 바꾸면 무엇이 달라지는지 예측하고 확인하세요.
4. 암호판 코드 5줄에 '하는 일'을 한 문장으로 이름 붙여 보세요. (다음 시간에 이 이름이 함수 이름이 됩니다) **[활동지]**

활동지: [lesson03_string_list_dict.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson03_string_list_dict.md)

## 도전 과제 (기본 · 응용 · 심화)

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | 시작할 때 뜻 힌트 대신 글자 수만 보여 주도록 바꾸기 |
| 응용 | 공개된 칸 수와 남은 칸 수를 함께 출력하기 (`board.count("_")`) |
| 심화 | 단어장을 `{"쉬움": {...}, "어려움": {...}}`처럼 딕셔너리 안의 딕셔너리로 만들고, 난이도를 골라 암호를 뽑기 |

## 확인 퀴즈

**Q1.** `for ch in "help":`에서 `ch`에 차례로 들어가는 값은?

- ① `"help" 한 번`
- ② `"h", "e", "l", "p"`
- ③ 0, 1, 2, 3
- ④ `"p", "l", "e", "h"`

**Q2.** `" ".join(["h", "_", "_", "p"])`의 결과는?

- ① `"h__p"`
- ② `"h _ _ p"`
- ③ `["h _ _ p"]`
- ④ `"h,_,_,p"`

**Q3.** `WORDS = {"help": "도움", "safe": "안전한"}`일 때 `WORDS["help"]`의 값은?

- ① `"help"`
- ② `"도움"`
- ③ 0
- ④ 오류

**Q4.** 단어장 `WORDS`에 `"care": "돌봄"`을 추가하는 코드는?

- ① `WORDS.append("care")`
- ② `WORDS["care"] = "돌봄"`
- ③ `WORDS["돌봄"] = "care"`
- ④ `WORDS = {"care": "돌봄"}`

**Q5.** `random.choice(list(WORDS))`가 돌려주는 것은?

- ① 뜻 하나
- ② 영단어(키) 하나
- ③ `(영단어, 뜻) 쌍`
- ④ 단어장 전체

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 밑줄 암호판 출력 (기본)

첫째 줄에 암호, 둘째 줄에 지금까지 말한 글자들이 공백 없이 주어집니다. 말한 글자는 그대로, 나머지는 `_`로 바꾸어 한 칸씩 띄어 출력하세요.

- 입력: 암호, 말한 글자들
- 출력: 암호판

예제 입력 1

```text
help
hp
```

예제 출력 1

```text
h _ _ p
```

예제 입력 2

```text
together
te
```

예제 출력 2

```text
t _ _ e t _ e _
```

### 문제 2. 뜻 힌트 사전 (도전)

첫째 줄에 n, 다음 n줄에 `영단어 뜻`이 주어집니다. 다음 줄에 m, 다음 m줄에 찾을 영단어가 주어지면 뜻을 출력하고, 단어장에 없으면 `단어장에 없어요`를 출력하세요.

- 입력: n, n줄의 `영단어 뜻`, m, m줄의 영단어
- 출력: 각 영단어의 뜻 또는 `단어장에 없어요`

예제 입력 1

```text
3
help 도움
safe 안전한
hope 희망
3
hope
smile
help
```

예제 출력 1

```text
희망
단어장에 없어요
도움
```

정답과 해설은 **[부록] 04-1-03. 3차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-03-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- `for ch in word:`로 글자 수와 상관없이 같은 코드로 암호판을 만든다
- `" ".join(리스트)`로 글자들을 공백으로 이어 붙인다
- 딕셔너리 `{키: 값}`은 이름(키)으로 값을 찾는다, `WORDS[새 키] = 값`으로 추가
- 번호로 찾으면 리스트, 이름으로 찾으면 딕셔너리

## 수업 흐름 (50분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 5분 | 4글자·8글자 암호판을 같은 코드로? 핵심 질문 |
| 전개 1 | 15분 | for 문과 암호판 알고리즘, 손으로 추적 |
| 전개 2 | 15분 | 딕셔너리 단어장 만들기·찾기·추가, 리스트와 비교 |
| 전개 3 | 7분 | step2 코드 수정, 암호판 코드에 '하는 일' 이름 붙이기 [활동지] |
| 정리 | 8분 | 확인 퀴즈, 4차시 예고(함수) |

## 교사용 메모

- 영어 시간에 배운 단어로 단어장을 만들게 하면 **영어 교과와 연계**됩니다. 키는 반드시 소문자 알파벳만 쓰게 안내합니다.
- `together`처럼 같은 글자가 두 번 나오는 단어로 암호판을 추적하면 for 문의 동작을 확실히 이해합니다.
- 활동 4의 '하는 일 이름 붙이기'는 4차시 함수 설계로 바로 이어집니다. 학생이 붙인 이름을 모아 두었다가 다음 시간에 `make_board`와 비교합니다.

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `lesson03_board.py` | [lesson03_board.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/lesson03_board.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/lesson03_board.py) |
| 학습용 PPT | [lesson03_string_list_dict.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/lesson03_string_list_dict.pptx) |
| 학생 활동지 | [lesson03_string_list_dict.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson03_string_list_dict.md) |
| 코딩 테스트 1 정답 코드 | [lesson03_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson03_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson03_test1.py) |
| 코딩 테스트 2 정답 코드 | [lesson03_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson03_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson03_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
