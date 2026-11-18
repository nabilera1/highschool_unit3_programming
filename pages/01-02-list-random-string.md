> **1부 게임을 분석하고 기본 버전 만들기** · 2차시 · 수업 단계: **문제 구조화**  
> 핵심 개념: 리스트, 인덱스, random.choice, len, in, 문자열

## 학습 목표

1. 리스트를 만들고 인덱스로 항목을 꺼낼 수 있다.
2. random.choice()로 리스트에서 무작위 항목을 고를 수 있다.
3. 문자열의 len(), 인덱스, in 연산자를 사용할 수 있다.

## 핵심 질문

> **단어 8개를 변수 8개에 따로 저장하면 어떤 점이 불편할까?**

게임을 시작하려면 먼저 **암호 단어장**이 있어야 하고, 그중 하나를 **무작위로** 골라야 합니다. 단어가 8개라고 변수를 8개 만들면 무작위로 고르기도, 단어를 추가하기도 어렵습니다.

**리스트**는 여러 값을 순서대로 한 변수에 담는 자료구조입니다. 오늘은 리스트와 `random`으로 암호를 고르고, 문자열을 다루는 기본 도구를 익힙니다.

## 리스트: 여러 값을 한 변수에

```python
words = ['help', 'rescue', 'safe', 'hope']   # 대괄호 [ ], 쉼표로 구분

print(len(words))     # 4      → 항목 개수
print(words[0])       # help   → 인덱스는 0부터!
print(words[3])       # hope
print(words[-1])      # hope   → -1 은 맨 뒤
words.append('smile') # 맨 뒤에 항목 추가
print(words)          # ['help', 'rescue', 'safe', 'hope', 'smile']
```

| 인덱스 | 0 | 1 | 2 | 3 |
| --- | --- | --- | --- | --- |
| 값 | 'help' | 'rescue' | 'safe' | 'hope' |

항목이 4개면 인덱스는 0~3입니다. `words[4]`는 **IndexError** 오류가 납니다.

## random.choice: 무작위로 하나 고르기

```python
import random                       # 무작위 기능 불러오기

비밀단어 = random.choice(words)      # 리스트에서 아무거나 하나
print(비밀단어)                      # 실행할 때마다 다름
```

`random.choice(리스트)`는 리스트의 항목 중 하나를 같은 확률로 고릅니다. 단어가 8개면 각 단어가 뽑힐 확률은 1/8입니다.

## 문자열도 '글자들의 순서'

문자열은 글자가 순서대로 늘어선 것이라 리스트와 비슷하게 다룰 수 있습니다.

```python
비밀단어 = 'help'
print(len(비밀단어))      # 4      → 글자 수
print(비밀단어[0])        # h      → 첫 글자
print('e' in 비밀단어)    # True   → 'e' 가 들어 있나?
print('z' in 비밀단어)    # False
print('_ ' * 4)           # _ _ _ _  → 문자열 반복
```

| 표현 | 뜻 | 결과 |
| --- | --- | --- |
| `len('help')` | 글자 수 | 4 |
| `'help'[1]` | 1번 글자 | 'e' |
| `'p' in 'help'` | 포함 여부 | True |
| `'ab' + 'c'` | 이어 붙이기 | 'abc' |
| `'=' * 5` | 반복 | '=====' |

## 실행 예시

`new_rescue_step1_secret.py`를 실행한 화면입니다. `>` 뒤의 글자가 키보드로 입력한 값입니다. `e`를 입력한 예입니다. (암호는 무작위로 정해지므로 실행할 때마다 달라집니다.)

```text
단어장에 들어 있는 단어 수: 8
첫 번째 단어: help
마지막 단어: smile

[SOS] 친구의 구조 신호가 도착했어요!
암호의 글자 수: 4
암호의 첫 글자: h
밑줄 암호: _ _ _ _ 
알파벳 한 글자 > e
e 는(은) 암호에 있어요!
정답 암호는 hope 였어요. (다음 차시에는 밑줄 암호판을 만들어요)
```

## 전체 코드

이번 차시의 **전체 프로그램**입니다. 주석(`#` 뒤의 설명)을 함께 읽으며 따라가 보세요.

1. 코드 블록 전체를 복사합니다. (코드 블록 오른쪽 위 복사 버튼 또는 드래그 후 Ctrl + C)
2. IDLE에서 **File → New File**을 열고 붙여 넣습니다. (Ctrl + V)
3. 아래 파일 이름으로 저장한 뒤 **F5**로 실행합니다. (VS Code는 ▶ 실행 버튼)

### new_rescue_step1_secret.py

```python
# =====================================================================
# 영단어 구조대 - 1단계: 암호(비밀 단어) 고르기          [2차시]
#
# 이번 단계에서 배우는 것
#   - 리스트      : 여러 단어를 한 변수에 순서대로 담는다.  words[0] → 'help'
#   - random.choice: 리스트에서 하나를 무작위로 고른다.
#   - 문자열      : len()으로 글자 수, 인덱스로 한 글자, in 으로 포함 여부 확인
#
# 실행 방법: python new_rescue_step1_secret.py
# =====================================================================
import random                     # 무작위(랜덤) 기능을 쓰기 위해 불러온다

# 암호 단어장 (리스트) - 대괄호 [ ] 안에 쉼표로 구분해서 담는다
# ← 여기에 '사람을 돕는' 영단어를 더 넣어 보세요!
words = ['help', 'rescue', 'safe', 'hope', 'friend', 'doctor', 'together', 'smile']

print('단어장에 들어 있는 단어 수:', len(words))   # len(리스트) → 항목 개수 8
print('첫 번째 단어:', words[0])                    # 인덱스는 0부터 시작
print('마지막 단어:', words[-1])                    # -1 은 맨 뒤 항목

# 1) 암호를 무작위로 하나 고른다
비밀단어 = random.choice(words)

# 2) 암호에 대한 정보 알려 주기 (암호 자체는 숨긴다!)
print()
print('[SOS] 친구의 구조 신호가 도착했어요!')
print('암호의 글자 수:', len(비밀단어))             # len(문자열) → 글자 수
print('암호의 첫 글자:', 비밀단어[0])               # 문자열도 인덱스로 한 글자를 꺼낼 수 있다
print('밑줄 암호:', '_ ' * len(비밀단어))           # 문자열 * 정수 → 반복  '_ ' * 4 → '_ _ _ _ '

# 3) 알파벳 한 글자를 입력받아 암호 안에 있는지 확인
guess = input('알파벳 한 글자 > ')
if guess in 비밀단어:                               # in : 문자열 안에 그 글자가 있으면 True
    print(guess, '는(은) 암호에 있어요!')
else:
    print(guess, '는(은) 암호에 없어요.')

print('정답 암호는', 비밀단어, '였어요. (다음 차시에는 밑줄 암호판을 만들어요)')
```

파일 받기: [new_rescue_step1_secret.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_step1_secret.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_step1_secret.py)

## 실습 활동

1. `new_rescue_step1_secret.py`를 실행해 암호가 매번 바뀌는지 확인하세요.
2. `words` 리스트에 '사람을 돕는' 영단어를 3개 추가해 보세요. (예: nurse, care, thanks)
3. 암호의 **마지막 글자**를 힌트로 출력하는 줄을 추가해 보세요.
4. `words[8]`을 출력하면 어떤 오류가 나는지 확인하고 이유를 적으세요.

활동지: [new_ws02-list-random-string.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws02-list-random-string.md)

## 도전 과제 (기본 · 응용 · 심화)

자신의 속도에 맞게 골라 도전하세요. 기본을 마치면 응용, 응용을 마치면 심화로!

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | 단어장에 단어를 추가하고 `len(words)`가 바뀌는 것을 확인하기 |
| 응용 | 암호의 첫 글자와 마지막 글자를 함께 힌트로 보여 주기 |
| 심화 | `random.randint()`와 인덱스로 `random.choice()`와 같은 일을 하는 코드 만들기 |

## 확인 퀴즈

**Q1.** `words = ['help', 'safe', 'hope']`일 때 `words[1]`의 값은?

- ① help
- ② safe
- ③ hope
- ④ 오류

**Q2.** `len('rescue')`의 값은?

- ① 5
- ② 6
- ③ 7
- ④ 'rescue'

**Q3.** `'e' in 'help'`의 결과는?

- ① True
- ② False
- ③ 1
- ④ 오류

**Q4.** 리스트에서 항목 하나를 무작위로 고르는 함수는?

- ① random.pick()
- ② random.choice()
- ③ random.list()
- ④ choice.random()

**Q5.** `words = ['a', 'b', 'c']`일 때 오류가 나는 것은?

- ① words[0]
- ② words[2]
- ③ words[-1]
- ④ words[3]

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

### 문제 2. 가장 긴 암호, 가장 짧은 암호 (도전)

첫째 줄에 단어들이 공백으로 구분되어 주어집니다. 가장 긴 단어와 가장 짧은 단어를 찾아 출력하세요. 길이가 같으면 먼저 나온 단어를 고릅니다.

- 입력: 단어들 (공백 구분)
- 출력: `가장 긴 암호: 단어 (n글자)`, `가장 짧은 암호: 단어 (n글자)`

예제 입력 1

```text
help rescue safe together hope
```

예제 출력 1

```text
가장 긴 암호: together (8글자)
가장 짧은 암호: help (4글자)
```

예제 입력 2

```text
a bb cc d
```

예제 출력 2

```text
가장 긴 암호: bb (2글자)
가장 짧은 암호: a (1글자)
```

정답과 해설은 **[부록] 04-1-02. 2차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-02-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 리스트는 여러 값을 순서대로 담는다, 인덱스는 0부터
- random.choice(리스트)로 무작위 암호 고르기
- 문자열: len()으로 글자 수, [i]로 한 글자, in으로 포함 여부
- '_ ' * n 처럼 문자열 반복으로 밑줄 만들기

## 수업 흐름 (45분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 5분 | 변수 8개 vs 리스트 1개 비교 |
| 전개 1 | 15분 | 리스트·인덱스·random.choice 실습 |
| 전개 2 | 15분 | 문자열 len·인덱스·in, 단어장 만들기 |
| 정리 | 10분 | 확인 퀴즈, 코딩 테스트 1 |

## 교사용 메모

- 리스트와 문자열이 **같은 방식**(인덱스, len, in)으로 다뤄진다는 점을 강조하면 3차시 for 반복이 쉬워집니다.
- 중학생 학급은 활동지의 '구조 단어장 만들기'에 시간을 더 주고, 만든 단어장을 실제 코드에 넣어 실행하게 하면 몰입도가 높습니다.
- 단어장에는 **소문자 알파벳만** 쓰도록 안내합니다. 대문자나 공백이 섞이면 이후 차시의 비교가 어긋납니다.

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `new_rescue_step1_secret.py` | [new_rescue_step1_secret.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_step1_secret.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_step1_secret.py) |
| 학습용 PPT | [new_02-list-random-string.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/new_02-list-random-string.pptx) |
| 학생 활동지 | [new_ws02-list-random-string.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws02-list-random-string.md) |
| 코딩 테스트 1 정답 코드 | [new_ch02_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch02_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch02_test1.py) |
| 코딩 테스트 2 정답 코드 | [new_ch02_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch02_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch02_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
