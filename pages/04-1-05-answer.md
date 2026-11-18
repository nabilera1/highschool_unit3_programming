> 5차시 **테스트 케이스로 오류 찾고 입력 검사하기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `' He '.strip().lower()`의 결과는?

- ① ' he '
- ② 'He'
- ③ 'he'
- ④ 'HE'

> **정답: ③ 'he'**  
> strip()으로 앞뒤 공백을 지우고 lower()로 소문자가 됩니다.

**Q2.** `'' in 'help'`의 결과는?

- ① True
- ② False
- ③ None
- ④ 오류

> **정답: ① True**  
> 빈 문자열은 모든 문자열에 포함된 것으로 판단됩니다. 그래서 빈 입력을 따로 걸러야 합니다.

**Q3.** 다음 중 '예외' 테스트 케이스에 해당하는 것은?

- ① e
- ② p
- ③ 3
- ④ a

> **정답: ③ 3**  
> 숫자 3은 알파벳 규칙을 벗어난 예외 입력입니다.

**Q4.** `len(guess) != 1` 검사를 가장 먼저 하는 이유는?

- ① 속도가 빨라서
- ② 'ab' in 알파벳이 True라서 두 글자를 먼저 걸러야 해서
- ③ 오류 메시지가 짧아서
- ④ 순서는 상관없다

> **정답: ② 'ab' in 알파벳이 True라서 두 글자를 먼저 걸러야 해서**  
> 'ab'는 알파벳 목록 안에 연속으로 들어 있어 in 검사를 통과해 버립니다.

**Q5.** `'ㅎ'.isalpha()`의 결과는?

- ① True
- ② False
- ③ 오류
- ④ None

> **정답: ① True**  
> isalpha()는 한글 자모도 문자로 보아 True입니다. 영어 알파벳만 허용하려면 따로 검사해야 합니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ③ | ① | ③ | ② | ① |

## 코딩 테스트 1. 입력 다듬고 검사하기

```python
알파벳 = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
for _ in range(n):
    guess = input().strip().lower()
    if len(guess) != 1:
        print('한 글자만')
    elif guess not in 알파벳:
        print('알파벳만')
    else:
        print('OK', guess)
```

**해설** 게임의 입력 검사 부분만 떼어 낸 문제입니다. 빈 줄은 `strip()` 후 길이가 0이므로 '한 글자만'으로 처리됩니다. 한글 `ㅎ`은 알파벳 목록에 없으므로 '알파벳만'입니다.

정답 코드 파일: [new_ch05_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch05_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch05_test1.py)

## 코딩 테스트 2. 이미 입력한 글자 걸러 내기

```python
알파벳 = 'abcdefghijklmnopqrstuvwxyz'
사용한글자 = ''
n = int(input())
for _ in range(n):
    guess = input().strip().lower()
    if len(guess) != 1:
        print('한 글자만')
    elif guess not in 알파벳:
        print('알파벳만')
    elif guess in 사용한글자:
        print('이미 입력')
    else:
        사용한글자 += guess
        print('OK', guess)
print('사용한 글자:', 사용한글자)
```

**해설** `E`는 소문자로 바뀐 뒤 `e`와 같아지므로 '이미 입력'입니다. 다듬기를 검사보다 **먼저** 해야 하는 이유를 보여 주는 테스트 케이스입니다.

정답 코드 파일: [new_ch05_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch05_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch05_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
