> 8차시 **나만의 영단어 구조대 발표와 형성평가**의 형성평가 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 형성평가 1~10번 정답

**1번.** `word = "rescue"`일 때 `word[2]`의 값은?

- ① `"r"`
- ② `"e"`
- ③ `"s"`
- ④ `"c"`

> **정답: ③ "s"**  
> 문자열의 번호는 0부터 시작합니다. r(0), e(1), s(2)입니다.

**2번.** `records = [[1, "help", "성공", 1], [2, "safe", "실패", 6], [3, "rescue", "성공", 2]]`일 때 `records[1][2]`의 값은?

- ① `"help"`
- ② `"성공"`
- ③ `"실패"`
- ④ 6

> **정답: ③ "실패"**  
> records[1]은 2번 출동 [2, "safe", "실패", 6]이고, 그중 2번 칸은 "실패"입니다.

**3번.** 2번 문제의 records에서 `records[0]`이 뜻하는 것은?

- ① 1번 출동의 기록 전체 (한 행)
- ② 모든 출동의 암호 목록 (한 열)
- ③ 1번 출동의 결과 칸
- ④ 기록표의 행 개수

> **정답: ① 1번 출동의 기록 전체 (한 행)**  
> 2차원 리스트에서 [ ]를 하나만 쓰면 행 하나(리스트)를 꺼냅니다.

**4번.** `WORDS = {"help": "도움", "safe": "안전한"}`일 때 `WORDS["safe"]`의 값은?

- ① `"help"`
- ② `"safe"`
- ③ `"안전한"`
- ④ 오류

> **정답: ③ "안전한"**  
> 딕셔너리는 키(영단어)로 값(뜻)을 찾습니다.

**5번.** (단답형) 2번 문제의 records로 `print_records(records)`를 실행할 때, 안쪽 for 문(칸 하나를 처리하는 반복)은 모두 몇 번 반복될까?

- 답: ____________________

> **정답: 16번**  
> 바깥 for는 머리글 행을 포함해 4번, 안쪽 for는 한 행의 칸 4개만큼 4번 돌므로 4 × 4 = 16번입니다.

**6번.** 단어장 `WORDS`에 "together"(함께)를 추가하는 코드로 알맞은 것은?

- ① `WORDS.append("together")`
- ② `WORDS["together"] = "함께"`
- ③ `WORDS["함께"] = "together"`
- ④ `WORDS = {"together": "함께"}`

> **정답: ② WORDS["together"] = "함께"**  
> ③은 키와 값이 바뀌었고, ④는 단어장 전체를 새것으로 바꾸어 기존 단어가 사라집니다.

**7번.** `make_board("help", ["p"])`의 결과는?

- ① `"h e l p"`
- ② `"_ _ _ p"`
- ③ `"p _ _ _"`
- ④ `"p"`

> **정답: ② "_ _ _ p"**  
> guessed에 있는 글자(p)는 그대로, 나머지는 _로 바꾼 뒤 공백으로 이어 붙입니다.

**8번.** `"z" in "rescue"`의 결과는?

- ① `True`
- ② `False`
- ③ `"z"`
- ④ 0

> **정답: ② False**  
> 없으므로 False이고, 게임에서는 구조 신호 배터리가 1칸 줄어듭니다.

**9번.** `MAX_BATTERY = 6`일 때 `make_battery(4)`의 결과는?

- ① ■■■■□□
- ② ■■□□□□
- ③ ■■■■■■
- ④ □□□□■■

> **정답: ① ■■■■□□**  
> ■를 4번, □를 6 - 4 = 2번 이어 붙입니다.

**10번.** (단답형) play() 안에서 암호를 모두 맞혔는지(구조 성공) 확인하는 조건식을 쓰시오. (`board = make_board(word, guessed)`)

- 답: ____________________

> **정답: "_" not in board**  
> 암호판에 _가 남아 있지 않다는 것은 모든 글자를 맞혔다는 뜻입니다.

| 문항 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 정답 | ③ | ③ | ① | ③ | 16번 | ② | ② | ② | ① | "_" not in board |

## 형성평가 11번. print_success 함수

```python
def print_success(records):
    for row in records:
        if row[2] == "성공":
            print(row[1])

records = []
n = int(input())
for i in range(n):
    no, word, result, wrong = input().split()
    records.append([int(no), word, result, int(wrong)])
print_success(records)
```

**해설** 바깥 for로 행(출동)을 하나씩 꺼내고, 2번 칸(결과)이 "성공"인 행만 골라 1번 칸(암호)을 출력합니다.

정답 코드 파일: [lesson08_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson08_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson08_test1.py)

## 형성평가 12번. count_wrong 함수

```python
def count_wrong(word, guessed):
    count = 0
    for g in guessed:
        if g not in word:
            count += 1
    return count

word = input()
guessed = input().split()
print(count_wrong(word, guessed))
```

**해설** guessed의 글자를 하나씩 보며 암호에 없는 글자만 셉니다. 개수는 `return`으로 돌려주어야 다른 곳에서 쓸 수 있습니다.

정답 코드 파일: [lesson08_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson08_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson08_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
- 정답 코드는 하나의 예시입니다. 출력이 같고 경계·예외 입력에도 올바르면 다른 풀이도 정답입니다.
