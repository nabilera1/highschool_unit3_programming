> **3부 테스트하고 공유하기** · 7차시 · 수업 단계: **테스트 및 개선**  
> 핵심 개념: 테스트 케이스(정상·경계·예외), strip, lower, len, in, 입력 검사, 다시 묻는 반복

## 학습 목표

1. 정상·경계·예외 테스트 케이스를 만들어 프로그램의 오류를 찾을 수 있다.
2. strip·lower·len·in으로 입력을 다듬고 검사하는 코드를 설명할 수 있다.
3. 테스트 결과를 기록하고 코드를 개선할 수 있다.

## 핵심 질문

> **게임을 하는 사람이 '이상한' 값을 입력해도 게임이 공정하게 진행되려면 무엇을 해야 할까?**

## 테스트 케이스의 세 종류

| 종류 | 뜻 | 영단어 구조대 예 |
| --- | --- | --- |
| 정상 | 규칙대로 들어오는 값 | `e`, `h` (소문자 알파벳 한 글자) |
| 경계 | 규칙이 바뀌는 바로 그 지점 | 배터리 1칸 남았을 때 틀리기, 마지막 한 글자 맞히기 |
| 예외 | 규칙에 맞지 않는 값 | `H`, ` e`, `he`, 빈 입력, `3`, `가`, 이미 말한 글자 |

## 입력 검사가 없으면? (테스트 결과)

`lesson07_no_check.py`는 `ask_letter()`의 입력 검사를 일부러 뺀 버전입니다. 암호가 `"help"`일 때 이상한 값을 넣어 본 실제 결과입니다.

| 테스트 입력 | 기대한 결과 | 검사 없는 버전의 실제 결과 | 문제 |
| --- | --- | --- | --- |
| `H` (대문자) | h로 인정 | 암호에 없다고 처리 → 배터리 감소 | h는 암호에 있는데 손해 |
| ` e` (앞에 공백) | e로 인정 | 암호에 없다고 처리 → 배터리 감소 | 공백 때문에 손해 |
| `he` (두 글자) | 다시 입력 | 배터리도 암호판도 그대로 | `"he" in "help"`가 True → 공짜 입력 |
| 빈 입력 (Enter) | 다시 입력 | 배터리도 암호판도 그대로 | `"" in 문자열`은 항상 True |
| `3`, `가` | 다시 입력 | 배터리 감소 | 안내 없이 손해 |
| `z`를 두 번 | '이미 말한 글자' 안내 | 배터리가 두 번 감소 | 같은 실수로 두 번 손해 |

## 입력 다듬기: strip()과 lower()

```text
' H '  →  .strip()  →  'H'  →  .lower()  →  'h'
```

## 올바른 입력이 들어올 때까지 다시 묻기

```python
def ask_letter(guessed):
    while True:
        g = input("알파벳 한 글자 > ").strip().lower()   # 공백 제거, 소문자로
        if len(g) != 1 or g not in "abcdefghijklmnopqrstuvwxyz":
            print("알파벳 한 글자만 입력하세요.")       # 빈 입력, 두 글자, 숫자, 한글
        elif g in guessed:
            print("이미 말한 글자예요.")
        else:
            return g                                   # 통과하면 반복과 함수를 함께 끝냄
```

> **왜 isalpha()를 쓰지 않을까?** `"가".isalpha()`는 True입니다. 한글도 '문자'이기 때문입니다. 그래서 이 게임에서는 알파벳 목록 `"abc…z"` 안에 있는지로 검사합니다.

## 실행 예시

완성 버전(`word_rescue.py`)의 `ask_letter(["e"])`에 이상한 값을 차례로 넣은 화면입니다. (작은따옴표는 입력값을 보이게 표시한 것)

```text
알파벳 한 글자 > ' E '
이미 말한 글자예요.
알파벳 한 글자 > 'ab'
알파벳 한 글자만 입력하세요.
알파벳 한 글자 > ''
알파벳 한 글자만 입력하세요.
알파벳 한 글자 > '3'
알파벳 한 글자만 입력하세요.
알파벳 한 글자 > '가'
알파벳 한 글자만 입력하세요.
알파벳 한 글자 > 'e'
이미 말한 글자예요.
알파벳 한 글자 > 'k'
k
```

` E `는 strip·lower를 거쳐 e가 되므로 '이미 말한 글자'로 걸러집니다.

## 실습 활동

1. `lesson07_no_check.py`를 실행해 위 표의 테스트를 직접 해 보고 실제 결과를 기록하세요. **[활동지]**
2. 짝의 게임(5·6차시 미션 코드)에 이상한 입력을 넣어 보고, 발견한 문제를 짝에게 알려 주세요.
3. 완성 버전의 `ask_letter()`에서 각 테스트를 막아 주는 코드 줄을 찾아 표에 적으세요.
4. 경계 테스트를 2개 이상 만들어 실행하세요. (예: 배터리 1칸에서 틀리기, 마지막 글자 맞히기)
5. 내 미션 코드에 주석을 달고, 테스트 결과에 따라 고친 점을 기록하세요.

활동지: [lesson07_test_input.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson07_test_input.md)

## 도전 과제 (기본 · 응용 · 심화)

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | 검사 없는 버전의 `ask_letter()`에 `.strip().lower()`를 붙이고 다시 테스트하기 |
| 응용 | 안내 문구를 경우마다 다르게 바꾸기 (한 글자가 아닐 때 / 알파벳이 아닐 때) |
| 심화 | 다시 출동 질문에 `yes`, `Y`, ` y `를 넣어 테스트하고, 어떤 답까지 '예'로 받아 줄지 정해 코드를 고치기 |

## 확인 퀴즈

**Q1.** `" H ".strip().lower()`의 결과는?

- ① `" h "`
- ② `"h"`
- ③ `"H"`
- ④ `" H"`

**Q2.** 입력 검사가 없는 버전에서 빈 입력(그냥 Enter)을 넣으면?

- ① 배터리가 한 칸 준다
- ② 아무 변화 없이 다시 묻는다(공짜 입력)
- ③ 구조 성공
- ④ 오류로 멈춘다

**Q3.** `"가".isalpha()`의 결과와 그 때문에 게임에서 쓰는 검사 방법을 바르게 짝지은 것은?

- ① `False – isalpha() 사용`
- ② `True – "abc…z" 안에 있는지로 검사`
- ③ `True – isalpha() 사용`
- ④ 오류 – 한글은 입력 불가

**Q4.** 다음 중 **경계** 테스트 케이스에 가장 가까운 것은?

- ① 정상 글자 e 입력
- ② 배터리 1칸 남았을 때 틀린 글자 입력
- ③ 한글 입력
- ④ 두 글자 입력

**Q5.** ask_letter()가 올바른 입력이 들어올 때까지 다시 묻기 위해 쓰는 구조는?

- ① `if 문 하나`
- ② `for i in range(3)`
- ③ `while True 와 return`
- ④ `try 문`

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 입력 다듬고 검사하기 (기본)

첫째 줄에 n, 다음 n줄에 사용자가 입력한 문자열이 주어집니다. 각 줄을 `strip()`과 `lower()`로 다듬은 뒤, 한 글자가 아니면 `한 글자만`, a~z가 아니면 `알파벳만`, 올바르면 `OK 글자`를 출력하세요.

- 입력: n, n줄의 입력 (빈 줄이 있을 수 있음)
- 출력: 각 줄의 검사 결과

예제 입력 1

```text
6
 H
he
3

ㅎ
z
```

예제 출력 1

```text
OK h
한 글자만
알파벳만
한 글자만
알파벳만
OK z
```

### 문제 2. 이미 말한 글자 걸러 내기 (도전)

첫째 줄에 n, 다음 n줄에 입력이 주어집니다. 기본 문제의 검사에 더해, 이미 통과한 글자가 다시 들어오면 `이미 말한 글자`를 출력하세요. 마지막 줄에는 통과한 글자를 리스트로 `guessed: [...]` 형식으로 출력합니다.

- 입력: n, n줄의 입력
- 출력: 각 줄의 검사 결과, guessed 리스트

예제 입력 1

```text
6
e
E
a
ab
z
a
```

예제 출력 1

```text
OK e
이미 말한 글자
OK a
한 글자만
OK z
이미 말한 글자
guessed: ['e', 'a', 'z']
```

정답과 해설은 **[부록] 04-1-07. 7차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-07-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 테스트 케이스는 정상·경계·예외 세 종류로 만든다
- `strip()`은 앞뒤 공백 제거, `lower()`는 소문자로
- `len(g) != 1`, `g not in "abc…z"`, `g in guessed`로 걸러 낸다
- `while True` + `return`으로 올바른 입력이 들어올 때까지 다시 묻는다
- 테스트 결과는 기록하고, 고친 뒤에는 같은 테스트를 다시 한다

## 수업 흐름 (50분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 5분 | '공정한 게임'이란? 핵심 질문, 테스트 케이스 세 종류 |
| 전개 1 | 15분 | 검사 없는 버전에 이상한 입력 넣기, 테스트 기록표 작성 [활동지] |
| 전개 2 | 10분 | 완성 버전의 ask_letter()에서 막아 주는 코드 찾기, isalpha() 함정 |
| 전개 3 | 12분 | 짝의 미션 코드 테스트 → 고치기 → 다시 테스트, 주석 달기 |
| 정리 | 8분 | 확인 퀴즈, 8차시 발표 준비 안내 |

## 교사용 메모

- `he`와 빈 입력은 학생들이 '오히려 이득'이라 좋아합니다. 이때 '이 게임은 공정한가?'를 물으면 입력 검사의 필요성을 스스로 말합니다.
- 테스트는 '찾은 오류 개수'로 칭찬합니다. 오류를 찾는 것이 테스트의 목적이라는 것을 분명히 합니다.
- 짝의 코드를 테스트할 때는 '고쳐 주기'가 아니라 '알려 주기'까지만 하게 합니다. 고치는 것은 코드 주인이 합니다.

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `lesson07_no_check.py` | [lesson07_no_check.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/lesson07_no_check.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/lesson07_no_check.py) |
| 소스코드 `word_rescue.py` | [word_rescue.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/word_rescue.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/word_rescue.py) |
| 학습용 PPT | [lesson07_test_input.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/lesson07_test_input.pptx) |
| 학생 활동지 | [lesson07_test_input.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson07_test_input.md) |
| 코딩 테스트 1 정답 코드 | [lesson07_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson07_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson07_test1.py) |
| 코딩 테스트 2 정답 코드 | [lesson07_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson07_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson07_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
