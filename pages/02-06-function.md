> **2부 테스트와 함수로 다듬기** · 6차시 · 수업 단계: **구현**  
> 핵심 개념: 함수, def, 매개변수, return, 반환값, main(), 리팩터링

## 학습 목표

1. def로 함수를 정의하고 호출할 수 있다.
2. 매개변수와 반환값(return)의 역할을 설명할 수 있다.
3. 긴 코드를 하는 일별 함수와 main() 구조로 나눌 수 있다.

## 핵심 질문

> **코드가 길어져서 어디가 무슨 일을 하는지 찾기 어렵다면 어떻게 정리해야 할까?**

5차시 코드는 잘 동작하지만 60줄이 넘어 어디가 무슨 일을 하는지 찾기 어렵습니다. 같은 일을 하는 코드(새 게임 준비 등)가 반복되기도 합니다.

**함수**는 '하는 일' 하나에 이름을 붙인 코드 묶음입니다. 오늘은 동작은 그대로 두고 구조만 더 좋게 고치는 **리팩터링**으로 영단어 구조대를 함수 버전으로 바꿉니다.

## 함수의 모양

```python
def 비밀단어생성(words):          # def 함수이름(매개변수):
    """단어 목록에서 암호 하나를 골라 돌려준다"""   # 함수 설명
    return random.choice(words)   # return: 값을 돌려주고 함수 끝

비밀단어 = 비밀단어생성(words)    # 호출: 돌려받은 값을 변수에 저장
```

| 용어 | 뜻 | 예 |
| --- | --- | --- |
| 정의 | 함수를 만드는 것 | `def 비밀단어생성(words):` |
| 호출 | 함수를 실행하는 것 | `비밀단어생성(words)` |
| 매개변수 | 함수가 받는 값의 이름 | `words` |
| 반환값 | 함수가 돌려주는 결과 | 고른 단어 |

## 영단어 구조대 함수 설계표

| 함수 | 매개변수 | 반환값 | 하는 일 |
| --- | --- | --- | --- |
| `구조대게임소개()` | 없음 | 없음 | 제목과 규칙 출력 |
| `비밀단어생성(words)` | 단어 목록 | 암호 | 무작위로 고르기 |
| `게임화면생성(틀린단어, 맞춘단어, 비밀단어)` | 3개 | 없음 | 신호 그림·암호판 출력 |
| `알파벳한글자리턴(단어목록)` | 사용한 글자 | 올바른 한 글자 | 입력 검사 |
| `모두맞췄는지(비밀단어, 맞춘단어)` | 2개 | True/False | 종료 조건 ① 판단 |
| `게임재실행()` | 없음 | True/False | 다시 출동? |
| `main()` | 없음 | 없음 | 전체 흐름 조립 |

## return은 반복 중에도 함수를 끝낸다

```python
def 모두맞췄는지(비밀단어, 맞춘단어):
    for 글자 in 비밀단어:
        if 글자 not in 맞춘단어:
            return False          # 못 맞힌 글자를 찾는 순간 바로 끝
    return True                   # 끝까지 다 봤으면 True
```

4차시의 **깃발 변수**가 필요 없어졌습니다. `return`이 반복을 끊고 결과를 돌려주기 때문입니다.

```python
def 알파벳한글자리턴(단어목록):
    while True:
        guess = input('알파벳 한 글자 > ').strip().lower()
        ...
        else:
            return guess          # while True 의 출구 = return
```

## main()과 if __name__ == '__main__':

```python
def main():
    구조대게임소개()
    비밀단어 = 비밀단어생성(words)
    ...

if __name__ == '__main__':   # 이 파일을 직접 실행할 때만
    main()
```

`main()` 안을 읽으면 게임 전체 흐름이 한눈에 보입니다. 함수 이름이 곧 **주석** 역할을 합니다.

## 실행 예시

`new_rescue_2_function.py`를 실행한 화면입니다. `>` 뒤의 글자가 키보드로 입력한 값입니다. 구조에 성공한 뒤 `n`을 입력해 끝낸 화면입니다. (암호는 무작위로 정해지므로 실행할 때마다 달라집니다.)

```text
==================================================
 영단어 구조대 - 암호를 완성해 친구를 구조하세요!
 알파벳 한 글자씩 입력, 6번 틀리면 신호가 끊겨요.
==================================================
[■■■■■■] 구조 신호 아주 강함 - 구조대가 친구의 위치를 알고 있어요
틀린 글자: 
_ _ _ _ _ _ 
알파벳 한 글자 > z
[■■■■■□] 구조 신호 강함
틀린 글자: z
_ _ _ _ _ _ 
알파벳 한 글자 > e
[■■■■■□] 구조 신호 강함
틀린 글자: z
_ _ _ e _ _ 
알파벳 한 글자 > a
[■■■■□□] 구조 신호 양호
틀린 글자: za
_ _ _ e _ _ 
알파벳 한 글자 > f
[■■■■□□] 구조 신호 양호
틀린 글자: za
f _ _ e _ _ 
알파벳 한 글자 > r
[■■■■□□] 구조 신호 양호
틀린 글자: za
f r _ e _ _ 
알파벳 한 글자 > i
[■■■■□□] 구조 신호 양호
틀린 글자: za
f r i e _ _ 
알파벳 한 글자 > e
이미 입력한 글자입니다. 다른 글자를 고르세요.
알파벳 한 글자 > n
[■■■■□□] 구조 신호 양호
틀린 글자: za
f r i e n _ 
알파벳 한 글자 > d
구조 성공! 암호 friend로 헬기가 출동해 친구가 무사히 돌아왔어요!
다시 출동할까요? (y/n) > n
오늘도 수고했어요, 구조대원님!
```

## 전체 코드

이번 차시의 **전체 프로그램**입니다. 주석(`#` 뒤의 설명)을 함께 읽으며 따라가 보세요.

1. 코드 블록 전체를 복사합니다. (코드 블록 오른쪽 위 복사 버튼 또는 드래그 후 Ctrl + C)
2. IDLE에서 **File → New File**을 열고 붙여 넣습니다. (Ctrl + V)
3. 아래 파일 이름으로 저장한 뒤 **F5**로 실행합니다. (VS Code는 ▶ 실행 버튼)

### new_rescue_2_function.py

```python
# =====================================================================
# 영단어 구조대 (함수 버전)                                [6차시]
#   하위 문제 하나 = 함수 하나  /  매개변수로 받고 return 으로 돌려준다  /  main() 구조
#
# 5차시 코드를 '하는 일'별로 나누어 이름을 붙였어요.
#   함수 이름              받는 값(매개변수)               돌려주는 값(반환값)
#   구조대게임소개()        없음                            없음 (화면 출력만)
#   비밀단어생성(words)     단어 목록                       고른 암호 (문자열)
#   게임화면생성(...)       틀린단어, 맞춘단어, 비밀단어      없음 (화면 출력만)
#   알파벳한글자리턴(...)   이미 사용한 글자들               올바른 알파벳 한 글자
#   모두맞췄는지(...)       비밀단어, 맞춘단어               True / False
#   게임재실행()            없음                            True / False
#   main()                 없음                            없음 (전체 흐름 조립)
#
# 실행 방법: python new_rescue_2_function.py
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

def 구조대게임소개():
    """게임 제목과 규칙을 출력한다 (반환값 없음)"""
    print('=' * 50)
    print(' 영단어 구조대 - 암호를 완성해 친구를 구조하세요!')
    print(f' 알파벳 한 글자씩 입력, {len(신호그림) - 1}번 틀리면 신호가 끊겨요.')
    print('=' * 50)

def 비밀단어생성(words):
    """단어 목록에서 암호(비밀 단어) 하나를 무작위로 골라 돌려준다"""
    return random.choice(words)

def 게임화면생성(틀린단어, 맞춘단어, 비밀단어):
    """신호 그림, 틀린 글자, 밑줄 암호를 출력한다 (반환값 없음)"""
    print(신호그림[len(틀린단어)])           # 틀린 횟수 = 신호 그림 인덱스
    print('틀린 글자:', 틀린단어)
    for 글자 in 비밀단어:
        if 글자 in 맞춘단어:
            print(글자, end=' ')
        else:
            print('_', end=' ')
    print()

def 알파벳한글자리턴(단어목록):
    """공백 제거·소문자 변환 후, 쓰지 않은 알파벳 한 글자가 들어올 때까지 다시 묻는다

    단어목록: 지금까지 말한 글자들 (틀린단어 + 맞춘단어)
    """
    while True:
        guess = input('알파벳 한 글자 > ').strip().lower()
        if len(guess) != 1:
            print('한 글자만 입력해 주세요.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('알파벳(a~z)만 입력해 주세요.')
        elif guess in 단어목록:
            print('이미 입력한 글자입니다. 다른 글자를 고르세요.')
        else:
            return guess                     # return 을 만나면 반복 중이어도 함수가 바로 끝난다

def 모두맞췄는지(비밀단어, 맞춘단어):
    """암호의 글자를 모두 맞혔으면 True, 아니면 False 를 돌려준다"""
    for 글자 in 비밀단어:
        if 글자 not in 맞춘단어:
            return False                     # 못 맞힌 글자를 하나라도 찾으면 바로 False
    return True                              # 끝까지 다 봤는데 없으면 True (깃발 변수가 필요 없어졌다!)

def 게임재실행():
    """'y'(또는 yes 등 y로 시작하는 답)이면 True 를 돌려준다"""
    return input('다시 출동할까요? (y/n) > ').strip().lower().startswith('y')

def main():
    """게임 전체 흐름: 함수들을 차례로 불러 조립한다"""
    구조대게임소개()
    비밀단어 = 비밀단어생성(words)
    맞춘단어, 틀린단어 = '', ''
    while True:
        게임화면생성(틀린단어, 맞춘단어, 비밀단어)
        guess = 알파벳한글자리턴(틀린단어 + 맞춘단어)
        if guess in 비밀단어:                         # 판정은 main 안의 if 문으로
            맞춘단어 = 맞춘단어 + guess
            if 모두맞췄는지(비밀단어, 맞춘단어):
                print(f'구조 성공! 암호 {비밀단어}로 헬기가 출동해 친구가 무사히 돌아왔어요!')
                if not 게임재실행():
                    break
                비밀단어, 맞춘단어, 틀린단어 = 비밀단어생성(words), '', ''   # 새 출동 준비
        else:
            틀린단어 = 틀린단어 + guess
            if len(틀린단어) == len(신호그림) - 1:
                print(신호그림[len(틀린단어)])
                print(f'신호가 끊겼어요. 암호는 {비밀단어}였어요.')
                if not 게임재실행():
                    break
                비밀단어, 맞춘단어, 틀린단어 = 비밀단어생성(words), '', ''
    print('오늘도 수고했어요, 구조대원님!')

# 이 파일을 직접 실행할 때만 main()을 부른다 (다른 파일에서 import 할 때는 실행되지 않음)
if __name__ == '__main__':
    main()
```

파일 받기: [new_rescue_2_function.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_2_function.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_2_function.py)

## 실습 활동

1. 5차시 코드와 6차시 코드를 나란히 놓고, 5차시 코드의 각 부분이 어느 함수로 옮겨졌는지 표시하세요.
2. IDLE 셸에서 `모두맞췄는지('help', 'phle')`, `모두맞췄는지('help', 'hp')`를 호출해 결과를 확인하세요.
3. `구조대게임소개()`에 '틀려도 괜찮아요. 다시 출동할 수 있어요!' 문장을 추가해 보세요.
4. `main()` 안의 '새 출동 준비' 코드가 두 번 반복됩니다. 이것을 줄일 방법을 모둠별로 이야기해 보세요.

활동지: [new_ws06-function.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws06-function.md)

## 도전 과제 (기본 · 응용 · 심화)

자신의 속도에 맞게 골라 도전하세요. 기본을 마치면 응용, 응용을 마치면 심화로!

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | `게임재실행()`이 'yes', 'Y'에도 True를 돌려주는지 확인하기 |
| 응용 | `밑줄단어(비밀단어, 맞춘단어)` 함수를 만들어 암호판을 **문자열로 돌려주게** 바꾸기 |
| 심화 | `한판진행()` 함수를 만들어 한 판의 결과(True/False)를 돌려주게 하고, main()에서 구조 횟수를 세기 |

## 확인 퀴즈

**Q1.** 함수를 정의할 때 쓰는 키워드는?

- ① func
- ② def
- ③ function
- ④ return

**Q2.** `모두맞췄는지('safe', 'efas')`의 반환값은?

- ① True
- ② False
- ③ 'safe'
- ④ None

**Q3.** 다음 설명 중 옳지 **않은** 것은?

- ① return은 값을 돌려준다
- ② return을 만나면 함수가 끝난다
- ③ return은 반복문 안에서 쓸 수 없다
- ④ 반환값이 없는 함수도 있다

**Q4.** `def 게임화면생성(틀린단어, 맞춘단어, 비밀단어):`에서 괄호 안의 이름들을 무엇이라 하는가?

- ① 반환값
- ② 매개변수
- ③ 전역 상수
- ④ 모듈

**Q5.** `if __name__ == '__main__':`의 역할은?

- ① 오류를 막는다
- ② 파일을 직접 실행할 때만 main()을 실행한다
- ③ main 함수를 정의한다
- ④ 프로그램을 끝낸다

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 모두맞췄는지 함수 (기본)

`모두맞췄는지(비밀단어, 맞춘단어)` 함수를 만드세요. 첫째 줄에 암호, 둘째 줄에 n, 다음 n줄에 맞춘 글자들이 주어지면 각 줄마다 함수의 결과(True/False)를 출력합니다.

- 입력: 암호, n, n줄의 맞춘 글자들
- 출력: 각 줄의 True/False

예제 입력 1

```text
help
3
phle
hel
lphez
```

예제 출력 1

```text
True
False
True
```

### 문제 2. 구조대 위치 함수 (도전)

`구조대위치(비밀단어, 맞춘단어)` 함수를 만드세요. 암호에서 공개된 칸 수를 세어 `칸 = 공개칸 * 10 // 글자 수`를 구한 뒤 `'구조대 [' + '=' * 칸 + '>' + ' ' * (10 - 칸) + '] 친구'`를 돌려줍니다. 첫째 줄에 암호, 둘째 줄에 n, 다음 n줄의 맞춘 글자들마다 결과를 출력하세요. (맞춘 글자가 빈 줄일 수 있음)

- 입력: 암호, n, n줄의 맞춘 글자들
- 출력: 각 줄의 구조대 위치 문자열

예제 입력 1

```text
help
3

hp
help
```

예제 출력 1

```text
구조대 [>          ] 친구
구조대 [=====>     ] 친구
구조대 [==========>] 친구
```

정답과 해설은 **[부록] 04-1-06. 6차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-06-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 함수 = 하는 일 하나에 붙인 이름
- 매개변수로 받고 return으로 돌려준다
- return은 반복 중이어도 함수를 즉시 끝낸다
- main()을 읽으면 전체 흐름이 보인다

## 수업 흐름 (45분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 5분 | 긴 코드에서 '입력 검사 부분' 찾기 경쟁 |
| 전개 1 | 15분 | def·매개변수·return, 함수 설계표 |
| 전개 2 | 15분 | 5차시 코드 → 함수 버전 대응, 호출 실험 |
| 정리 | 10분 | 확인 퀴즈, 코딩 테스트 |

## 교사용 메모

- 함수 이름을 한글로 쓴 것은 **역할이 바로 읽히도록** 하기 위한 수업용 선택입니다. 파이썬은 한글 이름을 허용하지만, 실무에서는 영어 이름을 주로 쓴다는 점을 알려 주고 영어 버전(`source/extra/new_word_rescue_english.py`)과 비교하게 할 수 있습니다.
- 'main()에서 새 출동 준비 코드가 두 번 반복된다'는 연습 4번은 정답이 하나가 아닙니다. 한판진행() 함수로 묶는 방법(7차시 코드)을 미리 보여 주지 말고 아이디어를 모읍니다.
- 반환값이 있는 함수와 없는 함수(출력만 하는 함수)를 구분하는 것이 이 차시의 핵심 오개념 지점입니다. `x = 게임화면생성(...)`의 x가 None이 되는 것을 보여 주세요.

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `new_rescue_2_function.py` | [new_rescue_2_function.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_2_function.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_2_function.py) |
| 학습용 PPT | [new_06-function.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/new_06-function.pptx) |
| 학생 활동지 | [new_ws06-function.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws06-function.md) |
| 코딩 테스트 1 정답 코드 | [new_ch06_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch06_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch06_test1.py) |
| 코딩 테스트 2 정답 코드 | [new_ch06_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch06_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch06_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
