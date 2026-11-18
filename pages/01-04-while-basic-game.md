> **1부 게임을 분석하고 기본 버전 만들기** · 4차시 · 수업 단계: **컴퓨팅 설계 · 구현**  
> 핵심 개념: while, break, 종료 조건, 깃발 변수, 리스트 인덱스, not in

## 학습 목표

1. while True와 break로 종료 조건이 있는 반복을 만들 수 있다.
2. 틀린 횟수를 리스트 인덱스로 사용해 신호 그림을 출력할 수 있다.
3. 깃발(flag) 변수로 '모두 맞혔는지'를 판단할 수 있다.

## 핵심 질문

> **몇 번 반복할지 미리 알 수 없을 때, 반복은 언제 어떻게 끝내야 할까?**

3차시 코드는 입력을 딱 3번만 받았습니다. 실제 게임은 **암호를 완성하거나 6번 틀릴 때까지** 계속 물어야 합니다. 몇 번 반복할지 미리 알 수 없으므로 `for` 대신 **`while`**을 씁니다.

오늘은 1차시에 쓴 의사코드를 그대로 코드로 옮겨 **영단어 구조대 기본 버전**을 완성합니다.

## while True + break

```python
while True:                 # 조건이 항상 참 → 계속 반복
    ...
    if 끝낼조건:
        break               # 반복을 즉시 빠져나간다
```

| 반복문 | 언제 쓰나 | 예 |
| --- | --- | --- |
| `for` | 반복 횟수(또는 대상)가 정해져 있을 때 | 암호의 글자마다 |
| `while` | 조건을 만족하는 동안, 횟수를 모를 때 | 암호를 완성할 때까지 |

## 신호 그림 리스트: 틀린 횟수 = 인덱스

```python
신호그림 = ['[■■■■■■] 구조 신호 아주 강함 ...',   # 인덱스 0 (0번 틀림)
            '[■■■■■□] 구조 신호 강함',               # 인덱스 1
            '[■■■■□□] 구조 신호 양호',               # 인덱스 2
            '[■■■□□□] 구조 신호 보통',               # 인덱스 3
            '[■■□□□□] 구조 신호 약함 - 서둘러요!',    # 인덱스 4
            '[■□□□□□] 구조 신호 아주 약함 - 마지막 기회!',  # 인덱스 5
            '[□□□□□□] 구조 신호 끊김']               # 인덱스 6 (6번 틀림)

print(신호그림[len(틀린단어)])    # 2번 틀렸으면 신호그림[2]
```

틀린 횟수가 0~6이므로 그림 7개를 리스트에 넣으면 **`if`를 7번 쓰지 않고** 한 줄로 알맞은 그림을 고를 수 있습니다. 6번 틀렸는지는 `len(틀린단어) == len(신호그림) - 1`로 검사합니다. 그림 개수를 바꿔도 코드를 고칠 필요가 없습니다.

※ ■ □ 입력: 한글 자판에서 `ㅁ` 입력 → **[한자]** 키 → 목록에서 선택 (Tab 키로 목록 넓히기)

## 깃발 변수로 '모두 맞혔나?' 판단하기

```python
모두맞춤 = True                  # 깃발을 일단 세워 둔다
for 글자 in 비밀단어:
    if 글자 not in 맞춘단어:     # 못 맞힌 글자가 하나라도 있으면
        모두맞춤 = False         # 깃발을 내린다
if 모두맞춤:
    print('구조 성공!')
```

| 비밀단어 | 맞춘단어 | 못 맞힌 글자 | 모두맞춤 |
| --- | --- | --- | --- |
| help | hp | e, l | False |
| help | phle | 없음 | True |

`맞춘단어`의 글자 순서는 상관없습니다. 각 글자가 **들어 있는지**만 봅니다.

## 기본 버전 전체 구조

```text
암호 고르기, 맞춘단어 = '', 틀린단어 = ''
while True:
    ① 화면: 신호그림[len(틀린단어)], 틀린 글자, 밑줄 암호판
    ② 입력: guess
    ③ 판정: guess in 비밀단어?
        예   → 맞춘단어 += guess → 모두 맞힘? → 구조 성공, break
        아니오 → 틀린단어 += guess → 6번 틀림? → 신호 끊김, break
```

전체 코드는 아래에 있습니다. 1차시 의사코드와 한 줄씩 짝지어 보세요.

## 실행 예시

`new_rescue_1_basic.py`를 실행한 화면입니다. `>` 뒤의 글자가 키보드로 입력한 값입니다. `z`, `e`, `a`, `h`, `o`, `p`를 차례로 입력해 구조에 성공한 예입니다. (암호는 무작위로 정해지므로 실행할 때마다 달라집니다.)

```text
==================================================
 영단어 구조대 - 암호를 완성해 친구를 구조하세요!
==================================================
[■■■■■■] 구조 신호 아주 강함 - 구조대가 친구의 위치를 알고 있어요
틀린 글자: 
_ _ _ _ 
알파벳 한 글자 > z
[■■■■■□] 구조 신호 강함
틀린 글자: z
_ _ _ _ 
알파벳 한 글자 > e
[■■■■■□] 구조 신호 강함
틀린 글자: z
_ _ _ e 
알파벳 한 글자 > a
[■■■■□□] 구조 신호 양호
틀린 글자: za
_ _ _ e 
알파벳 한 글자 > h
[■■■■□□] 구조 신호 양호
틀린 글자: za
h _ _ e 
알파벳 한 글자 > o
[■■■■□□] 구조 신호 양호
틀린 글자: za
h o _ e 
알파벳 한 글자 > p
구조 성공! 암호 hope로 헬기가 출동해 친구가 무사히 돌아왔어요!
```

## 전체 코드

이번 차시의 **전체 프로그램**입니다. 주석(`#` 뒤의 설명)을 함께 읽으며 따라가 보세요.

1. 코드 블록 전체를 복사합니다. (코드 블록 오른쪽 위 복사 버튼 또는 드래그 후 Ctrl + C)
2. IDLE에서 **File → New File**을 열고 붙여 넣습니다. (Ctrl + V)
3. 아래 파일 이름으로 저장한 뒤 **F5**로 실행합니다. (VS Code는 ▶ 실행 버튼)

### new_rescue_1_basic.py

```python
# =====================================================================
# 영단어 구조대 (기본 버전)                                [4차시]
#   리스트 · 문자열 · for · while · if 만 사용 (함수 없음)
#
# 이야기
#   산에서 길을 잃은 친구가 영단어 암호로 SOS를 보냈어요.
#   알파벳을 한 글자씩 맞혀 암호를 완성하면 구조 헬기가 출동해요!
#   암호에 없는 글자를 말하면 구조 신호 배터리가 한 칸씩 줄어요.
#   6번 틀리면(배터리 0칸) 신호가 끊겨요. 괜찮아요, 다시 출동하면 돼요.
#
# 게임 알고리즘 (순서)
#   ① 암호를 무작위로 고른다
#   ② [반복] 신호 그림 · 틀린 글자 · 밑줄 암호를 보여 준다
#   ③        알파벳 한 글자를 입력받는다
#   ④        암호에 있으면 → 맞춘단어에 추가 → 모두 맞혔으면 '구조 성공' 후 끝
#            암호에 없으면 → 틀린단어에 추가 → 6번 틀렸으면 '신호 끊김' 후 끝
#
# ※ 5차시 '테스트로 오류 찾기' 활동을 위해 입력 검사(대문자·숫자·두 글자·
#   이미 입력한 글자)를 일부러 넣지 않았습니다. 고친 버전: new_rescue_1_basic_checked.py
#
# 실행 방법: python new_rescue_1_basic.py
# =====================================================================
import random

# 구조 신호 그림 리스트
#   틀린 횟수가 곧 인덱스!  0번 틀림 → 신호그림[0],  3번 틀림 → 신호그림[3]
#   ■ □ 입력 방법: 한글 자판에서 ㅁ 입력 → [한자] 키 → 목록에서 선택
신호그림 = ['[■■■■■■] 구조 신호 아주 강함 - 구조대가 친구의 위치를 알고 있어요',
            '[■■■■■□] 구조 신호 강함',
            '[■■■■□□] 구조 신호 양호',
            '[■■■□□□] 구조 신호 보통',
            '[■■□□□□] 구조 신호 약함 - 서둘러요!',
            '[■□□□□□] 구조 신호 아주 약함 - 마지막 기회!',
            '[□□□□□□] 구조 신호 끊김']

# 암호 단어장 (리스트)
words = ['help', 'rescue', 'safe', 'hope', 'friend', 'doctor', 'together', 'smile']

print('=' * 50)                                   # 문자열 * 50 → '=' 50개
print(' 영단어 구조대 - 암호를 완성해 친구를 구조하세요!')
print('=' * 50)

비밀단어 = random.choice(words)    # ① 암호(비밀 단어)
맞춘단어 = ''                      # 맞힌 글자를 이어 붙여 기록 (예: 'hp')
틀린단어 = ''                      # 틀린 글자를 이어 붙여 기록 (예: 'zx') → len(틀린단어) = 틀린 횟수

while True:                        # 끝나는 조건(break)을 만날 때까지 계속 반복
    # ② 화면 출력: 신호 그림, 틀린 글자, 밑줄 암호
    print(신호그림[len(틀린단어)])  # 틀린 횟수 = 인덱스
    print('틀린 글자:', 틀린단어)
    for 글자 in 비밀단어:
        if 글자 in 맞춘단어:
            print(글자, end=' ')
        else:
            print('_', end=' ')
    print()

    # ③ 입력
    guess = input('알파벳 한 글자 > ')

    # ④ 판정
    if guess in 비밀단어:
        맞춘단어 = 맞춘단어 + guess
        # 종료 조건 ① 모두 맞힘
        #   깃발(flag) 변수: 일단 True 로 세워 두고, 못 맞힌 글자를 하나라도 찾으면 False 로 내린다
        모두맞춤 = True
        for 글자 in 비밀단어:
            if 글자 not in 맞춘단어:
                모두맞춤 = False
        if 모두맞춤:
            print(f'구조 성공! 암호 {비밀단어}로 헬기가 출동해 친구가 무사히 돌아왔어요!')
            break                  # while 반복을 빠져나간다 → 프로그램 끝
    else:
        틀린단어 = 틀린단어 + guess
        # 종료 조건 ② 6번 틀림 (신호그림은 7개 → 마지막 인덱스 6 = len(신호그림) - 1)
        if len(틀린단어) == len(신호그림) - 1:
            print(신호그림[len(틀린단어)])
            print(f'신호가 끊겼어요. 암호는 {비밀단어}였어요. 다시 출동해서 친구를 구해 봐요!')
            break
```

파일 받기: [new_rescue_1_basic.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_1_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_1_basic.py)

## 실습 활동

1. `new_rescue_1_basic.py`를 실행해 구조 성공과 신호 끊김을 각각 한 번씩 경험해 보세요.
2. 1차시 의사코드의 각 줄 옆에 해당하는 코드 줄 번호를 적어 보세요.
3. 빈칸 채우기 파일 `new_rescue_1_blank.py`의 ①~⑩을 채워 게임을 완성하세요.
4. 신호그림 리스트에 그림을 하나 더 넣으면 기회가 몇 번이 되는지 예상하고 확인하세요.

활동지: [new_ws04-while-basic-game.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws04-while-basic-game.md)

## 도전 과제 (기본 · 응용 · 심화)

자신의 속도에 맞게 골라 도전하세요. 기본을 마치면 응용, 응용을 마치면 심화로!

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | words 리스트를 2차시에 만든 우리 반 구조 단어장으로 바꾸기 |
| 응용 | 구조 성공 메시지에 틀린 횟수 함께 출력하기 (`len(틀린단어)`) |
| 심화 | 게임이 끝나면 '다시 출동할까요?'를 물어 y면 새 암호로 다시 시작하기 (while 안에 while) |

## 확인 퀴즈

**Q1.** `while True:` 반복을 끝내는 명령은?

- ① stop
- ② exit
- ③ break
- ④ end

**Q2.** 신호그림이 7개일 때 `len(신호그림) - 1`의 값은?

- ① 5
- ② 6
- ③ 7
- ④ 8

**Q3.** 틀린단어가 `'zx'`일 때 출력되는 그림은?

- ① 신호그림[0]
- ② 신호그림[1]
- ③ 신호그림[2]
- ④ 신호그림[3]

**Q4.** `비밀단어='safe'`, `맞춘단어='sfa'`일 때 깃발 변수 `모두맞춤`의 값은?

- ① True
- ② False
- ③ None
- ④ 오류

**Q5.** 횟수를 미리 알 수 없는 반복에 알맞은 것은?

- ① for i in range(3)
- ② while
- ③ if
- ④ print

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 신호 배터리 그리기 (기본)

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

### 문제 2. 구조 출동 시뮬레이션 (도전)

첫째 줄에 암호, 둘째 줄에 입력할 알파벳들이 한 줄로 주어집니다(중복 없음). 앞에서부터 한 글자씩 게임 규칙대로 처리하여, 모두 맞히면 `구조 성공! 틀린 횟수 n`, 6번 틀리면 `신호 끊김`, 글자를 다 써도 끝나지 않으면 `암호 미완성`을 출력하세요. 게임이 끝나면 남은 글자는 무시합니다.

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

정답과 해설은 **[부록] 04-1-04. 4차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-04-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 횟수를 모르는 반복 → while True 와 break
- 신호그림[len(틀린단어)] : 틀린 횟수를 인덱스로
- 깃발 변수: True로 세우고, 못 맞힌 글자가 있으면 False
- 종료 조건 두 개 = break 두 개

## 수업 흐름 (45분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 5분 | 3번만 묻는 코드의 한계, 핵심 질문 |
| 전개 1 | 15분 | while·break, 신호그림 인덱스 |
| 전개 2 | 15분 | 깃발 변수, 기본 버전 완성·실행 |
| 정리 | 10분 | 빈칸 채우기, 확인 퀴즈 |

## 교사용 메모

- 기본 버전에는 입력 검사가 **일부러** 없습니다. 오늘 학생이 'H를 쳤더니 틀렸어요'라고 하면 정답을 알려 주지 말고 메모해 두게 하세요. 5차시 테스트 활동의 재료가 됩니다.
- 빈칸 채우기 파일은 빈칸이 있는 상태로는 실행되지 않습니다(SyntaxError). 모두 채운 뒤 실행하도록 안내합니다.
- 활동지 '게임 실행 추적' 정답: (입력 처리 후 기준) e(맞춘단어 e, 인덱스 0) → z(틀린단어 z, 1) → s(es, 1) → q(zq, 2) → a(esa, 2) → f(esaf, 모두 맞힘 → 구조 성공).

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `new_rescue_1_basic.py` | [new_rescue_1_basic.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_1_basic.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_1_basic.py) |
| 소스코드 `new_rescue_1_blank.py` | [new_rescue_1_blank.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_1_blank.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_1_blank.py) |
| 소스코드 `new_rescue_1_blank_answer.py` | [new_rescue_1_blank_answer.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_1_blank_answer.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_1_blank_answer.py) |
| 학습용 PPT | [new_04-while-basic-game.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/new_04-while-basic-game.pptx) |
| 학생 활동지 | [new_ws04-while-basic-game.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws04-while-basic-game.md) |
| 코딩 테스트 1 정답 코드 | [new_ch04_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch04_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch04_test1.py) |
| 코딩 테스트 2 정답 코드 | [new_ch04_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch04_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch04_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
