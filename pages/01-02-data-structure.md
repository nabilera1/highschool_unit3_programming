> **1부 게임을 분석하고 설계하기** · 2차시 · 수업 단계: **문제 구조화**  
> 핵심 개념: 리스트, 인덱스, append, random.choice, 문자열(len, in), 문자열 곱하기, 추적표

## 학습 목표

1. 리스트로 여러 단어를 한 변수에 담고, 인덱스로 하나를 꺼낼 수 있다.
2. random.choice로 암호를 고르고, 문자열의 len·인덱스·in을 쓸 수 있다.
3. 입력에 따라 자료(guessed, battery)가 어떻게 바뀌는지 추적표로 따라갈 수 있다.

## 핵심 질문

> **단어 8개를 변수 8개에 따로 저장하면 어떤 점이 불편할까? 게임의 자료를 어떤 그릇에 담아야 할까?**

1차시에 찾은 자료(단어장, 암호, 말한 글자, 배터리)를 오늘은 파이썬의 **그릇**에 담아 봅니다. 여러 값을 순서대로 담는 그릇이 **리스트**, 글자들의 순서가 **문자열**입니다.

## 리스트: 여러 값을 한 변수에

```python
words = ["help", "safe", "hope", "rescue", "friend", "share", "smile", "together"]
print(words[0])      # help      ← 번호(인덱스)는 0부터!
print(words[-1])     # together  ← -1은 맨 뒤
print(len(words))    # 8
```

| 인덱스 | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 값 | help | safe | hope | rescue | friend | share | smile | together |

말한 글자처럼 **게임 도중 늘어나는 자료**는 빈 리스트에서 시작해 `append()`로 뒤에 붙입니다.

```python
guessed = []              # 처음엔 아무것도 말하지 않았다
guessed.append("h")       # ["h"]
guessed.append("x")       # ["h", "x"]   ← 틀린 글자도 '말한 글자'이므로 넣는다
```

## random.choice: 무작위로 하나 고르기

```python
import random
word = random.choice(words)      # 실행할 때마다 다른 암호
```

## 문자열도 '글자들의 순서'

| 코드 | 결과 | 뜻 |
| --- | --- | --- |
| `len("rescue")` | `6` | 글자 수 |
| `"rescue"[0]` | `"r"` | 0번 글자 |
| `"e" in "rescue"` | `True` | 들어 있나? |
| `"z" in "rescue"` | `False` | 없으면 False → 배터리 감소! |
| `"■" * 3 + "□" * 2` | `"■■■□□"` | 문자열 곱하기 → 배터리 그림 |

## 추적표로 자료의 변화 따라가기

코드를 실행하기 전에 **손으로 먼저** 따라가 보는 표를 추적표라고 합니다. 암호가 `"help"`, 배터리 6칸일 때 h → x → e → l → p 순서로 입력하면 자료가 이렇게 바뀝니다.

| 순서 | 입력 | guessed | 암호판 | 배터리 | 판단 |
| --- | --- | --- | --- | --- | --- |
| 시작 | – | `[]` | `_ _ _ _` | ■■■■■■ (6) | 게임 시작 |
| 1 | h | `["h"]` | `h _ _ _` | ■■■■■■ (6) | 암호에 있음 |
| 2 | x | `["h", "x"]` | `h _ _ _` | ■■■■■□ (5) | 없음 → 배터리 1칸 감소 |
| 3 | e | `["h", "x", "e"]` | `h e _ _` | ■■■■■□ (5) | 암호에 있음 |
| 4 | l | `["h", "x", "e", "l"]` | `h e l _` | ■■■■■□ (5) | 암호에 있음 |
| 5 | p | `["h", "x", "e", "l", "p"]` | `h e l p` | ■■■■■□ (5) | _ 없음 → 구조 성공 |

> **생각해 보기** x는 암호판에 나타나지 않는데 왜 guessed에 넣을까요? → 이미 말한 글자를 다시 입력하지 못하게 검사할 때 쓰기 때문입니다. guessed는 '맞힌 글자'가 아니라 **'말한 글자'** 목록입니다.

## 실행 예시

`lesson02_words.py`를 두 번 실행한 화면입니다. 아직 반복이 없어서 한 글자만 입력받습니다.

```text
[SOS] 4글자 암호가 도착했어요. 첫 글자는 h 입니다.
알파벳 한 글자 > p
p 는 암호에 있어요!
말한 글자: ['p']
배터리: ■■■■■■ (6칸)
정답 확인(교사용): hope
```

```text
[SOS] 6글자 암호가 도착했어요. 첫 글자는 r 입니다.
알파벳 한 글자 > z
z 는 암호에 없어요. 신호가 약해집니다.
말한 글자: ['z']
배터리: ■■■■■□ (5칸)
정답 확인(교사용): rescue
```

## 전체 코드

### lesson02_words.py

```python
"""영단어 구조대 - 1단계: 단어장에서 암호 고르기                [2차시]

이번 단계에서 배우는 것
  - 리스트        : 여러 단어를 한 변수에 순서대로 담는다.   words[0] → "help"
  - random.choice : 리스트에서 하나를 무작위로 고른다.
  - 문자열        : len()으로 글자 수, word[0]으로 첫 글자, in 으로 포함 여부
  - 리스트 append : 말한 글자를 guessed 리스트에 차례로 쌓는다.
  - 문자열 곱하기 : "■" * 5 → "■■■■■"  (배터리 그림)

실행 방법: python lesson02_words.py
"""
import random

# 암호 단어장 (리스트) - 3차시에 '뜻'을 함께 담는 딕셔너리로 바뀝니다
words = ["help", "safe", "hope", "rescue", "friend", "share", "smile", "together"]
MAX_BATTERY = 6

# 1) 암호를 무작위로 하나 고른다
word = random.choice(words)
print(f"[SOS] {len(word)}글자 암호가 도착했어요. 첫 글자는 {word[0]} 입니다.")

# 2) 게임이 기억할 자료를 만든다
guessed = []                  # 말한 글자 리스트 (처음엔 비어 있음)
battery = MAX_BATTERY         # 남은 구조 신호 배터리

# 3) 알파벳 한 글자를 입력받아 판단한다 (반복은 5차시에!)
g = input("알파벳 한 글자 > ")
guessed.append(g)
if g in word:
    print(f"{g} 는 암호에 있어요!")
else:
    battery = battery - 1
    print(f"{g} 는 암호에 없어요. 신호가 약해집니다.")

# 4) 지금 상태를 보여 준다
print("말한 글자:", guessed)
print("배터리:", "■" * battery + "□" * (MAX_BATTERY - battery), f"({battery}칸)")
print("정답 확인(교사용):", word)
```

## 실습 활동

1. 코드를 실행하기 전에 화면을 예측해 보고, 실행해서 비교하세요. (PRIMM의 예측 → 실행)
2. `words` 리스트에 '서로 돕는 말' 영단어를 3개 더 넣어 보세요. (소문자 알파벳만)
3. 암호 `"help"`로 추적표를 손으로 채워 보세요. **[활동지]**
4. 큰 문제를 '암호 고르기 → 보여 주기 → 입력 → 판단 → 기록' 작은 문제로 나누고, 각 단계에 필요한 자료를 적어 보세요.

활동지: [lesson02_data_structure.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson02_data_structure.md)

## 도전 과제 (기본 · 응용 · 심화)

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | 첫 글자와 함께 마지막 글자도 힌트로 보여 주기 (`word[-1]`) |
| 응용 | 입력한 글자가 암호의 몇 번째 자리에 있는지 출력하기 (`word.index(g)`) |
| 심화 | `MAX_BATTERY`를 8로 바꾸면 화면의 어느 부분이 바뀌는지 예측하고 확인하기. 숫자 6을 코드 여러 곳에 직접 쓰면 어떤 문제가 생길까? |

## 확인 퀴즈

**Q1.** `words = ["help", "safe", "hope"]`일 때 `words[1]`의 값은?

- ① `"help"`
- ② `"safe"`
- ③ `"hope"`
- ④ 오류

**Q2.** `random.choice(words)`가 하는 일은?

- ① 리스트를 정렬한다
- ② 리스트에서 하나를 무작위로 고른다
- ③ 리스트를 섞는다
- ④ 리스트의 길이를 센다

**Q3.** `word = "rescue"`일 때 `word[0]`과 `len(word)`의 값은?

- ① `"r", 6`
- ② `"e", 6`
- ③ `"r", 5`
- ④ `"rescue", 1`

**Q4.** `guessed = ["h"]`에서 `guessed.append("x")`를 실행한 뒤의 `guessed`는?

- ① `["x"]`
- ② `["h", "x"]`
- ③ `["x", "h"]`
- ④ `"hx"`

**Q5.** `"■" * 3 + "□" * 2`의 결과는?

- ① ■■■□□
- ② ■□■□■
- ③ ■3□2
- ④ 오류

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 번호로 암호 꺼내기 (기본)

첫째 줄에 단어들이 공백으로 구분되어 주어지고, 둘째 줄에 번호 k(1부터 시작)가 주어집니다. k번째 단어와 그 글자 수를 공백으로 구분해 출력하세요.

- 입력: 단어들 (공백 구분), 번호 k
- 출력: k번째 단어와 글자 수

예제 입력 1

```text
help rescue safe hope
2
```

예제 출력 1

```text
rescue 6
```

예제 입력 2

```text
together smile
1
```

예제 출력 2

```text
together 8
```

### 문제 2. 배터리 그림 그리기 (도전)

틀린 횟수 k(0~6)가 주어질 때, 배터리 6칸 중 남은 칸은 `■`, 쓴 칸은 `□`로 `[■■■■□□]`처럼 출력하고, 다음 줄에 `남은 배터리: n칸`을 출력하세요.

- 입력: 틀린 횟수 k
- 출력: 배터리 그림, `남은 배터리: n칸`

예제 입력 1

```text
2
```

예제 출력 1

```text
[■■■■□□]
남은 배터리: 4칸
```

예제 입력 2

```text
6
```

예제 출력 2

```text
[□□□□□□]
남은 배터리: 0칸
```

정답과 해설은 **[부록] 04-1-02. 2차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-02-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 리스트 = 여러 값을 순서대로 담는 그릇, 인덱스는 0부터
- `random.choice(리스트)`로 무작위로 하나 고른다
- 문자열도 순서가 있어 `len`, 인덱스, `in`을 쓸 수 있다
- 추적표로 입력에 따른 자료의 변화를 먼저 손으로 따라간다

## 수업 흐름 (50분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 5분 | 변수 8개 vs 리스트 1개 비교, 핵심 질문 |
| 전개 1 | 15분 | 리스트·인덱스·append, 문자열 len·in·곱하기 (셸에서 바로 실습) |
| 전개 2 | 20분 | step1 코드 예측·실행·수정, 추적표 채우기 [활동지] |
| 정리 | 10분 | 작은 문제와 자료 짝짓기 발표, 확인 퀴즈 |

## 교사용 메모

- 인덱스가 0부터라는 점을 가장 많이 틀립니다. 단어 카드 8장을 칠판에 붙이고 번호를 0부터 매기며 시작하면 효과적입니다.
- 추적표는 **실행하기 전에** 손으로 채우게 합니다. 예측과 실행 결과가 다른 칸이 바로 배움이 일어나는 곳입니다.
- `"x"`를 guessed에 넣는 이유를 꼭 묻습니다. 7차시 입력 검사(이미 말한 글자)의 복선입니다.
- 3차시에는 `words` 리스트를 뜻이 있는 단어장(딕셔너리)으로 바꿉니다.

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `lesson02_words.py` | [lesson02_words.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/lesson02_words.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/lesson02_words.py) |
| 학습용 PPT | [lesson02_data_structure.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/lesson02_data_structure.pptx) |
| 학생 활동지 | [lesson02_data_structure.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson02_data_structure.md) |
| 코딩 테스트 1 정답 코드 | [lesson02_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson02_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson02_test1.py) |
| 코딩 테스트 2 정답 코드 | [lesson02_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson02_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson02_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
