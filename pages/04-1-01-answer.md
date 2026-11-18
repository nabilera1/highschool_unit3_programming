> 1차시 **영단어 구조대 플레이하고 알고리즘 찾기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 영단어 구조대에서 암호에 **없는** 글자를 입력하면 어떻게 되는가?

- ① 암호가 바뀐다
- ② 구조 신호 배터리가 한 칸 준다
- ③ 게임이 바로 끝난다
- ④ 아무 일도 없다

> **정답: ② 구조 신호 배터리가 한 칸 준다**  
> 틀린 글자마다 배터리가 한 칸씩 줄고, 6칸을 모두 쓰면 신호가 끊깁니다.

**Q2.** 게임의 종료 조건 두 가지로 옳은 것은?

- ① 모두 맞힘, 6번 틀림
- ② 10번 입력, 6번 틀림
- ③ 모두 맞힘, 시간 초과
- ④ 첫 글자 맞힘, 마지막 글자 맞힘

> **정답: ① 모두 맞힘, 6번 틀림**  
> 모든 글자를 맞히면 구조 성공, 6번 틀리면 신호 끊김으로 반복이 끝납니다.

**Q3.** 다음 중 '입력'에 해당하는 것은?

- ① 밑줄 암호 출력
- ② 알파벳 한 글자
- ③ 구조 성공 메시지
- ④ 신호 배터리 그림

> **정답: ② 알파벳 한 글자**  
> 사용자가 키보드로 넣는 값이 입력입니다. 나머지는 모두 출력입니다.

**Q4.** 틀린 횟수를 따로 변수로 세지 않고 구하는 방법은?

- ① len(비밀단어)
- ② len(맞춘단어)
- ③ len(틀린단어)
- ④ len(words)

> **정답: ③ len(틀린단어)**  
> 틀린 글자를 `틀린단어`에 이어 붙이므로 그 길이가 곧 틀린 횟수입니다.

**Q5.** 알고리즘에 대한 설명으로 가장 알맞은 것은?

- ① 컴퓨터 부품의 이름
- ② 문제를 해결하는 명확한 절차
- ③ 파이썬의 예약어
- ④ 게임 그림 파일

> **정답: ② 문제를 해결하는 명확한 절차**  
> 알고리즘은 문제를 해결하기 위한 단계적이고 명확한 절차입니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ① | ② | ③ | ② |

## 코딩 테스트 1. 밑줄 암호 만들기

```python
word = input()
print('글자 수:', len(word))
print(' '.join('_' * len(word)))    # '____' 의 글자 사이에 공백을 넣어 이어 붙인다
```

**해설** `'_' * 4`는 `'____'`입니다. `' '.join(문자열)`은 글자 사이에 공백을 넣어 `'_ _ _ _'`를 만듭니다. `print('_ ' * len(word))`로 써도 화면은 같지만 맨 끝에 공백이 하나 더 붙습니다.

정답 코드 파일: [new_ch01_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch01_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch01_test1.py)

## 코딩 테스트 2. 이 글자는 몇 번?

```python
word = input()
letter = input()
count = 0
for ch in word:          # 암호의 글자를 하나씩 보면서
    if ch == letter:     # 찾는 글자와 같으면
        count += 1       # 1 증가
if count > 0:
    print(f'{count}번 있어요')
else:
    print('없어요')
```

**해설** 반복하면서 조건에 맞을 때마다 1씩 더하는 **세기(카운트) 패턴**입니다. 파이썬의 `word.count(letter)`로도 같은 결과를 얻을 수 있습니다.

정답 코드 파일: [new_ch01_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch01_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch01_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
