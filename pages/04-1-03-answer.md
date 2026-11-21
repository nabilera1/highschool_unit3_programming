> 3차시 **문자열·리스트·딕셔너리로 암호판 만들기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `for ch in "help":`에서 `ch`에 차례로 들어가는 값은?

- ① `"help" 한 번`
- ② `"h", "e", "l", "p"`
- ③ 0, 1, 2, 3
- ④ `"p", "l", "e", "h"`

> **정답: ② "h", "e", "l", "p"**  
> 문자열을 for 문으로 돌리면 앞에서부터 글자를 하나씩 꺼냅니다.

**Q2.** `" ".join(["h", "_", "_", "p"])`의 결과는?

- ① `"h__p"`
- ② `"h _ _ p"`
- ③ `["h _ _ p"]`
- ④ `"h,_,_,p"`

> **정답: ② "h _ _ p"**  
> `join()`은 리스트의 문자열들을 앞의 문자열(공백)로 이어 붙입니다.

**Q3.** `WORDS = {"help": "도움", "safe": "안전한"}`일 때 `WORDS["help"]`의 값은?

- ① `"help"`
- ② `"도움"`
- ③ 0
- ④ 오류

> **정답: ② "도움"**  
> 딕셔너리는 키(영단어)로 값(뜻)을 찾습니다.

**Q4.** 단어장 `WORDS`에 `"care": "돌봄"`을 추가하는 코드는?

- ① `WORDS.append("care")`
- ② `WORDS["care"] = "돌봄"`
- ③ `WORDS["돌봄"] = "care"`
- ④ `WORDS = {"care": "돌봄"}`

> **정답: ② WORDS["care"] = "돌봄"**  
> `딕셔너리[새 키] = 값`으로 추가합니다. ④는 단어장 전체를 새것으로 바꾸어 기존 단어가 사라집니다.

**Q5.** `random.choice(list(WORDS))`가 돌려주는 것은?

- ① 뜻 하나
- ② 영단어(키) 하나
- ③ `(영단어, 뜻) 쌍`
- ④ 단어장 전체

> **정답: ② 영단어(키) 하나**  
> `list(WORDS)`는 키만 모은 리스트입니다. 그중 하나를 고르므로 영단어가 나옵니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ② | ② |

## 코딩 테스트 1. 밑줄 암호판 출력

```python
word = input()
guessed = list(input())          # "hp" → ["h", "p"]
board = []
for ch in word:
    if ch in guessed:
        board.append(ch)
    else:
        board.append("_")
print(" ".join(board))
```

**해설** 게임의 암호판 코드와 같습니다. `list("hp")`는 `["h", "p"]`가 됩니다. together처럼 같은 글자가 여러 번 나와도 모두 공개됩니다.

정답 코드 파일: [lesson03_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson03_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson03_test1.py)

## 코딩 테스트 2. 뜻 힌트 사전

```python
WORDS = {}
n = int(input())
for i in range(n):
    eng, kor = input().split()
    WORDS[eng] = kor              # 딕셔너리에 추가
m = int(input())
for i in range(m):
    w = input()
    if w in WORDS:                # 키가 있는지 먼저 확인
        print(WORDS[w])
    else:
        print("단어장에 없어요")
```

**해설** 빈 딕셔너리 `{}`에 한 줄씩 추가해 단어장을 만듭니다. 없는 키를 바로 꺼내면 `KeyError`가 나므로 `in`으로 먼저 확인합니다.

정답 코드 파일: [lesson03_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson03_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson03_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
- 정답 코드는 하나의 예시입니다. 출력이 같고 경계·예외 입력에도 올바르면 다른 풀이도 정답입니다.
