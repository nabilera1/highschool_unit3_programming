> **1부 게임을 분석하고 기본 버전 만들기** · 3차시 · 수업 단계: **컴퓨팅 설계**  
> 핵심 개념: for, range, 문자열 누적, end, 조건문, 추적표

## 학습 목표

1. for 반복문으로 문자열의 글자를 하나씩 꺼낼 수 있다.
2. for와 if를 함께 써서 맞힌 글자만 보여 주는 암호판을 만들 수 있다.
3. 문자열 누적(+)으로 맞힌 글자를 기록할 수 있다.

## 핵심 질문

> **암호가 4글자일 때도, 8글자일 때도 똑같은 코드로 밑줄 암호판을 만들려면?**

`help`의 암호판은 `_ _ _ _`, `together`의 암호판은 `_ _ _ _ _ _ _ _`입니다. 글자 수가 바뀔 때마다 코드를 고칠 수는 없습니다.

**for 반복문**은 문자열의 글자를 처음부터 끝까지 하나씩 꺼내 줍니다. 글자마다 '맞힌 글자인가?'를 물어보면 어떤 길이의 암호든 같은 코드로 암호판을 만들 수 있습니다.

## for 글자 in 문자열

```python
for 글자 in 'help':        # 'h' → 'e' → 'l' → 'p' 순서로 하나씩
    print(글자)
```

```text
h
e
l
p
```

`print(글자, end=' ')`처럼 `end`를 바꾸면 줄을 바꾸지 않고 옆으로 이어서 출력합니다.

## 밑줄 암호판 알고리즘

```python
비밀단어 = 'help'
맞춘단어 = 'hp'
for 글자 in 비밀단어:          # 암호의 글자를 하나씩
    if 글자 in 맞춘단어:      # 맞힌 글자면
        print(글자, end=' ')   #   그대로 보여 주고
    else:
        print('_', end=' ')    #   아니면 밑줄
print()                        # 마지막에 줄바꿈
```

**추적표**로 한 단계씩 따라가 봅시다.

| 반복 | 글자 | `글자 in 맞춘단어` | 출력 |
| --- | --- | --- | --- |
| 1 | h | True | `h ` |
| 2 | e | False | `_ ` |
| 3 | l | False | `_ ` |
| 4 | p | True | `p ` |

최종 화면: `h _ _ p`

## 맞힌 글자 기록하기: 문자열 누적

```python
맞춘단어 = ''                     # 빈 문자열에서 시작
guess = input('알파벳 한 글자 > ')
if guess in 비밀단어:
    맞춘단어 = 맞춘단어 + guess   # 'h' → 'hp' → 'hpe' 처럼 이어 붙인다
```

`맞춘단어 = 맞춘단어 + guess`는 '지금까지 기록 뒤에 새 글자를 붙여 다시 저장'한다는 뜻입니다. `맞춘단어 += guess`로 줄여 쓸 수도 있습니다.

## 횟수가 정해진 반복: for + range

```python
for 차례 in range(3):      # 차례 = 0, 1, 2 → 3번 반복
    guess = input(f'{차례 + 1}번째 알파벳 > ')
```

오늘 코드는 입력을 **딱 3번**만 받습니다. 암호를 완성할 때까지 계속 묻는 것은 다음 차시에 `while`로 해결합니다.

## 실행 예시

`new_rescue_step2_board.py`를 실행한 화면입니다. `>` 뒤의 글자가 키보드로 입력한 값입니다. `e`, `a`, `z`를 차례로 입력한 예입니다. (암호는 무작위로 정해지므로 실행할 때마다 달라집니다.)

```text
_ _ _ _ 
1번째 알파벳 > e
좋아요! 암호에 있는 글자예요.
_ _ _ e 
2번째 알파벳 > a
암호에 없는 글자예요.
_ _ _ e 
3번째 알파벳 > z
암호에 없는 글자예요.
정답 암호: hope / 맞힌 글자: e
(다음 차시: while 반복문으로 암호를 완성할 때까지 계속 묻기)
```

## 전체 코드

이번 차시의 **전체 프로그램**입니다. 주석(`#` 뒤의 설명)을 함께 읽으며 따라가 보세요.

1. 코드 블록 전체를 복사합니다. (코드 블록 오른쪽 위 복사 버튼 또는 드래그 후 Ctrl + C)
2. IDLE에서 **File → New File**을 열고 붙여 넣습니다. (Ctrl + V)
3. 아래 파일 이름으로 저장한 뒤 **F5**로 실행합니다. (VS Code는 ▶ 실행 버튼)

### new_rescue_step2_board.py

```python
# =====================================================================
# 영단어 구조대 - 2단계: 밑줄 암호판 만들기               [3차시]
#
# 이번 단계에서 배우는 것
#   - for 글자 in 문자열 : 문자열의 글자를 앞에서부터 하나씩 꺼낸다.
#   - if ~ else         : 맞힌 글자면 그 글자를, 아니면 _ 를 출력한다.
#   - print(..., end=' '): 줄을 바꾸지 않고 옆으로 이어서 출력한다.
#   - 문자열 누적        : 맞춘단어 = 맞춘단어 + guess
#
# 암호판이 만들어지는 원리 (비밀단어 = 'help', 맞춘단어 = 'hp')
#   h → 맞춘단어에 있음 → h
#   e → 없음           → _
#   l → 없음           → _
#   p → 있음           → p          화면:  h _ _ p
#
# 실행 방법: python new_rescue_step2_board.py
# =====================================================================
import random

words = ['help', 'rescue', 'safe', 'hope', 'friend', 'doctor', 'together', 'smile']
비밀단어 = random.choice(words)
맞춘단어 = ''                          # 맞힌 글자를 차례로 이어 붙일 빈 문자열

# 세 번만 입력받아 보자 (반복 횟수가 정해져 있으면 for + range)
for 차례 in range(3):                  # 차례 = 0, 1, 2
    # ---- 밑줄 암호판 출력 ----
    for 글자 in 비밀단어:              # 암호의 글자를 하나씩 꺼내서
        if 글자 in 맞춘단어:          # 이미 맞힌 글자면
            print(글자, end=' ')       #   그 글자를 보여 주고
        else:                          # 아직 못 맞힌 글자면
            print('_', end=' ')        #   밑줄로 가린다
    print()                            # 암호판을 다 찍었으면 줄바꿈

    # ---- 입력과 판정 ----
    guess = input(f'{차례 + 1}번째 알파벳 > ')
    if guess in 비밀단어:
        맞춘단어 = 맞춘단어 + guess    # 맞힌 글자를 기록에 이어 붙인다
        print('좋아요! 암호에 있는 글자예요.')
    else:
        print('암호에 없는 글자예요.')

print('정답 암호:', 비밀단어, '/ 맞힌 글자:', 맞춘단어)
print('(다음 차시: while 반복문으로 암호를 완성할 때까지 계속 묻기)')
```

파일 받기: [new_rescue_step2_board.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_step2_board.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_step2_board.py)

## 실습 활동

1. `new_rescue_step2_board.py`를 실행하고, 화면의 암호판이 어떻게 바뀌는지 관찰하세요.
2. 추적표를 이용해 `비밀단어='rescue'`, `맞춘단어='es'`일 때 출력될 암호판을 예상하세요.
3. `range(3)`을 `range(5)`로 바꾸면 무엇이 달라지는지 확인하세요.
4. 밑줄 대신 `?`나 `*`로 가려 보는 등 화면을 꾸며 보세요.

활동지: [new_ws03-for-board.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws03-for-board.md)

## 도전 과제 (기본 · 응용 · 심화)

자신의 속도에 맞게 골라 도전하세요. 기본을 마치면 응용, 응용을 마치면 심화로!

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | 암호판 아래에 `(맞힌 글자: hp)`처럼 맞춘단어를 함께 출력하기 |
| 응용 | 틀린 글자도 `틀린단어`에 누적해 출력하기 |
| 심화 | print 대신 문자열 변수 `판`에 누적해 암호판 문자열을 만든 뒤 한 번에 출력하기 |

## 확인 퀴즈

**Q1.** `for ch in 'safe':`는 몇 번 반복하는가?

- ① 3번
- ② 4번
- ③ 5번
- ④ 무한 반복

**Q2.** `print('a', end=' ')`의 `end=' '`의 역할은?

- ① 줄을 바꾼다
- ② 줄을 바꾸지 않고 공백을 붙인다
- ③ 출력을 지운다
- ④ 오류가 난다

**Q3.** `비밀단어='hope'`, `맞춘단어='oe'`일 때 암호판은?

- ① h o p e
- ② _ o _ e
- ③ o _ e _
- ④ _ _ _ _

**Q4.** `s = ''` 다음에 `s = s + 'h'`, `s = s + 'p'`를 실행하면 s는?

- ① 'h'
- ② 'p'
- ③ 'hp'
- ④ 'ph'

**Q5.** `for i in range(3):`에서 i가 갖는 값은?

- ① 1, 2, 3
- ② 0, 1, 2
- ③ 0, 1, 2, 3
- ④ 3

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 밑줄 암호판 출력 (기본)

첫째 줄에 암호, 둘째 줄에 지금까지 맞힌 글자들이 주어집니다. 맞힌 글자는 그대로, 나머지는 `_`로 바꾸어 한 칸씩 띄어 출력하세요.

- 입력: 암호, 맞힌 글자들
- 출력: 밑줄 암호판

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

### 문제 2. 공개된 칸, 남은 칸 (도전)

첫째 줄에 암호, 둘째 줄에 맞힌 글자들이 주어집니다. 암호판에서 공개된 칸 수와 아직 `_`인 칸 수를 `공개 a칸 / 남은 b칸` 형식으로 출력하세요.

- 입력: 암호, 맞힌 글자들
- 출력: `공개 a칸 / 남은 b칸`

예제 입력 1

```text
together
te
```

예제 출력 1

```text
공개 4칸 / 남은 4칸
```

예제 입력 2

```text
help
xyz
```

예제 출력 2

```text
공개 0칸 / 남은 4칸
```

정답과 해설은 **[부록] 04-1-03. 3차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-03-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- for 글자 in 문자열 → 글자를 하나씩 꺼낸다
- for + if 로 맞힌 글자만 보여 주는 암호판
- 맞춘단어 = 맞춘단어 + guess 로 기록을 누적한다
- range(n)은 0부터 n-1까지, n번 반복

## 수업 흐름 (45분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 5분 | 4글자·8글자 암호판을 한 코드로? |
| 전개 1 | 15분 | for 글자 in 문자열, end, 추적표 |
| 전개 2 | 15분 | 암호판 코드 실습, 문자열 누적 |
| 정리 | 10분 | 확인 퀴즈, 코딩 테스트 |

## 교사용 메모

- **추적표**는 이후 모든 차시에서 쓰는 도구입니다. 첫 사용이므로 교사가 칠판에서 한 줄씩 함께 채웁니다.
- `end=' '`를 빼먹어 글자가 세로로 출력되는 실수가 많습니다. 일부러 빼고 실행해 보게 하면 오래 기억합니다.
- 코딩 테스트 2의 '공개 칸 수'는 7차시 `구조대위치()` 함수의 기초가 되므로, 해결한 학생에게 '비율로 바꾸면?'을 물어 확장해 줍니다.

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `new_rescue_step2_board.py` | [new_rescue_step2_board.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_step2_board.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_step2_board.py) |
| 학습용 PPT | [new_03-for-board.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/new_03-for-board.pptx) |
| 학생 활동지 | [new_ws03-for-board.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws03-for-board.md) |
| 코딩 테스트 1 정답 코드 | [new_ch03_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch03_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch03_test1.py) |
| 코딩 테스트 2 정답 코드 | [new_ch03_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch03_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch03_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
