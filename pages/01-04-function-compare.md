> **1부 게임을 분석하고 설계하기** · 4차시 · 수업 단계: **컴퓨팅 설계**  
> 핵심 개념: 함수, def, 매개변수, return, 반환값, main(), 문제 분해, 재사용

## 학습 목표

1. def로 함수를 정의하고, 매개변수와 반환값을 사용해 호출할 수 있다.
2. 함수 없는 코드와 함수로 나눈 코드를 비교하여 함수의 장점과 한계를 근거를 들어 설명할 수 있다.
3. 하위 문제 하나를 함수 하나로 설계하는 함수 설계표를 작성할 수 있다.

## 핵심 질문

> **똑같이 동작하는 두 코드가 있다. 하나는 함수 없이 위에서 아래로, 하나는 함수로 나누어 썼다. 어느 쪽이 더 '좋은' 코드일까? 왜 그렇게 생각하는가?**

오늘은 함수를 설명부터 듣지 않습니다. **똑같은 게임을 두 가지 방식으로 쓴 코드**를 먼저 실행하고, 읽고, 고쳐 보면서 함수가 왜 필요한지 스스로 찾아냅니다. (PRIMM: 예측 → 실행 → 탐구 → 수정 → 만들기)

| 파일 | 모양 | 줄 수(주석·설명 제외) |
| --- | --- | --- |
| `word_rescue_nofunc.py` | 함수 없이 위에서 아래로 한 덩어리 | 56줄 |
| `word_rescue.py` | 하는 일별로 함수 8개로 나눔 | 69줄 |

아래에서는 두 파일을 줄여서 **nofunc**(`word_rescue_nofunc.py`, 함수 없는 버전)와 **full**(`word_rescue.py`, 함수 버전)이라고 부릅니다.

## 함수의 모양

```python
def make_battery(battery):                        # def 함수이름(매개변수):
    """남은 칸은 ■, 쓴 칸은 □ 로 배터리 그림을 돌려준다"""
    return "■" * battery + "□" * (MAX_BATTERY - battery)   # return 돌려줄 값

print(make_battery(4))        # 함수 호출 → ■■■■□□
img = make_battery(2)         # 돌려받은 값을 변수에 담기 → ■■□□□□
```

| 용어 | 뜻 | 예 |
| --- | --- | --- |
| 정의 | 함수를 만드는 것 | `def make_battery(battery):` |
| 매개변수 | 함수가 받는 값의 이름 | `battery` |
| 호출 | 함수를 실행하는 것 | `make_battery(4)` |
| 반환값 | 함수가 돌려주는 값 | `"■■■■□□"` |

## 활동 1. 예측하고 실행하기 – 두 코드는 정말 같을까?

두 파일을 **같은 순서로 같은 글자**를 넣어 실행해 보세요. 암호는 무작위이므로 짝과 함께 '처음 나온 암호'에 맞춰 입력합니다. 이 책의 검증에서는 무작위 값을 고정해(seed) 세 가지 입력(정상 플레이, 이상한 입력, 실패)으로 실행했더니 **두 파일의 화면이 한 글자도 다르지 않았습니다.**

> 결론 1: 함수로 나누어도 **프로그램이 하는 일은 같다.** 함수는 컴퓨터를 위한 것이 아니라 **코드를 읽고 고치는 사람**을 위한 것이다.

## 활동 2. 탐구하기 – 어느 부분이 어느 함수가 되었나?

`nofunc` 파일에는 `[A]`~`[F]` 표시가 있습니다. 각 구간이 `full` 파일의 어느 함수가 되었는지 짝지어 봅니다. **[활동지]**

| nofunc 구간 | 하는 일 | full 함수 | 받는 값(매개변수) | 돌려주는 값 |
| --- | --- | --- | --- | --- |
| [A] | 암호 고르기 | `pick_word` | `words` | 암호 영단어 1개 |
| [B] | 암호판 만들기 | `make_board` | `word, guessed` | `"h _ _ p"` 같은 문자열 |
| [C] | 배터리 그림 | `make_battery` | `battery` | `"■■■■□□"` 같은 문자열 |
| [D] | 글자 입력·검사 | `ask_letter` | `guessed` | 검사를 통과한 한 글자 |
| [E] | 한 판 진행 | `play` | `word` | `(성공 여부, 틀린 횟수)` |
| [F] | 출동 기록표 출력 | `print_records` | `records` | 없음 (화면 출력) |
| [F] 안쪽 | 화면 칸 수 세기 (한글 2칸) | `text_width` | `text` | 칸 수 (정수) |
| 전체 흐름 | 출동 반복·기록 | `main` | 없음 | 없음 |

이제 `full` 파일의 `main()`만 읽어 보세요. 함수 이름만 보고도 게임 전체 흐름이 **목차처럼** 읽힙니다.

```python
def main():
    print("=== 영단어 구조대 === 암호를 완성해 친구를 구조하세요!")
    records = []
    while True:
        word = pick_word(WORDS)                 # 암호 고르고
        success, wrong = play(word)             # 한 판 하고
        records.append([len(records) + 1, word, "성공" if success else "실패", wrong])
        print_records(records)                  # 기록표 보여 주고
        if input("다시 출동할까요? (y/n) > ").strip().lower() != "y":
            break
```

같은 부분을 `nofunc`에서 찾으면 `while` 안에 `for`, 그 안에 또 `for`와 `for`, `if`가 겹겹이 들어 있어 가장 깊은 곳이 **들여쓰기 5단계**입니다(기록표 출력 부분). `full`은 가장 깊은 곳이 3단계입니다. 함수로 나누면 겹겹이 쌓인 반복이 함수 이름 하나로 접힙니다.

## 활동 3. 수정하기 – 새 기능을 더하면 어디를 고쳐야 할까?

**[실험 A] 단어장 미리보기:** 게임을 시작하기 전에 모든 암호를 첫 글자만 보이게 보여 주는 기능을 더해 봅시다.

함수 코드에서는 이미 있는 `make_board()`를 **다시 쓰면** 됩니다. (2줄 추가)

```python
print("[단어장 미리보기]")
for w in WORDS:
    print(make_board(w, [w[0]]))        # 첫 글자만 '말한 글자'로 넘긴다
```

함수 없는 코드에서는 암호판 만드는 코드를 **복사해서 다시 써야** 합니다. (7줄 추가)

```python
print("[단어장 미리보기]")
for w in WORDS:
    board = []
    for ch in w:
        if ch == w[0]:
            board.append(ch)
        else:
            board.append("_")
    print(" ".join(board))
```

두 코드의 실행 결과는 같습니다.

```text
[단어장 미리보기]
h _ _ _
s _ _ _
h _ _ _
r _ _ _ _ _
f _ _ _ _ _
s _ _ _ _
s _ _ _ _
t _ _ _ t _ _ _
```

> **생각해 보기** 나중에 암호판 모양을 `h _ _ p`에서 `h · · p`로 바꾸기로 했다면? 함수 코드는 `make_board()` **한 곳**만 고치면 되지만, 함수 없는 코드는 복사한 **두 곳**을 모두 찾아 고쳐야 합니다. 한 곳을 빠뜨리면 화면마다 모양이 달라지는 오류가 생깁니다.

**[실험 B] 따로 시험하기:** 파이썬 셸에서 함수 하나만 가져와 시험해 봅니다.

```text
>>> from word_rescue import make_board, make_battery
>>> make_board("help", ["p"])
'_ _ _ p'
>>> make_battery(2)
'■■□□□□'
```

함수 없는 파일은 가져오는 순간 **게임 전체가 시작**되어 버려 암호판 부분만 따로 시험할 수 없습니다.

```text
>>> import word_rescue_nofunc
=== 영단어 구조대 === 암호를 완성해 친구를 구조하세요!
암호판: _ _ _ _ _   배터리: ■■■■■■
알파벳 한 글자 >
```

`full` 파일 맨 아래의 `if __name__ == "__main__":`은 '이 파일을 직접 실행할 때만 `main()`을 부르라'는 뜻입니다. 그래서 다른 파일이나 셸에서 함수만 가져다 쓸 수 있습니다. (8차시 `lesson08_letter_freq.py`도 이 방법으로 단어장을 가져옵니다.)

## 비교 정리 – 함수는 늘 좋을까?

| 비교 기준 | 함수 없는 코드 (nofunc) | 함수로 나눈 코드 (full) |
| --- | --- | --- |
| 실행 결과 | 같다 | 같다 |
| 코드 길이 | **더 짧다** (56줄) | 더 길다 (69줄, def·return이 늘어남) |
| 가장 깊은 들여쓰기 | 5단계 (while 안의 for 안의 for 안의 for 안의 if) | 3단계 |
| 흐름 파악 | 위에서 아래로 끝까지 읽어야 한다 | `main()`만 읽어도 목차처럼 보인다 |
| 같은 일 다시 쓰기 | 코드를 복사해야 한다 (실험 A: 7줄) | 이름으로 부른다 (실험 A: 2줄) |
| 고칠 곳 | 복사한 곳을 모두 찾아야 한다 | 함수 한 곳 |
| 따로 시험하기 | 어렵다 (가져오면 게임이 시작됨) | `make_board("help", ["p"])`처럼 바로 |
| 나누어 만들기(협업) | 한 파일을 함께 고치기 어렵다 | 함수마다 맡아 만들 수 있다 |
| 끝내는 방법 | 결과를 `success` 변수에 담고 `break` | `return`으로 결과를 바로 돌려줌 |
| 한계 | 짧은 프로그램은 오히려 읽기 쉽다 | 함수 사이를 오가며 읽어야 하고, 이름을 잘못 지으면 더 헷갈린다 |

> 결론 2: 함수로 나누면 줄 수가 줄어드는 것이 아니라, **읽기·고치기·다시 쓰기·따로 시험하기**가 쉬워진다. 프로그램이 커지고 같은 일이 여러 번 필요할수록 함수의 힘이 커진다.

## 함수 설계표 – 하위 문제 하나 = 함수 하나

1~3차시에 나눈 작은 문제를 함수로 설계합니다. 함수를 만들기 전에 **이름 · 받는 값 · 돌려주는 값 · 하는 일**을 먼저 정합니다.

| 함수 | 받는 값(매개변수) | 돌려주는 값 | 하는 일 |
| --- | --- | --- | --- |
| `pick_word` | `words` (단어장) | 암호 영단어 1개 | 단어장의 키 중 하나를 무작위로 고르기 |
| `make_board` | `word, guessed` | 암호판 문자열 | 말한 글자는 보이고 나머지는 _로 가리기 |
| `make_battery` | `battery` | 배터리 그림 문자열 | 남은 칸 ■, 쓴 칸 □ |
| `ask_letter` | `guessed` | 알파벳 한 글자 | 한 글자·알파벳·처음 말한 글자일 때까지 다시 묻기 |
| `play` | `word` | `(성공 여부, 틀린 횟수)` | 배터리가 남은 동안 출력 → 입력 → 판단 반복 (5차시) |
| `print_records` | `records` | 없음 | 출동 기록표를 중첩 for 문으로 출력 (6차시) |
| `text_width` | `text` | 화면 칸 수 | 한글은 2칸, 나머지는 1칸으로 세기 (6차시) |
| `main` | 없음 | 없음 | 출동을 반복하며 기록을 쌓고 출력 (전체 흐름 조립) |

```text
main ─┬─ pick_word
      ├─ play ─┬─ make_board
      │        ├─ make_battery
      │        └─ ask_letter
      └─ print_records ── text_width
```

## 전체 코드

두 파일을 화면 두 개에 나란히 띄워 놓고 비교하세요.

### word_rescue_nofunc.py (함수 없는 버전)

```python
"""영단어 구조대 (함수 없는 버전)                              [4차시 비교용]

word_rescue.py 와 하는 일·화면이 똑같은 게임을 '함수(def) 없이'
위에서 아래로 한 덩어리로 쓴 코드입니다.

4차시에는 두 코드를 나란히 놓고
  ① 같은 입력이면 화면도 똑같은지 실행해 확인하고
  ② 이 파일의 [A]~[F] 구간이 full 버전의 어느 함수가 되었는지 짝짓고
  ③ 같은 기능을 더할 때 어느 쪽이 고치기 쉬운지 비교합니다.

구간 표시
  [A] 암호 고르기        → pick_word()
  [B] 암호판 만들기      → make_board()
  [C] 배터리 그림        → make_battery()
  [D] 글자 입력·검사     → ask_letter()
  [E] 한 판 진행         → play()
  [F] 출동 기록표 출력   → print_records(), text_width()
  (전체 흐름)            → main()

실행 방법: python word_rescue_nofunc.py   (Python 3.10 이상)
"""
import random

# 암호 단어장: {영단어(키): 뜻(값)}  - 서로 돕는 말
WORDS = {"help": "도움", "safe": "안전한", "hope": "희망", "rescue": "구조하다",
         "friend": "친구", "share": "나누다", "smile": "미소", "together": "함께"}
MAX_BATTERY = 6          # 구조 신호 배터리 칸 수 = 틀릴 수 있는 횟수

print("=== 영단어 구조대 === 암호를 완성해 친구를 구조하세요!")
records = []                                   # [[출동 번호, 암호, 결과, 틀린 횟수], ...]
while True:
    # [A] 암호 고르기
    word = random.choice(list(WORDS))

    # [E] 한 판 진행 ------------------------------------------------
    guessed = []
    battery = MAX_BATTERY
    success = False                            # 함수가 없으니 결과를 변수에 담아 둔다
    while battery > 0:
        # [B] 암호판 만들기
        board = []
        for ch in word:
            if ch in guessed:
                board.append(ch)
            else:
                board.append("_")
        board = " ".join(board)
        # [C] 배터리 그림
        battery_img = "■" * battery + "□" * (MAX_BATTERY - battery)
        print(f"암호판: {board}   배터리: {battery_img}")
        if "_" not in board:
            print(f"구조 성공! 암호 {word} = {WORDS[word]}")
            success = True
            break                              # return 대신 break 로 반복을 빠져나온다
        # [D] 글자 입력·검사
        while True:
            g = input("알파벳 한 글자 > ").strip().lower()
            if len(g) != 1 or g not in "abcdefghijklmnopqrstuvwxyz":
                print("알파벳 한 글자만 입력하세요.")
            elif g in guessed:
                print("이미 말한 글자예요.")
            else:
                break
        guessed.append(g)
        if g not in word:
            battery -= 1
            print("암호에 없는 글자예요. 신호가 약해집니다.")
    if not success:
        print(f"신호가 끊겼어요. 암호는 {word}({WORDS[word]})였어요.")
    wrong = MAX_BATTERY - battery
    # ----------------------------------------------------------------

    records.append([len(records) + 1, word, "성공" if success else "실패", wrong])

    # [F] 출동 기록표 출력
    for row in [["출동", "암호", "결과", "틀린 횟수"]] + records:
        cells = []
        for item in row:
            text = str(item)
            width = 0                          # 화면 칸 수 세기 (한글은 2칸)
            for ch in text:
                if "가" <= ch <= "힣":
                    width += 2
                else:
                    width += 1
            cells.append(text + " " * (10 - width))
        print(" | ".join(cells).rstrip())

    if input("다시 출동할까요? (y/n) > ").strip().lower() != "y":
        break
print("오늘도 수고했어요, 구조대원님!")
```

### word_rescue.py (함수 버전)

```python
"""영단어 구조대 (수업 모형 기준 완성 코드)

산에서 길을 잃은 친구가 보낸 영어 암호를 알파벳 한 글자씩 맞혀 완성하면 구조 성공!
틀릴 때마다 구조 신호 배터리가 한 칸씩 줄고, 배터리가 0이 되면 신호가 끊긴다.
(행맨과 같은 규칙을 '친구를 구조하는' 이야기로 바꾼 게임)

배우는 것
  - 문자열·리스트 인덱스, in 검사      : make_board(), ask_letter()
  - 딕셔너리 {영단어: 뜻}               : WORDS
  - while 조건 반복과 return            : play()
  - 2차원 리스트와 중첩 for 문          : records, print_records(), text_width()
  - 함수(매개변수·반환값)로 문제 나누기 : 모든 함수

함수 없는 버전(word_rescue_nofunc.py)과 하는 일·화면이 똑같습니다.
4차시에 두 코드를 비교하며 '함수로 나누면 무엇이 좋아지는지' 탐구합니다.

실행 방법: python word_rescue.py   (Python 3.10 이상)
"""
import random

# 암호 단어장: {영단어(키): 뜻(값)}  - 서로 돕는 말
WORDS = {"help": "도움", "safe": "안전한", "hope": "희망", "rescue": "구조하다",
         "friend": "친구", "share": "나누다", "smile": "미소", "together": "함께"}
MAX_BATTERY = 6          # 구조 신호 배터리 칸 수 = 틀릴 수 있는 횟수


def pick_word(words):
    """단어장에서 암호(영단어) 하나를 무작위로 골라 돌려준다"""
    return random.choice(list(words))          # list(words): 딕셔너리의 키만 모은 리스트


def make_board(word, guessed):
    """맞힌 글자는 보여 주고 나머지는 _ 로 가린 암호판 문자열을 돌려준다"""
    board = []
    for ch in word:                            # 암호의 글자를 하나씩
        if ch in guessed:
            board.append(ch)
        else:
            board.append("_")
    return " ".join(board)                     # ["_", "_", "_", "p"] → "_ _ _ p"


def make_battery(battery):
    """남은 칸은 ■, 쓴 칸은 □ 로 배터리 그림 문자열을 돌려준다"""
    return "■" * battery + "□" * (MAX_BATTERY - battery)


def ask_letter(guessed):
    """아직 말하지 않은 알파벳 한 글자가 들어올 때까지 다시 묻고, 그 글자를 돌려준다"""
    while True:
        g = input("알파벳 한 글자 > ").strip().lower()   # 앞뒤 공백 제거, 소문자로
        if len(g) != 1 or g not in "abcdefghijklmnopqrstuvwxyz":
            print("알파벳 한 글자만 입력하세요.")
        elif g in guessed:
            print("이미 말한 글자예요.")
        else:
            return g


def play(word):
    """암호 word 로 한 번 출동한다. (성공 여부, 틀린 횟수)를 돌려준다"""
    guessed = []                               # 지금까지 말한 글자
    battery = MAX_BATTERY
    while battery > 0:                         # 배터리가 남아 있는 동안 반복
        board = make_board(word, guessed)
        print(f"암호판: {board}   배터리: {make_battery(battery)}")
        if "_" not in board:                   # 가린 글자가 없으면 = 모두 맞힘
            print(f"구조 성공! 암호 {word} = {WORDS[word]}")
            return True, MAX_BATTERY - battery
        g = ask_letter(guessed)
        guessed.append(g)
        if g not in word:
            battery -= 1
            print("암호에 없는 글자예요. 신호가 약해집니다.")
    print(f"신호가 끊겼어요. 암호는 {word}({WORDS[word]})였어요.")
    return False, MAX_BATTERY


def text_width(text):
    """화면에서 차지하는 칸 수를 센다 (한글은 2칸, 영문·숫자·기호는 1칸)"""
    width = 0
    for ch in text:
        if "가" <= ch <= "힣":                  # 한글 글자는 화면에서 두 칸
            width += 2
        else:
            width += 1
    return width


def print_records(records):
    """출동 기록표(2차원 리스트)를 중첩 for 문으로 출력한다

    한글은 화면에서 2칸을 차지하므로, 글자 수가 아니라 화면 칸 수(text_width)로
    빈칸을 채워야 표의 세로줄이 맞는다.
    """
    for row in [["출동", "암호", "결과", "틀린 횟수"]] + records:   # 바깥 for: 행
        cells = []
        for item in row:                                            # 안쪽 for: 칸
            text = str(item)
            cells.append(text + " " * (10 - text_width(text)))      # 화면에서 10칸이 되게 채우기
        print(" | ".join(cells).rstrip())


def main():
    print("=== 영단어 구조대 === 암호를 완성해 친구를 구조하세요!")
    records = []                               # [[출동 번호, 암호, 결과, 틀린 횟수], ...]
    while True:
        word = pick_word(WORDS)
        success, wrong = play(word)
        records.append([len(records) + 1, word, "성공" if success else "실패", wrong])
        print_records(records)
        if input("다시 출동할까요? (y/n) > ").strip().lower() != "y":
            break
    print("오늘도 수고했어요, 구조대원님!")


if __name__ == "__main__":
    main()
```

## 실습 활동

1. **예측·실행**: 두 파일을 실행해 같은 화면이 나오는지 확인하세요.
2. **탐구**: nofunc의 `[A]`~`[F]` 구간에 색을 칠하고, full의 함수와 짝지어 대응표를 채우세요. **[활동지]**
3. **수정**: 실험 A(단어장 미리보기)를 두 파일에 모두 해 보고, 추가한 줄 수와 고친 곳의 수를 비교하세요.
4. **시험**: 셸에서 `make_board`, `make_battery`를 가져와 서로 다른 값 3개로 시험해 보세요.
5. **만들기**: 함수 설계표를 보고 `make_battery()`를 직접 만들어 보세요. (빈 파일에서 시작)
6. **토의**: '함수로 나누면 항상 좋은가?'에 대한 내 생각을 근거 2가지와 함께 쓰세요.

활동지: [lesson04_function_compare.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson04_function_compare.md)

## 도전 과제 (기본 · 응용 · 심화)

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | 실험 A를 함수 코드에 넣고 실행하기 |
| 응용 | 맞힌 칸 비율만큼 `구조대 [=====>     ] 친구`를 돌려주는 `rescue_bar(word, guessed)` 함수를 만들어 play()에서 부르기 (코딩 테스트 2) |
| 심화 | nofunc 파일에 실험 A와 '실패했을 때 마지막 암호판 보여 주기'를 모두 넣은 뒤, 암호판 모양을 `·`로 바꾸어 보기. 몇 곳을 고쳐야 했는지 기록하고 함수 코드와 비교하기 |

## 확인 퀴즈

**Q1.** 함수를 정의할 때 쓰는 키워드는?

- ① `func`
- ② `def`
- ③ `function`
- ④ `return`

**Q2.** `def make_board(word, guessed):`에서 괄호 안의 `word`, `guessed`를 무엇이라 하는가?

- ① 반환값
- ② 매개변수
- ③ 전역 상수
- ④ 모듈

**Q3.** `make_battery(2)`의 결과는? (`MAX_BATTERY = 6`)

- ① ■■□□□□
- ② ■■■■□□
- ③ □□■■■■
- ④ 2

**Q4.** 함수 없는 코드(nofunc)와 함수 코드(full)를 비교한 설명으로 옳지 **않은** 것은?

- ① 두 코드는 같은 입력에 같은 화면을 출력한다
- ② 함수 코드는 같은 일을 이름 하나로 다시 쓸 수 있다
- ③ 함수 코드는 make_board() 하나만 따로 실행해 시험할 수 있다
- ④ 함수로 나누면 코드 줄 수가 항상 줄어든다

**Q5.** `if __name__ == "__main__":`의 역할은?

- ① 오류를 막는다
- ② 파일을 직접 실행할 때만 main()을 실행한다
- ③ `main 함수를 정의한다`
- ④ 프로그램을 끝낸다

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. is_rescued 함수 (기본)

암호와 말한 글자 리스트를 받아 암호의 글자를 모두 맞혔으면 `True`, 아니면 `False`를 돌려주는 함수 `is_rescued(word, guessed)`를 만드세요. 첫째 줄에 암호, 둘째 줄에 n, 다음 n줄에 말한 글자들(공백 없이)이 주어지면 각 줄에 대한 함수의 결과를 출력합니다.

- 입력: 암호, n, n줄의 말한 글자들
- 출력: 각 줄의 `True` / `False`

예제 입력 1

```text
safe
3
efas
saf
zsafe
```

예제 출력 1

```text
True
False
True
```

### 문제 2. 구조대 위치 함수 (도전)

맞힌 칸의 비율만큼 구조대가 친구에게 다가가는 그림을 돌려주는 함수 `rescue_bar(word, guessed)`를 만드세요. 공개된 칸 수를 a라 할 때 막대 칸 수는 `a * 10 // len(word)`이고, `구조대 [` + `=` × 칸 + `>` + 공백 × (10 - 칸) + `] 친구` 모양입니다. 입력 형식은 문제 1과 같습니다.

- 입력: 암호, n, n줄의 말한 글자들
- 출력: 각 줄의 구조대 위치 그림

예제 입력 1

```text
help
3
z
hp
help
```

예제 출력 1

```text
구조대 [>          ] 친구
구조대 [=====>     ] 친구
구조대 [==========>] 친구
```

정답과 해설은 **[부록] 04-1-04. 4차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-04-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- `def 이름(매개변수):`로 만들고, `return`으로 값을 돌려준다
- 함수로 나누어도 프로그램이 하는 일은 같다 – 함수는 **사람**을 위한 것
- 함수의 장점: 흐름이 목차처럼 읽힘, 같은 일을 이름으로 다시 씀, 고칠 곳이 한 곳, 따로 시험 가능
- 함수의 한계: 줄 수가 늘 수 있고, 함수 사이를 오가며 읽어야 한다 → 이름을 잘 짓는 것이 중요
- 하위 문제 하나 = 함수 하나, 만들기 전에 함수 설계표부터

## 수업 흐름 (50분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 5분 | 두 코드 화면을 나란히 보여 주고 '어느 쪽이 좋은 코드일까?' 손 들기 (근거 없이 먼저 선택) |
| 예측·실행 | 7분 | 두 파일 실행, 같은 화면 확인 → 결론 1 |
| 탐구 | 13분 | nofunc 구간 색칠, 대응표 채우기, main() 목차 읽기 [활동지] |
| 수정 | 12분 | 실험 A(미리보기)를 두 파일에 추가, 줄 수·고칠 곳 비교 / 실험 B 셸에서 따로 시험 |
| 만들기 | 6분 | make_battery() 직접 만들기, 함수 설계표 확인 |
| 정리 | 7분 | 비교 정리표 완성, '함수는 늘 좋을까?' 토의 → 결론 2, 처음 선택 다시 보기 |

## 교사용 메모

- **비교 수업의 핵심은 '같은 결과'를 먼저 확인하는 것**입니다. 결과가 같다는 것을 확인해야 학생이 '그럼 왜 나누지?'라는 질문을 스스로 갖습니다.
- 줄 수는 함수 코드가 더 깁니다(69줄 대 56줄). 이 사실을 숨기지 말고 먼저 보여 주세요. '짧은 코드 = 좋은 코드'라는 오해를 바로잡는 좋은 기회입니다.
- 실험 A에서 학생들은 nofunc에 코드를 복사하다가 `ch in guessed`를 `ch == w[0]`으로 바꾸는 것을 자주 놓칩니다. 이 실수 자체가 '복사의 위험'을 보여 주는 살아 있는 예시입니다.
- 두 파일을 화면 양쪽에 띄우거나 인쇄해 나눠 주고 형광펜으로 구간을 칠하게 하면 대응 관계가 잘 보입니다.
- 이 차시에는 play()와 print_records()의 **안쪽 동작**까지 다 이해하지 않아도 됩니다. '무엇을 받고 무엇을 돌려주는지'만 알면 되고, 안쪽은 5·6차시에 직접 완성합니다.
- 중학교에서는 실험 A까지만 하고, 비교 정리표는 교사가 함께 채웁니다.

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `word_rescue_nofunc.py` | [word_rescue_nofunc.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/word_rescue_nofunc.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/word_rescue_nofunc.py) |
| 소스코드 `word_rescue.py` | [word_rescue.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/word_rescue.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/word_rescue.py) |
| 학습용 PPT | [lesson04_function_compare.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/lesson04_function_compare.pptx) |
| 학생 활동지 | [lesson04_function_compare.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson04_function_compare.md) |
| 코딩 테스트 1 정답 코드 | [lesson04_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson04_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson04_test1.py) |
| 코딩 테스트 2 정답 코드 | [lesson04_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson04_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson04_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
