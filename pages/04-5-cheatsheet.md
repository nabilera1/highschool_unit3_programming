## 입출력과 변수

| 코드 | 뜻 | 영단어 구조대에서 |
| --- | --- | --- |
| `g = input("> ")` | 키보드 입력(항상 문자열) | 알파벳 한 글자 받기 |
| `print(a, b)` | 출력 (사이에 공백) | 화면 보여 주기 |
| `print(x, end=" ")` | 줄을 바꾸지 않고 이어서 출력 | 성공한 암호 이어 쓰기 |
| `sep.join(cells)` | 리스트의 칸들을 구분 문자열 sep으로 이어 한 줄로 | 기록표 한 행 (sep = 세로줄) |
| `f"배터리: {battery}칸"` | 변수 값을 끼운 문자열 | 안내 문구 |
| `MAX_BATTERY = 6` | 바뀌지 않는 값(상수)은 대문자 이름 | 배터리 칸 수 |

## 문자열

| 코드 | 결과 | 뜻 |
| --- | --- | --- |
| `len("help")` | `4` | 글자 수 |
| `"help"[0]`, `"help"[-1]` | `"h"`, `"p"` | 0번 글자, 맨 뒤 글자 |
| `"e" in "help"` | `True` | 들어 있나? |
| `" H ".strip().lower()` | `"h"` | 앞뒤 공백 제거, 소문자 |
| `"■" * 3` | `"■■■"` | 반복해 이어 붙이기 |
| `" ".join(["h", "_"])` | `"h _"` | 리스트를 공백으로 이어 붙이기 |

## 조건과 반복

| 코드 | 뜻 |
| --- | --- |
| `if g not in word:` / `elif` / `else:` | 조건에 따라 나누기 |
| `for ch in word:` | 글자(값)를 하나씩 – 횟수가 정해진 반복 |
| `for i in range(3):` | 3번 반복 (i = 0, 1, 2) |
| `while battery > 0:` | 조건이 참인 동안 반복 – 조건 변수는 반복 안에서 바꾸기! |
| `while True:` … `break` / `return` | 계속 반복하다가 원할 때 끝내기 |
| `"성공" if success else "실패"` | 한 줄짜리 조건 |

## 자료구조

| 자료구조 | 만들기 | 꺼내기 | 추가 | 영단어 구조대 |
| --- | --- | --- | --- | --- |
| 리스트 | `guessed = []` | `guessed[0]` | `guessed.append("h")` | 말한 글자, 암호판 |
| 딕셔너리 | `WORDS = {"help": "도움"}` | `WORDS["help"]` | `WORDS["care"] = "돌봄"` | 단어장 |
| 2차원 리스트 | `records = []` | `records[1][2]` (행, 칸) | `records.append([1, "help", "성공", 1])` | 출동 기록표 |

| 자주 쓰는 것 | 뜻 |
| --- | --- |
| `list(WORDS)` | 딕셔너리의 키만 모은 리스트 |
| `"help" in WORDS` | 키가 있나? (없는 키를 꺼내면 KeyError) |
| `len(records)` | 행의 개수 |
| `for row in records:` → `row[2]` | 행을 하나씩 꺼내 칸 읽기 |

## 함수

```python
def make_battery(battery):          # def 이름(매개변수):
    """하는 일 설명"""
    return "■" * battery + "□" * (MAX_BATTERY - battery)   # 돌려줄 값

img = make_battery(4)               # 호출하고 돌려받기 → "■■■■□□"
success, wrong = play("help")       # 값 두 개 나누어 받기

if __name__ == "__main__":          # 직접 실행할 때만 main() 실행
    main()
```

| 함수 이름 | 받는 값 | 돌려주는 값 |
| --- | --- | --- |
| `pick_word(words)` | 단어장 | 암호 영단어 |
| `make_board(word, guessed)` | 암호, 말한 글자 | `"h _ _ p"` |
| `make_battery(battery)` | 남은 칸 수 | `"■■■■□□"` |
| `ask_letter(guessed)` | 말한 글자 | 검사를 통과한 한 글자 |
| `play(word)` | 암호 | `(성공 여부, 틀린 횟수)` |
| `print_records(records)` | 기록표 | 없음 (출력) |
| `text_width(text)` | 글자 | 화면 칸 수 (한글 2칸) |

## 한글이 섞인 표 줄 맞추기

화면에서 영문·숫자는 1칸, 한글은 **2칸**입니다. `f"{x:<8}"`처럼 글자 수로 채우면 한글 칸이 어긋나므로, 화면 칸 수를 세어 빈칸을 채웁니다.

```python
text + " " * (10 - text_width(text))    # 화면에서 10칸이 되게
```

## random

| 코드 | 뜻 |
| --- | --- |
| `import random` | random 모듈 가져오기 |
| `random.choice(리스트)` | 하나를 무작위로 고르기 |
| `random.choice(list(WORDS))` | 단어장에서 암호(키) 고르기 |

## 특수 문자 입력 (■ □)

| 방법 | 하는 법 |
| --- | --- |
| 윈도우 한글 자판 | 한글 상태에서 **ㅁ** 입력 → **한자** 키 → **Tab** → ■ □ 선택 |
| 유니코드 | `"■"` ■, `"□"` □ |
| 복사·붙여 넣기 | 이 페이지의 ■ □를 복사해 붙여 넣기 |
