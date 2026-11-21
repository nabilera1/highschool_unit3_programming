> 4차시 **함수로 나누기 – 함수 없는 코드와 함수 코드 비교**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 함수를 정의할 때 쓰는 키워드는?

- ① `func`
- ② `def`
- ③ `function`
- ④ `return`

> **정답: ② def**  
> 파이썬은 `def 함수이름(매개변수):`로 함수를 정의합니다.

**Q2.** `def make_board(word, guessed):`에서 괄호 안의 `word`, `guessed`를 무엇이라 하는가?

- ① 반환값
- ② 매개변수
- ③ 전역 상수
- ④ 모듈

> **정답: ② 매개변수**  
> 함수가 받는 값의 이름을 매개변수라고 합니다.

**Q3.** `make_battery(2)`의 결과는? (`MAX_BATTERY = 6`)

- ① ■■□□□□
- ② ■■■■□□
- ③ □□■■■■
- ④ 2

> **정답: ① ■■□□□□**  
> ■를 2번, □를 6 - 2 = 4번 이어 붙입니다.

**Q4.** 함수 없는 코드(nofunc)와 함수 코드(full)를 비교한 설명으로 옳지 **않은** 것은?

- ① 두 코드는 같은 입력에 같은 화면을 출력한다
- ② 함수 코드는 같은 일을 이름 하나로 다시 쓸 수 있다
- ③ 함수 코드는 make_board() 하나만 따로 실행해 시험할 수 있다
- ④ 함수로 나누면 코드 줄 수가 항상 줄어든다

> **정답: ④ 함수로 나누면 코드 줄 수가 항상 줄어든다**  
> 이 게임에서는 오히려 함수 코드가 더 깁니다(69줄 대 56줄). 함수의 장점은 줄 수가 아니라 읽기·고치기·다시 쓰기·따로 시험하기입니다.

**Q5.** `if __name__ == "__main__":`의 역할은?

- ① 오류를 막는다
- ② 파일을 직접 실행할 때만 main()을 실행한다
- ③ `main 함수를 정의한다`
- ④ 프로그램을 끝낸다

> **정답: ② 파일을 직접 실행할 때만 main()을 실행한다**  
> 다른 파일에서 `import`할 때는 게임이 시작되지 않게 해 줍니다. 그래서 함수만 가져다 시험할 수 있습니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ① | ④ | ② |

## 코딩 테스트 1. is_rescued 함수

```python
def is_rescued(word, guessed):
    for ch in word:
        if ch not in guessed:
            return False          # 못 맞힌 글자를 하나라도 찾으면 바로 False
    return True                   # 끝까지 없으면 True

word = input()
n = int(input())
for i in range(n):
    print(is_rescued(word, list(input())))
```

**해설** `return`을 만나면 반복 중이어도 함수가 바로 끝납니다. 게임에서는 `"_" not in make_board(word, guessed)`와 같은 뜻입니다. 암호에 없는 글자(z)가 섞여 있어도 암호의 글자가 모두 있으면 True입니다.

정답 코드 파일: [lesson04_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson04_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson04_test1.py)

## 코딩 테스트 2. 구조대 위치 함수

```python
def rescue_bar(word, guessed):
    opened = 0
    for ch in word:
        if ch in guessed:
            opened += 1
    n = opened * 10 // len(word)          # 0 ~ 10칸
    return "구조대 [" + "=" * n + ">" + " " * (10 - n) + "] 친구"

word = input()
k = int(input())
for i in range(k):
    print(rescue_bar(word, list(input())))
```

**해설** 공개된 칸 세기와 그림 만들기를 함수 하나로 묶었습니다. `//`는 몫(소수점 버림)이라 칸 수가 항상 정수입니다. 만든 함수는 게임의 `play()` 안에서 `print(rescue_bar(word, guessed))` 한 줄로 다시 쓸 수 있습니다.

정답 코드 파일: [lesson04_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson04_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson04_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
- 정답 코드는 하나의 예시입니다. 출력이 같고 경계·예외 입력에도 올바르면 다른 풀이도 정답입니다.
