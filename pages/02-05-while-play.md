> **2부 게임 구현하기** · 5차시 · 수업 단계: **구현**  
> 핵심 개념: while 조건 반복, 종료 조건, return, 값 두 개 돌려주기, 무한 반복, for와 while

## 학습 목표

1. while 문의 반복 조건과 return으로 게임이 끝나는 두 경우(성공·실패)를 설계할 수 있다.
2. 4차시에 설계한 함수를 조립하여 영단어 구조대의 한 판(play)을 완성하고 규칙을 바꿀 수 있다.

## 핵심 질문

> **컴퓨터는 언제까지 글자를 물어봐야 할까? 게임은 언제, 어떻게 끝나야 할까?**

몇 번 입력할지 미리 알 수 없습니다. 3번 만에 맞힐 수도, 12번이 걸릴 수도 있습니다. 이렇게 **횟수가 정해지지 않은 반복**에는 `while` 문을 씁니다.

## while 조건: 조건이 참인 동안 반복

```python
battery = 3
while battery > 0:          # 배터리가 남아 있는 동안
    print("■" * battery)
    battery -= 1            # 조건에 쓰인 변수를 반드시 바꾼다!
print("신호 끊김")
```

```text
■■■
■■
■
신호 끊김
```

| 반복 | battery | `battery > 0` | 실행 |
| --- | --- | --- | --- |
| 1 | 3 | True | ■■■ 출력, 2로 |
| 2 | 2 | True | ■■ 출력, 1로 |
| 3 | 1 | True | ■ 출력, 0으로 |
| 4 | 0 | **False** | 반복 끝 → 신호 끊김 |

## play(): 게임이 끝나는 두 가지 길

```python
def play(word):
    guessed = []
    battery = MAX_BATTERY
    while battery > 0:                          # 끝나는 길 ②: 배터리가 0이면 반복이 끝난다
        board = make_board(word, guessed)
        print(f"암호판: {board}   배터리: {make_battery(battery)}")
        if "_" not in board:                    # 끝나는 길 ①: 모두 맞히면
            print(f"구조 성공! 암호 {word} = {WORDS[word]}")
            return True, MAX_BATTERY - battery  # 반복 중이어도 함수가 바로 끝난다
        g = ask_letter(guessed)
        guessed.append(g)
        if g not in word:
            battery -= 1
            print("암호에 없는 글자예요. 신호가 약해집니다.")
    print(f"신호가 끊겼어요. 암호는 {word}({WORDS[word]})였어요.")
    return False, MAX_BATTERY
```

| 끝나는 길 | 언제 | 어떻게 끝나나 | 돌려주는 값 |
| --- | --- | --- | --- |
| ① 구조 성공 | 암호판에 `_`가 없을 때 | `return`이 반복과 함수를 함께 끝냄 | `(True, 틀린 횟수)` |
| ② 신호 끊김 | `battery`가 0이 되어 조건이 거짓일 때 | while 반복이 끝나고 아래 줄 실행 | `(False, 6)` |

> **왜 성공 검사가 입력보다 먼저일까?** 마지막 글자를 맞히면 다음 반복의 처음에서 바로 '구조 성공'으로 끝나야 합니다. 검사가 입력보다 뒤에 있으면, 이미 다 맞혔는데도 한 글자를 더 물어보게 됩니다.

## 값 두 개를 돌려주고 나누어 받기

```python
success, wrong = play("help")     # (True, 1) → success = True, wrong = 1
```

`return True, MAX_BATTERY - battery`처럼 쉼표로 여러 값을 돌려줄 수 있습니다. main()은 이 두 값을 받아 출동 기록표에 씁니다(6차시).

## 끝나지 않는 반복 (오류 찾기)

`battery -= 1`을 지우고 틀린 글자만 계속 넣으면 `battery`가 계속 6이라 조건이 늘 참입니다. 게임이 끝나지 않으면 **Ctrl + C**로 멈춥니다.

> while 조건에 쓰인 변수는 반복 안에서 **반드시 바뀌어야** 한다.

## for와 while 비교

| | for | while |
| --- | --- | --- |
| 쓰는 때 | 횟수(또는 대상)가 정해진 반복 | 조건으로 끝나는 반복 |
| 영단어 구조대에서 | 암호의 글자 하나씩 (`make_board`), 기록표의 행 하나씩 | 배터리가 남은 동안 (`play`), 올바른 입력이 들어올 때까지 (`ask_letter`) |

## 실행 예시

`play("help")`에 h → x → e → l → p를 입력한 화면입니다. 2차시 추적표와 비교해 보세요.

```text
암호판: _ _ _ _   배터리: ■■■■■■
알파벳 한 글자 > h
암호판: h _ _ _   배터리: ■■■■■■
알파벳 한 글자 > x
암호에 없는 글자예요. 신호가 약해집니다.
암호판: h _ _ _   배터리: ■■■■■□
알파벳 한 글자 > e
암호판: h e _ _   배터리: ■■■■■□
알파벳 한 글자 > l
암호판: h e l _   배터리: ■■■■■□
알파벳 한 글자 > p
암호판: h e l p   배터리: ■■■■■□
구조 성공! 암호 help = 도움
(True, 1)
```

## 전체 코드

### lesson05_play_blank.py (빈칸 채우기)

```python
"""영단어 구조대 - play() 빈칸 채우기                          [5차시]

word_rescue.py 의 play() 함수에서 6곳을 비웠습니다.
①~⑥을 채운 뒤 실행하세요. (빈칸이 남아 있으면 SyntaxError 가 납니다)

  ① 반복 조건 : 배터리가 남아 있는 동안
  ② 성공 조건 : 암호판에 _ 가 하나도 없으면
  ③ 돌려줄 값 : (성공 여부, 틀린 횟수)
  ④ 말한 글자를 guessed 에 기록
  ⑤ 입력한 글자가 암호에 없으면
  ⑥ 배터리 한 칸 줄이기

정답: lesson05_play_answer.py
실행 방법: python lesson05_play_blank.py
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
    while ____①____:                           # 배터리가 남아 있는 동안 반복
        board = make_board(word, guessed)
        print(f"암호판: {board}   배터리: {make_battery(battery)}")
        if ____②____:                          # 가린 글자가 없으면 = 모두 맞힘
            print(f"구조 성공! 암호 {word} = {WORDS[word]}")
            return ____③____                   # (성공 여부, 틀린 횟수)
        g = ask_letter(guessed)
        ____④____                              # 말한 글자 기록
        if ____⑤____:
            ____⑥____
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

정답 파일: `lesson05_play_answer.py` (완성 코드는 `word_rescue.py`와 같습니다)

## 실습 활동

1. **예측**: `play("help")`에 h → x → e → l → p를 넣을 때 화면을 활동지에 먼저 예측하고 실행해 비교하세요. **[활동지]**
2. **순서도 카드**: 암호판 출력 → 성공 검사 → 글자 입력 → guessed에 추가 → 없으면 배터리 감소 → 조건 다시 검사, 6장의 카드를 순서대로 놓으세요.
3. **빈칸 채우기**: `lesson05_play_blank.py`의 ①~⑥을 채워 게임을 완성하세요.
4. **짝과 바꾸기** (짝 프로그래밍: 한 명 입력, 한 명 확인, 미션마다 역할 교대)
   - 미션 ① `MAX_BATTERY = 8`로 바꾸어 쉬운 모드 만들기
   - 미션 ② 단어장 `WORDS`에 서로 돕는 말 2개 추가하기
   - 미션 ③ (도전) 출동이 끝나면 틀린 글자 기록 출력하기
5. **오류 찾기**: `battery -= 1`을 주석 처리하고 실행해 끝나지 않는 반복을 확인한 뒤 Ctrl + C로 멈추세요.

활동지: [lesson05_while_play.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson05_while_play.md)

## 도전 과제 (기본 · 응용 · 심화)

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | 미션 ①, ② 완성하기 |
| 응용 | 구조에 성공하면 '틀린 횟수 n번'도 함께 출력하기 (`MAX_BATTERY - battery`) |
| 심화 | 미션 ③ 틀린 글자 기록을 출력하는 `print_report(word, guessed, battery)` 함수를 만들어 성공·실패 두 곳에서 부르기 (부록 04-7 산출물 예시 A-상 참고) |

## 확인 퀴즈

**Q1.** `while battery > 0:`의 뜻으로 알맞은 것은?

- ① 배터리가 0이 될 때까지 한 번만 실행
- ② 배터리가 남아 있는 동안 반복
- ③ 배터리가 0이면 반복
- ④ 배터리를 0으로 만든다

**Q2.** play() 안에서 `"_" not in board`가 참이 되는 때는?

- ① 배터리가 0칸일 때
- ② 암호의 글자를 모두 맞혔을 때
- ③ 처음 시작할 때
- ④ 틀린 글자를 말했을 때

**Q3.** `return True, MAX_BATTERY - battery`에 대한 설명으로 옳은 것은?

- ① 반복만 끝나고 함수는 계속된다
- ② 값 두 개를 한 번에 돌려주고 함수가 끝난다
- ③ `True만 돌려준다`
- ④ 반복문 안에서는 쓸 수 없다

**Q4.** play()에서 `battery -= 1`을 지우고 틀린 글자만 계속 입력하면?

- ① 바로 구조 성공
- ② 반복이 끝나지 않는다
- ③ 오류가 나며 멈춘다
- ④ 배터리가 2칸씩 준다

**Q5.** 구조대 게임의 글자 입력 반복에 for보다 while이 알맞은 까닭은?

- ① `while이 더 빠르다`
- ② 몇 번 입력할지 미리 알 수 없다
- ③ `for 문은 문자열에 쓸 수 없다`
- ④ `while은 들여쓰기가 필요 없다`

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 배터리가 다 닳을 때까지 (기본)

처음 배터리 칸 수 n(1~10)이 주어집니다. while 문으로 배터리가 0이 될 때까지 한 칸씩 줄이며 `■`를 남은 칸 수만큼 출력하고 옆에 `(n칸)`을 붙이세요. 0칸이 되면 `신호 끊김`을 출력합니다.

- 입력: 처음 배터리 칸 수 n
- 출력: 줄어드는 배터리, `신호 끊김`

예제 입력 1

```text
3
```

예제 출력 1

```text
■■■ (3칸)
■■ (2칸)
■ (1칸)
신호 끊김
```

예제 입력 2

```text
1
```

예제 출력 2

```text
■ (1칸)
신호 끊김
```

### 문제 2. 구조 출동 시뮬레이션 (도전)

첫째 줄에 암호, 둘째 줄에 입력할 알파벳들이 한 줄로 주어집니다(중복 없음). 앞에서부터 한 글자씩 게임 규칙(배터리 6칸)대로 처리하여, 모두 맞히면 `구조 성공! 틀린 횟수 n`, 배터리가 0칸이 되면 `신호 끊김`, 글자를 다 써도 끝나지 않으면 `암호 미완성`을 출력하세요. 게임이 끝나면 남은 글자는 무시합니다.

- 입력: 암호, 알파벳들
- 출력: `구조 성공! 틀린 횟수 n` / `신호 끊김` / `암호 미완성`

예제 입력 1

```text
help
zeahlp
```

예제 출력 1

```text
구조 성공! 틀린 횟수 2
```

예제 입력 2

```text
hope
trisaxn
```

예제 출력 2

```text
신호 끊김
```

예제 입력 3

```text
friend
fr
```

예제 출력 3

```text
암호 미완성
```

정답과 해설은 **[부록] 04-1-05. 5차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-05-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- `while 조건:` → 조건이 참인 동안 반복, 조건에 쓰인 변수는 반복 안에서 바뀌어야 한다
- 한 판이 끝나는 길은 두 가지: `return`(구조 성공), 조건이 거짓(배터리 0)
- `return a, b`로 값 두 개를 돌려주고 `x, y = 함수()`로 나누어 받는다
- 횟수가 정해지면 for, 조건으로 끝나면 while

## 수업 흐름 (50분 기준, 교사용) – 본시

교육청 수업 모형 문서의 「Ⅲ. 5차시 수업 지도안」과 같은 흐름입니다. (부록 04-8 참고)

| 단계 | 시간 | 핵심 질문 | 활동 |
| --- | --- | --- | --- |
| 동기 유발 | 5분 | “컴퓨터는 언제까지 글자를 물어봐야 할까?” | 칠판에 `_ _ _ _`, 종이 구조대 한 판 → 멈추는 두 경우 찾기 |
| 학습 목표 | 2분 | | 목표 2개 안내 |
| 개념 확인 | 8분 | “횟수가 정해지지 않은 반복은 어떻게 쓸까?” | while 조건, 반복 안의 return, 퀵 퀴즈 |
| 탐구 1 | 7분 | “실행하기 전에 화면을 먼저 맞혀 볼까?” | play("help") 예측 → 실행 비교 [활동지] |
| 탐구 2 | 8분 | “play() 안에서 일이 어떤 순서로 일어날까?” | 순서도 카드 배열, 성공 검사가 먼저인 이유, 값 두 개 반환 |
| 탐구 3 | 10분 | “게임 규칙을 바꾸려면 어디를 고치면 될까?” | 빈칸 채우기, 짝과 미션 ①~③ |
| 오류 찾기 | 3분 | “battery -= 1을 지우면 어떻게 될까?” | 끝나지 않는 반복, Ctrl + C |
| 생각 넓히기 | 2분 | “for 문으로도 만들 수 있을까?” | for와 while 비교 |
| 정리 | 5분 | “여러 번 출동한 결과는 어떻게 모아 둘까?” | 출구 티켓 3문항, 6차시 예고 |

## 교사용 메모

- 동기 유발의 종이 게임은 교사가 암호를 정하고 학생들이 돌아가며 글자를 말하게 합니다. 칠판의 배터리 칸을 지우며 진행하면 '조건이 거짓이 되는 순간'이 눈에 보입니다.
- 순서도 카드는 모둠별로 6장씩 인쇄해 섞어 나눠 줍니다. '성공 검사'를 '글자 입력' 뒤에 놓은 모둠이 있으면 그대로 실행해 보게 하세요(한 글자를 더 묻게 됨).
- 끝나지 않는 반복은 학생이 겁먹지 않게 '일부러 만들어 보는 오류'로 안내하고, IDLE에서는 Ctrl + C 또는 셸 창의 [Shell] → [Interrupt Execution]으로 멈춘다는 것을 미리 보여 줍니다.
- 출구 티켓 예: ① `while battery > 0`의 뜻 ② `make_battery(4)`의 결과 ③ 구조 성공 조건식 (정답: 배터리가 남은 동안 반복 / ■■■■□□ / `"_" not in board`)

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `lesson05_play_blank.py` | [lesson05_play_blank.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/lesson05_play_blank.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/lesson05_play_blank.py) |
| 소스코드 `lesson05_play_answer.py` | [lesson05_play_answer.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/lesson05_play_answer.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/lesson05_play_answer.py) |
| 소스코드 `word_rescue.py` | [word_rescue.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/word_rescue.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/word_rescue.py) |
| 학습용 PPT | [lesson05_while_play.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/lesson05_while_play.pptx) |
| 학생 활동지 | [lesson05_while_play.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson05_while_play.md) |
| 코딩 테스트 1 정답 코드 | [lesson05_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson05_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson05_test1.py) |
| 코딩 테스트 2 정답 코드 | [lesson05_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson05_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson05_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
