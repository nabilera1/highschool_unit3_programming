> 2차시 **규칙을 자료로 정리하기 – 단어장·암호·배터리**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `words = ["help", "safe", "hope"]`일 때 `words[1]`의 값은?

- ① `"help"`
- ② `"safe"`
- ③ `"hope"`
- ④ 오류

> **정답: ② "safe"**  
> 리스트의 번호(인덱스)는 0부터 시작합니다. 0번 help, 1번 safe입니다.

**Q2.** `random.choice(words)`가 하는 일은?

- ① 리스트를 정렬한다
- ② 리스트에서 하나를 무작위로 고른다
- ③ 리스트를 섞는다
- ④ 리스트의 길이를 센다

> **정답: ② 리스트에서 하나를 무작위로 고른다**  
> `random.choice()`는 리스트에서 값 하나를 무작위로 골라 돌려줍니다.

**Q3.** `word = "rescue"`일 때 `word[0]`과 `len(word)`의 값은?

- ① `"r", 6`
- ② `"e", 6`
- ③ `"r", 5`
- ④ `"rescue", 1`

> **정답: ① "r", 6**  
> 문자열도 글자들의 순서이므로 0번 글자는 r, 글자 수는 6입니다.

**Q4.** `guessed = ["h"]`에서 `guessed.append("x")`를 실행한 뒤의 `guessed`는?

- ① `["x"]`
- ② `["h", "x"]`
- ③ `["x", "h"]`
- ④ `"hx"`

> **정답: ② ["h", "x"]**  
> `append()`는 리스트의 맨 뒤에 값을 하나 붙입니다.

**Q5.** `"■" * 3 + "□" * 2`의 결과는?

- ① ■■■□□
- ② ■□■□■
- ③ ■3□2
- ④ 오류

> **정답: ① ■■■□□**  
> 문자열에 정수를 곱하면 그 횟수만큼 반복해 이어 붙입니다. 배터리 그림을 만드는 원리입니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ① | ② | ① |

## 코딩 테스트 1. 번호로 암호 꺼내기

```python
words = input().split()
k = int(input())
word = words[k - 1]          # 사람은 1부터, 파이썬은 0부터 센다
print(word, len(word))
```

**해설** `split()`은 공백을 기준으로 나누어 리스트를 만듭니다. 문제의 번호는 1부터, 인덱스는 0부터이므로 `k - 1`번을 꺼냅니다.

정답 코드 파일: [lesson02_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson02_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson02_test1.py)

## 코딩 테스트 2. 배터리 그림 그리기

```python
MAX_BATTERY = 6
k = int(input())
battery = MAX_BATTERY - k
print("[" + "■" * battery + "□" * k + "]")
print(f"남은 배터리: {battery}칸")
```

**해설** 남은 칸 수는 `6 - k`, 쓴 칸 수는 `k`입니다. 문자열 곱하기로 ■와 □를 이어 붙입니다. 게임의 `make_battery()`와 같은 원리입니다.

정답 코드 파일: [lesson02_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson02_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson02_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
- 정답 코드는 하나의 예시입니다. 출력이 같고 경계·예외 입력에도 올바르면 다른 풀이도 정답입니다.
