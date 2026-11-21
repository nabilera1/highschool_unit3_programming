> 7차시 **이상한 입력 넣어 보고 고치기 – 테스트와 개선**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `" H ".strip().lower()`의 결과는?

- ① `" h "`
- ② `"h"`
- ③ `"H"`
- ④ `" H"`

> **정답: ② "h"**  
> `strip()`이 앞뒤 공백을 지우고 `lower()`가 소문자로 바꿉니다.

**Q2.** 입력 검사가 없는 버전에서 빈 입력(그냥 Enter)을 넣으면?

- ① 배터리가 한 칸 준다
- ② 아무 변화 없이 다시 묻는다(공짜 입력)
- ③ 구조 성공
- ④ 오류로 멈춘다

> **정답: ② 아무 변화 없이 다시 묻는다(공짜 입력)**  
> `"" in "help"`는 항상 True라서 "틀리지 않은 것"으로 처리되고, 암호판도 바뀌지 않습니다.

**Q3.** `"가".isalpha()`의 결과와 그 때문에 게임에서 쓰는 검사 방법을 바르게 짝지은 것은?

- ① `False – isalpha() 사용`
- ② `True – "abc…z" 안에 있는지로 검사`
- ③ `True – isalpha() 사용`
- ④ 오류 – 한글은 입력 불가

> **정답: ② True – "abc…z" 안에 있는지로 검사**  
> 한글도 문자라서 isalpha()가 True입니다. 그래서 알파벳 목록 안에 있는지로 검사합니다.

**Q4.** 다음 중 **경계** 테스트 케이스에 가장 가까운 것은?

- ① 정상 글자 e 입력
- ② 배터리 1칸 남았을 때 틀린 글자 입력
- ③ 한글 입력
- ④ 두 글자 입력

> **정답: ② 배터리 1칸 남았을 때 틀린 글자 입력**  
> 배터리가 1칸에서 0칸이 되는 순간처럼, 규칙이 바뀌는 경계에서 시험하는 것이 경계 테스트입니다.

**Q5.** ask_letter()가 올바른 입력이 들어올 때까지 다시 묻기 위해 쓰는 구조는?

- ① `if 문 하나`
- ② `for i in range(3)`
- ③ `while True 와 return`
- ④ `try 문`

> **정답: ③ while True 와 return**  
> `while True`로 계속 묻다가 검사를 통과하면 `return g`로 함수와 반복을 함께 끝냅니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ② | ③ |

## 코딩 테스트 1. 입력 다듬고 검사하기

```python
n = int(input())
for i in range(n):
    g = input().strip().lower()
    if len(g) != 1:
        print("한 글자만")
    elif g not in "abcdefghijklmnopqrstuvwxyz":
        print("알파벳만")
    else:
        print("OK", g)
```

**해설** 검사 순서가 중요합니다. 길이를 먼저 보아야 빈 입력과 두 글자를 걸러 낼 수 있습니다.

정답 코드 파일: [lesson07_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson07_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson07_test1.py)

## 코딩 테스트 2. 이미 말한 글자 걸러 내기

```python
guessed = []
n = int(input())
for i in range(n):
    g = input().strip().lower()
    if len(g) != 1:
        print("한 글자만")
    elif g not in "abcdefghijklmnopqrstuvwxyz":
        print("알파벳만")
    elif g in guessed:
        print("이미 말한 글자")
    else:
        guessed.append(g)
        print("OK", g)
print("guessed:", guessed)
```

**해설** 게임의 `ask_letter()`와 같은 검사입니다. 대문자 E도 `lower()` 뒤에는 e가 되어 이미 말한 글자로 걸러집니다.

정답 코드 파일: [lesson07_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson07_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson07_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
- 정답 코드는 하나의 예시입니다. 출력이 같고 경계·예외 입력에도 올바르면 다른 풀이도 정답입니다.
