> **2부 테스트와 함수로 다듬기** · 5차시 · 수업 단계: **테스트 및 개선**  
> 핵심 개념: 테스트 케이스, 정상, 경계, 예외, strip, lower, 입력 검사

## 학습 목표

1. 정상·경계·예외 테스트 케이스를 만들어 프로그램의 오류를 찾을 수 있다.
2. strip(), lower(), len()으로 입력값을 다듬고 검사할 수 있다.
3. 올바른 입력이 들어올 때까지 다시 묻는 while 반복을 만들 수 있다.

## 핵심 질문

> **게임을 하는 사람이 '이상한' 값을 입력해도 게임이 공정하게 진행되려면 무엇을 해야 할까?**

4차시 기본 버전은 규칙대로 입력하면 잘 동작합니다. 하지만 실제 사용자는 대문자 `H`를 치거나, 실수로 두 글자를 치거나, 한글 자판 상태에서 `ㅗ`를 치기도 합니다.

오늘은 **일부러 이상한 값을 넣어 보는 테스트**로 오류를 찾고, 입력 검사를 추가해 게임을 고칩니다. 프로그램을 만드는 일만큼 **테스트하고 개선하는 일**도 중요한 문제 해결 과정입니다.

## 테스트 케이스의 세 종류

| 종류 | 뜻 | 영단어 구조대 예 |
| --- | --- | --- |
| 정상 | 규칙대로 들어오는 값 | `e`, `p` |
| 경계 | 규칙의 끝에 걸친 값 | `a`, `z`, 6번째 틀림 |
| 예외 | 규칙을 벗어난 값 | `H`, ` e`, `he`, `3`, `ㅎ`, 빈 입력, 같은 글자 두 번 |

## 기본 버전 테스트 결과

| 테스트 입력 | 기대한 결과 | 기본 버전의 실제 결과 | 오류? |
| --- | --- | --- | --- |
| `e` (정상) | 맞힘 처리 | 맞힘 처리 | 없음 |
| `H` (대문자) | `h`로 인정 | 틀림, 배터리 감소 | **오류** |
| ` e` (앞 공백) | `e`로 인정 | 틀림, 배터리 감소 | **오류** |
| `he` (두 글자) | 다시 입력 | `'he' in 'help'`가 True → 맞힘 처리 | **오류** |
| 빈 입력(Enter) | 다시 입력 | `'' in 'help'`가 True → 맞힘 처리 | **오류** |
| `3`, `ㅎ` | 다시 입력 | 틀림, 배터리 감소 | **오류** |
| `z`를 두 번 | '이미 입력' 안내 | 배터리가 두 번 감소 | **오류** |

**빈 문자열은 모든 문자열에 포함**된다는 점(`'' in 'help'` → True)은 많은 사람이 놓치는 함정입니다.

## 입력 다듬기: strip()과 lower()

```python
guess = input('알파벳 한 글자 > ').strip().lower()
#        ' H '  →  .strip() → 'H'  →  .lower() → 'h'
```

| 메서드 | 하는 일 | 예 |
| --- | --- | --- |
| `.strip()` | 앞뒤 공백 제거 | `' e '` → `'e'` |
| `.lower()` | 소문자로 | `'H'` → `'h'` |
| `.upper()` | 대문자로 | `'h'` → `'H'` |

## 올바른 입력이 들어올 때까지 다시 묻기

```python
알파벳 = 'abcdefghijklmnopqrstuvwxyz'
while True:
    guess = input('알파벳 한 글자 > ').strip().lower()
    if len(guess) != 1:                   # 빈 입력, 두 글자 이상
        print('한 글자만 입력해 주세요.')
    elif guess not in 알파벳:             # 숫자, 한글, 기호
        print('알파벳(a~z)만 입력해 주세요.')
    elif guess in 맞춘단어 + 틀린단어:    # 이미 말한 글자
        print('이미 입력한 글자입니다. 다른 글자를 고르세요.')
    else:
        break                             # 통과! 반복 탈출
```

검사 **순서**가 중요합니다. 먼저 한 글자인지 확인해야 `guess not in 알파벳`이 올바르게 동작합니다. (`'ab' in 알파벳`은 True라서 두 글자를 먼저 걸러야 합니다.)

※ `guess.isalpha()`는 한글 `'ㅎ'`도 True로 판단합니다. 그래서 여기서는 알파벳 목록으로 직접 검사합니다.

## 실행 예시

`new_rescue_1_basic_checked.py`를 실행한 화면입니다. `>` 뒤의 글자가 키보드로 입력한 값입니다. 빈 입력, `he`, `3`, `ㅎ`, ` E `, `e`, `Z`처럼 일부러 예외 입력을 넣어 본 테스트 화면입니다. (암호는 무작위로 정해지므로 실행할 때마다 달라집니다.)

```text
==================================================
 영단어 구조대 - 암호를 완성해 친구를 구조하세요!
==================================================
[■■■■■■] 구조 신호 아주 강함 - 구조대가 친구의 위치를 알고 있어요
틀린 글자: 
_ _ _ _ 
알파벳 한 글자 > 
한 글자만 입력해 주세요.
알파벳 한 글자 > he
한 글자만 입력해 주세요.
알파벳 한 글자 > 3
알파벳(a~z)만 입력해 주세요.
알파벳 한 글자 > ㅎ
알파벳(a~z)만 입력해 주세요.
알파벳 한 글자 >  E 
[■■■■■■] 구조 신호 아주 강함 - 구조대가 친구의 위치를 알고 있어요
틀린 글자: 
_ _ _ e 
알파벳 한 글자 > e
이미 입력한 글자입니다. 다른 글자를 고르세요.
알파벳 한 글자 > Z
[■■■■■□] 구조 신호 강함
틀린 글자: z
_ _ _ e 
알파벳 한 글자 > e
이미 입력한 글자입니다. 다른 글자를 고르세요.
알파벳 한 글자 > t
[■■■■□□] 구조 신호 양호
틀린 글자: zt
_ _ _ e 
알파벳 한 글자 > r
[■■■□□□] 구조 신호 보통
틀린 글자: ztr
_ _ _ e 
알파벳 한 글자 > o
[■■■□□□] 구조 신호 보통
틀린 글자: ztr
_ o _ e 
알파벳 한 글자 > i
[■■□□□□] 구조 신호 약함 - 서둘러요!
틀린 글자: ztri
_ o _ e 
알파벳 한 글자 > s
[■□□□□□] 구조 신호 아주 약함 - 마지막 기회!
틀린 글자: ztris
_ o _ e 
알파벳 한 글자 > a
[□□□□□□] 구조 신호 끊김
신호가 끊겼어요. 암호는 hope였어요. 다시 출동해서 친구를 구해 봐요!
```

## 전체 코드

이번 차시의 **전체 프로그램**입니다. 주석(`#` 뒤의 설명)을 함께 읽으며 따라가 보세요.

1. 코드 블록 전체를 복사합니다. (코드 블록 오른쪽 위 복사 버튼 또는 드래그 후 Ctrl + C)
2. IDLE에서 **File → New File**을 열고 붙여 넣습니다. (Ctrl + V)
3. 아래 파일 이름으로 저장한 뒤 **F5**로 실행합니다. (VS Code는 ▶ 실행 버튼)

### new_rescue_1_basic_checked.py

```python
# =====================================================================
# 영단어 구조대 (기본 + 입력 검사 버전)                    [5차시]
#
# 4차시 기본 버전을 테스트했더니 이런 오류가 있었어요.
#   테스트 입력        기대한 결과               기본 버전의 실제 결과
#   'H' (대문자)       h 로 인정                  암호에 없다고 처리 → 배터리 감소
#   ' e' (앞에 공백)   e 로 인정                  ' e' 는 암호에 없음 → 배터리 감소
#   'he' (두 글자)     다시 입력하게 안내          'he' in 'help' → True! 두 글자를 한 번에 맞힘
#   '' (그냥 Enter)    다시 입력하게 안내          '' in 문자열 → 항상 True! (빈 문자열은 모든 문자열에 포함)
#   '3', 'ㅎ'         다시 입력하게 안내          배터리 감소
#   'z' 를 두 번       '이미 입력' 안내           같은 실수로 배터리가 두 번 감소
#
# 고친 방법: 입력을 받는 부분을 '올바른 입력이 들어올 때까지 다시 묻는 while 반복'으로 바꿨다.
#   .strip()  → 앞뒤 공백 제거       ' e ' → 'e'
#   .lower()  → 소문자로 바꾸기      'H'   → 'h'
#   len(guess) != 1                → 한 글자가 아니면 다시
#   guess not in 'abc...z'         → 알파벳이 아니면 다시
#     (※ isalpha()는 한글 'ㅎ'도 True 이므로 여기서는 알파벳 목록으로 검사한다)
#   guess in 맞춘단어 + 틀린단어      → 이미 말한 글자면 다시
#
# 실행 방법: python new_rescue_1_basic_checked.py
# =====================================================================
import random

신호그림 = ['[■■■■■■] 구조 신호 아주 강함 - 구조대가 친구의 위치를 알고 있어요',
            '[■■■■■□] 구조 신호 강함',
            '[■■■■□□] 구조 신호 양호',
            '[■■■□□□] 구조 신호 보통',
            '[■■□□□□] 구조 신호 약함 - 서둘러요!',
            '[■□□□□□] 구조 신호 아주 약함 - 마지막 기회!',
            '[□□□□□□] 구조 신호 끊김']
words = ['help', 'rescue', 'safe', 'hope', 'friend', 'doctor', 'together', 'smile']
알파벳 = 'abcdefghijklmnopqrstuvwxyz'

print('=' * 50)
print(' 영단어 구조대 - 암호를 완성해 친구를 구조하세요!')
print('=' * 50)

비밀단어 = random.choice(words)
맞춘단어 = ''
틀린단어 = ''

while True:
    # 화면 출력
    print(신호그림[len(틀린단어)])
    print('틀린 글자:', 틀린단어)
    for 글자 in 비밀단어:
        if 글자 in 맞춘단어:
            print(글자, end=' ')
        else:
            print('_', end=' ')
    print()

    # ---- [새로 추가] 올바른 입력이 들어올 때까지 다시 묻기 ----
    while True:
        guess = input('알파벳 한 글자 > ').strip().lower()   # 공백 제거 + 소문자 통일
        if len(guess) != 1:                  # 빈 입력, 두 글자 이상
            print('한 글자만 입력해 주세요.')
        elif guess not in 알파벳:            # 숫자, 한글, 기호
            print('알파벳(a~z)만 입력해 주세요.')
        elif guess in 맞춘단어 + 틀린단어:   # 이미 말한 글자
            print('이미 입력한 글자입니다. 다른 글자를 고르세요.')
        else:
            break                            # 올바른 입력 → 안쪽 while 탈출
    # -------------------------------------------------------------

    if guess in 비밀단어:
        맞춘단어 = 맞춘단어 + guess
        모두맞춤 = True
        for 글자 in 비밀단어:
            if 글자 not in 맞춘단어:
                모두맞춤 = False
        if 모두맞춤:
            print(f'구조 성공! 암호 {비밀단어}로 헬기가 출동해 친구가 무사히 돌아왔어요!')
            break
    else:
        틀린단어 = 틀린단어 + guess
        if len(틀린단어) == len(신호그림) - 1:
            print(신호그림[len(틀린단어)])
            print(f'신호가 끊겼어요. 암호는 {비밀단어}였어요. 다시 출동해서 친구를 구해 봐요!')
            break
```

파일 받기: [new_rescue_1_basic_checked.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_1_basic_checked.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_1_basic_checked.py)

## 실습 활동

1. `new_rescue_1_basic.py`(기본 버전)에 테스트 표의 입력을 하나씩 넣어 실제 결과를 기록하세요.
2. `new_rescue_1_basic_checked.py`에 같은 입력을 넣어 오류가 고쳐졌는지 확인하세요.
3. 모둠별로 아직 찾지 못한 예외 입력을 하나 더 찾아 테스트 표에 추가하세요.
4. 입력 검사의 `if`와 첫 번째 `elif`의 순서를 바꾸면 어떤 입력에서 문제가 생기는지 확인하세요.

활동지: [new_ws05-test-input-check.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws05-test-input-check.md)

## 도전 과제 (기본 · 응용 · 심화)

자신의 속도에 맞게 골라 도전하세요. 기본을 마치면 응용, 응용을 마치면 심화로!

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | 테스트 표를 완성하고 기본 버전과 개선 버전의 결과 비교하기 |
| 응용 | 안내 메시지에 지금까지 말한 글자 목록을 함께 보여 주기 |
| 심화 | `ord()`를 이용해 `'a' <= guess <= 'z'`처럼 범위로 알파벳을 검사하는 방법을 찾아 비교하기 |

## 확인 퀴즈

**Q1.** `' He '.strip().lower()`의 결과는?

- ① ' he '
- ② 'He'
- ③ 'he'
- ④ 'HE'

**Q2.** `'' in 'help'`의 결과는?

- ① True
- ② False
- ③ None
- ④ 오류

**Q3.** 다음 중 '예외' 테스트 케이스에 해당하는 것은?

- ① e
- ② p
- ③ 3
- ④ a

**Q4.** `len(guess) != 1` 검사를 가장 먼저 하는 이유는?

- ① 속도가 빨라서
- ② 'ab' in 알파벳이 True라서 두 글자를 먼저 걸러야 해서
- ③ 오류 메시지가 짧아서
- ④ 순서는 상관없다

**Q5.** `'ㅎ'.isalpha()`의 결과는?

- ① True
- ② False
- ③ 오류
- ④ None

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

### 문제 2. 이미 입력한 글자 걸러 내기 (도전)

첫째 줄에 n, 다음 n줄에 입력이 주어집니다. 기본 문제의 검사에 더해, 이미 통과한 글자가 다시 들어오면 `이미 입력`을 출력하세요. 마지막 줄에는 통과한 글자를 순서대로 이어 `사용한 글자: ...` 형식으로 출력합니다.

- 입력: n, n줄의 입력
- 출력: 각 줄의 검사 결과, 사용한 글자

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
이미 입력
OK a
한 글자만
OK z
이미 입력
사용한 글자: eaz
```

정답과 해설은 **[부록] 04-1-05. 5차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-05-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 테스트 케이스: 정상 · 경계 · 예외
- strip()으로 공백 제거, lower()로 소문자 통일
- 검사 순서: 한 글자? → 알파벳? → 이미 입력?
- 올바른 입력이 들어올 때까지 while로 다시 묻기

## 수업 흐름 (45분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 5분 | 4차시에 발견한 이상한 동작 공유 |
| 전개 1 | 15분 | 테스트 케이스 3종, 기본 버전 테스트 |
| 전개 2 | 15분 | strip·lower·입력 검사 반복으로 개선 |
| 정리 | 10분 | 개선 버전 재테스트, 확인 퀴즈 |

## 교사용 메모

- 4차시에 학생들이 메모해 둔 '이상한 동작'을 먼저 발표하게 하고 테스트 표에 옮겨 적습니다. 학생이 찾은 오류로 수업을 시작하면 동기가 높습니다.
- `'' in 'help'`가 True인 것은 교사도 놓치기 쉬운 부분입니다. 직접 IDLE에서 확인하게 하세요.
- 중학생 학급은 '심화(ord)'를 생략하고 테스트 표 작성과 개선 버전 비교에 집중합니다.

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `new_rescue_1_basic.py` | [new_rescue_1_basic.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_1_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_1_basic.py) |
| 소스코드 `new_rescue_1_basic_checked.py` | [new_rescue_1_basic_checked.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_1_basic_checked.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_1_basic_checked.py) |
| 학습용 PPT | [new_05-test-input-check.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/new_05-test-input-check.pptx) |
| 학생 활동지 | [new_ws05-test-input-check.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws05-test-input-check.md) |
| 코딩 테스트 1 정답 코드 | [new_ch05_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch05_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch05_test1.py) |
| 코딩 테스트 2 정답 코드 | [new_ch05_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch05_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch05_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
