> 6차시 **출동 기록표 – 2차원 리스트와 중첩 for 문**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `records = [[1, "help", "성공", 1], [2, "safe", "실패", 6]]`일 때 `records[1][2]`의 값은?

- ① `"help"`
- ② `"성공"`
- ③ `"실패"`
- ④ 6

> **정답: ③ "실패"**  
> 첫 번째 [ ]는 행(출동), 두 번째 [ ]는 칸입니다. 1번 행 [2, "safe", "실패", 6]의 2번 칸은 "실패"입니다.

**Q2.** 같은 records에서 `records[0]`이 뜻하는 것은?

- ① 1번 출동의 기록 전체(한 행)
- ② 모든 출동의 암호
- ③ 1번 출동의 결과
- ④ 행의 개수

> **정답: ① 1번 출동의 기록 전체(한 행)**  
> [ ]를 하나만 쓰면 행 하나(리스트)를 꺼냅니다.

**Q3.** 새 출동 기록 한 행을 추가하는 코드는?

- ① `records + [3, "hope", "성공", 0]`
- ② `records.append([3, "hope", "성공", 0])`
- ③ `records[3] = "hope"`
- ④ `records.add(3, "hope")`

> **정답: ② records.append([3, "hope", "성공", 0])**  
> `append()`에 리스트 하나를 넣으면 그 리스트가 새 행이 됩니다.

**Q4.** 행이 3개, 한 행의 칸이 4개인 records를 중첩 for로 모두 출력하면 안쪽 for 문은 모두 몇 번 반복되는가?

- ① 3번
- ② 4번
- ③ 7번
- ④ 12번

> **정답: ④ 12번**  
> 바깥 for가 3번, 그때마다 안쪽 for가 4번 돌아 3 × 4 = 12번입니다.

**Q5.** records에서 성공한 출동의 암호만 출력하는 코드로 알맞은 것은?

- ① 행마다 row[1]을 모두 출력한다
- ② 행마다 row[2]가 "성공"인지 보고, 맞으면 row[1]을 출력한다
- ③ `records["성공"]을 출력한다`
- ④ `records[2]가 "성공"이면 records[1]을 출력한다`

> **정답: ② 행마다 row[2]가 "성공"인지 보고, 맞으면 row[1]을 출력한다**  
> 행을 하나씩 꺼내 결과 칸(2번)이 "성공"인 행만 골라 암호 칸(1번)을 출력합니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ③ | ① | ② | ④ | ② |

## 코딩 테스트 1. 기록표에서 출동 찾기

```python
records = []
n = int(input())
for i in range(n):
    no, word, result, wrong = input().split()
    records.append([int(no), word, result, int(wrong)])   # 한 행 추가
k = int(input())
row = records[k - 1]                 # 출동 번호는 1부터, 행 번호는 0부터
print(f"{row[0]}번 출동: {row[1]} ({row[2]}, 틀린 횟수 {row[3]})")
```

**해설** 한 줄을 `split()`으로 나누어 숫자 칸은 `int()`로 바꾼 뒤 한 행으로 `append`합니다. k번 출동은 `k - 1`번 행입니다.

정답 코드 파일: [lesson06_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson06_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson06_test1.py)

## 코딩 테스트 2. 출동 기록 분석

```python
records = []
n = int(input())
for i in range(n):
    word, result, wrong = input().split()
    records.append([word, result, int(wrong)])

count = {"성공": 0, "실패": 0}          # 결과별 횟수 (딕셔너리)
best = None                          # 가장 아슬아슬한 구조 행
for row in records:
    count[row[1]] += 1
    if row[1] == "성공":
        if best is None or row[2] > best[2]:
            best = row
print(f"성공: {count['성공']}번")
print(f"실패: {count['실패']}번")
if best is None:
    print("성공 기록 없음")
else:
    print(f"가장 아슬아슬한 구조: {best[0]} (틀림 {best[2]})")
```

**해설** 행을 하나씩 보며 결과 칸으로 개수를 세고, 성공한 행 중 틀린 횟수 칸이 가장 큰 행을 기억합니다. `>`를 써야 같은 값일 때 먼저 나온 행이 남습니다.

정답 코드 파일: [lesson06_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson06_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson06_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
- 정답 코드는 하나의 예시입니다. 출력이 같고 경계·예외 입력에도 올바르면 다른 풀이도 정답입니다.
