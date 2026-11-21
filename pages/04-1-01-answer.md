> 1차시 **영단어 구조대 플레이하고 규칙 찾기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** 영단어 구조대에서 암호에 **없는** 글자를 입력하면 어떻게 되는가?

- ① 암호가 바뀐다
- ② 구조 신호 배터리가 한 칸 줄어든다
- ③ 게임이 바로 끝난다
- ④ 아무 일도 없다

> **정답: ② 구조 신호 배터리가 한 칸 줄어든다**  
> 암호에 없는 글자를 말하면 `battery`가 1 줄어 배터리 그림의 ■ 하나가 □로 바뀝니다.

**Q2.** 한 번 출동(한 판)이 끝나는 조건 두 가지로 옳은 것은?

- ① 모두 맞힘, 배터리 0칸
- ② 10번 입력, 배터리 0칸
- ③ 모두 맞힘, 시간 초과
- ④ 첫 글자 맞힘, 마지막 글자 맞힘

> **정답: ① 모두 맞힘, 배터리 0칸**  
> 암호의 글자를 모두 맞히면 구조 성공, 배터리가 0칸이 되면 신호가 끊깁니다.

**Q3.** 다음 중 게임의 **입력**에 해당하는 것은?

- ① 암호판 출력
- ② 알파벳 한 글자
- ③ 구조 성공 메시지
- ④ 출동 기록표

> **정답: ② 알파벳 한 글자**  
> 플레이어가 키보드로 넣는 알파벳 한 글자가 입력이고, 나머지는 모두 출력입니다.

**Q4.** `MAX_BATTERY = 6`, `battery = 4`일 때 지금까지 틀린 횟수를 구하는 식은?

- ① `battery`
- ② `MAX_BATTERY + battery`
- ③ `MAX_BATTERY - battery`
- ④ `len(battery)`

> **정답: ③ MAX_BATTERY - battery**  
> 처음 6칸에서 남은 4칸을 빼면 틀린 횟수 2가 됩니다. 같은 정보를 변수 두 개에 따로 저장하지 않아도 됩니다.

**Q5.** 알고리즘에 대한 설명으로 가장 알맞은 것은?

- ① 컴퓨터 부품의 이름
- ② 문제를 해결하는 명확한 절차
- ③ 파이썬의 예약어
- ④ 게임 그림 파일

> **정답: ② 문제를 해결하는 명확한 절차**  
> 알고리즘은 문제를 해결하기 위한 명확하고 유한한 절차입니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ① | ② | ③ | ② |

## 코딩 테스트 1. 밑줄 암호 만들기

```python
word = input()
print(f"글자 수: {len(word)}")
print(" ".join(["_"] * len(word)))
```

**해설** `["_"] * 4`는 `["_", "_", "_", "_"]`이고, `" ".join()`이 사이에 공백을 넣어 이어 붙입니다. `print("_ " * len(word))`로 쓰면 끝에 공백이 하나 더 붙어 출력이 달라지므로 주의합니다.

정답 코드 파일: [lesson01_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson01_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson01_test1.py)

## 코딩 테스트 2. 이 글자는 몇 번?

```python
word = input()
g = input()
count = 0
for ch in word:
    if ch == g:
        count += 1
if count > 0:
    print(f"{count}번 있어요")
else:
    print("없어요")
```

**해설** 글자를 하나씩 꺼내 같으면 `count`를 1 늘리는 **누적** 패턴입니다. `word.count(g)`로도 풀 수 있지만, 반복으로 직접 세는 방법을 먼저 익힙니다.

정답 코드 파일: [lesson01_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson01_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson01_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
- 정답 코드는 하나의 예시입니다. 출력이 같고 경계·예외 입력에도 올바르면 다른 풀이도 정답입니다.
