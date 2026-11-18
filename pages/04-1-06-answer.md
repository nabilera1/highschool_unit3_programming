> 6차시 **함수로 나누어 코드 다듬기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 함수를 정의할 때 쓰는 키워드는?

- ① func
- ② def
- ③ function
- ④ return

> **정답: ② def**  
> 파이썬은 `def`로 함수를 정의합니다.

**Q2.** `모두맞췄는지('safe', 'efas')`의 반환값은?

- ① True
- ② False
- ③ 'safe'
- ④ None

> **정답: ① True**  
> s, a, f, e가 모두 맞춘단어에 들어 있으므로 True입니다.

**Q3.** 다음 설명 중 옳지 **않은** 것은?

- ① return은 값을 돌려준다
- ② return을 만나면 함수가 끝난다
- ③ return은 반복문 안에서 쓸 수 없다
- ④ 반환값이 없는 함수도 있다

> **정답: ③ return은 반복문 안에서 쓸 수 없다**  
> return은 반복문 안에서도 쓸 수 있고, 만나는 즉시 반복과 함수가 함께 끝납니다.

**Q4.** `def 게임화면생성(틀린단어, 맞춘단어, 비밀단어):`에서 괄호 안의 이름들을 무엇이라 하는가?

- ① 반환값
- ② 매개변수
- ③ 전역 상수
- ④ 모듈

> **정답: ② 매개변수**  
> 함수가 받는 값의 이름을 매개변수라고 합니다.

**Q5.** `if __name__ == '__main__':`의 역할은?

- ① 오류를 막는다
- ② 파일을 직접 실행할 때만 main()을 실행한다
- ③ main 함수를 정의한다
- ④ 프로그램을 끝낸다

> **정답: ② 파일을 직접 실행할 때만 main()을 실행한다**  
> 다른 파일에서 import할 때는 실행되지 않게 해 줍니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ① | ③ | ② | ② |

## 코딩 테스트 1. 모두맞췄는지 함수

```python
def 모두맞췄는지(비밀단어, 맞춘단어):
    for 글자 in 비밀단어:
        if 글자 not in 맞춘단어:
            return False
    return True

비밀단어 = input()
n = int(input())
for _ in range(n):
    print(모두맞췄는지(비밀단어, input()))
```

**해설** 게임 코드의 함수를 그대로 씁니다. 맞춘 글자에 암호에 없는 글자(z)가 섞여 있어도, 암호의 글자가 모두 들어 있으면 True입니다.

정답 코드 파일: [new_ch06_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch06_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch06_test1.py)

## 코딩 테스트 2. 구조대 위치 함수

```python
def 구조대위치(비밀단어, 맞춘단어):
    공개칸 = 0
    for 글자 in 비밀단어:
        if 글자 in 맞춘단어:
            공개칸 += 1
    칸 = 공개칸 * 10 // len(비밀단어)        # 0 ~ 10
    return '구조대 [' + '=' * 칸 + '>' + ' ' * (10 - 칸) + '] 친구'

비밀단어 = input()
n = int(input())
for _ in range(n):
    print(구조대위치(비밀단어, input()))
```

**해설** 3차시 '공개된 칸 세기'를 함수로 만들고, 비율을 0~10칸으로 바꾼 것입니다. `//`는 몫(소수점 버림)이라 칸 수가 항상 정수입니다. 7차시 산출물 예시 코드에 같은 함수가 들어 있습니다.

정답 코드 파일: [new_ch06_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch06_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch06_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
