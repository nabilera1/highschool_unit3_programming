> **2부 게임 구현하기** · 6차시 · 수업 단계: **구현**  
> 핵심 개념: 2차원 리스트, 행·칸, records[행][칸], append로 행 쌓기, 중첩 for 문, 조건으로 행 고르기

## 학습 목표

1. 출동 기록을 2차원 리스트에 행 단위로 쌓고, `records[행][칸]`으로 값을 읽을 수 있다.
2. 중첩 for 문으로 2차원 리스트 전체를 표로 출력할 수 있다.
3. 행을 하나씩 보며 조건에 맞는 행만 골라 내거나 한 칸(열)을 모아 계산할 수 있다.

## 핵심 질문

> **여러 번 출동한 결과를 어떻게 모아 두고, 표로 보여 줄 수 있을까?**

5차시의 `play()`는 한 판이 끝나면 `(성공 여부, 틀린 횟수)`를 돌려줍니다. 출동할 때마다 이 결과를 **한 줄(행)씩** 쌓으면 출동 기록표가 됩니다.

## 2차원 리스트: 리스트를 담은 리스트

```python
records = [[1, "help", "성공", 1],
           [2, "safe", "실패", 6],
           [3, "rescue", "성공", 2]]
```

| | 0번 칸: 출동 | 1번 칸: 암호 | 2번 칸: 결과 | 3번 칸: 틀린 횟수 |
| --- | --- | --- | --- | --- |
| **0번 행** | 1 | help | 성공 | 1 |
| **1번 행** | 2 | safe | 실패 | 6 |
| **2번 행** | 3 | rescue | 성공 | 2 |

| 코드 | 값 | 읽는 법 |
| --- | --- | --- |
| `records[0]` | `[1, "help", "성공", 1]` | 1번 출동의 기록 전체 (한 행) |
| `records[1][2]` | `"실패"` | 2번 출동의 결과 칸 |
| `records[2][1]` | `"rescue"` | 3번 출동의 암호 |
| `len(records)` | `3` | 출동 횟수 = 행의 개수 |

> `records[행][칸]`은 '**몇 번째 출동의 몇 번째 칸**'으로 읽습니다. 행도 칸도 0부터 셉니다.

## 행 쌓기: append

```python
records = []                                         # 처음엔 빈 기록표
success, wrong = play(word)                          # 한 판 하고
records.append([len(records) + 1, word, "성공" if success else "실패", wrong])   # 한 행 추가
```

`len(records) + 1`은 '지금까지의 출동 수 + 1' = 이번 출동 번호입니다. `"성공" if success else "실패"`는 success가 True면 "성공", 아니면 "실패"가 되는 한 줄짜리 if입니다.

## 중첩 for: 행을 돌고, 그 안에서 칸을 돈다

```python
def text_width(text):
    """화면에서 차지하는 칸 수를 센다 (한글은 2칸, 영문·숫자·기호는 1칸)"""
    width = 0
    for ch in text:
        if "가" <= ch <= "힣":                  # 한글 글자는 화면에서 두 칸
            width += 2
        else:
            width += 1
    return width


def print_records(records):
    for row in [["출동", "암호", "결과", "틀린 횟수"]] + records:   # 바깥 for: 행
        cells = []
        for item in row:                                            # 안쪽 for: 칸
            text = str(item)
            cells.append(text + " " * (10 - text_width(text)))      # 화면에서 10칸이 되게 채우기
        print(" | ".join(cells).rstrip())                           # 한 행을 한 줄로 출력
```

- `[머리글 행] + records`는 머리글을 맨 위에 붙인 새 리스트입니다.
- 안쪽 for는 칸마다 빈칸을 채워 `cells`에 모으고, 한 행이 끝나면 `" | ".join(cells)`로 이어 한 줄에 출력합니다.
- 머리글 포함 4행 × 4칸 = 안쪽 for가 **16번** 반복됩니다.

> **왜 text_width()가 필요할까?** 화면에서 영문·숫자는 1칸, 한글은 **2칸**을 차지합니다. `f"{item:<8}"`처럼 **글자 수**로 빈칸을 채우면 "출동"(2글자, 화면 4칸)과 "1"(1글자, 화면 1칸)의 실제 폭이 달라져 세로줄이 한두 칸씩 어긋납니다. 그래서 글자 수가 아니라 **화면 칸 수**를 세어 빈칸을 채웁니다. (IDLE에서는 D2Coding처럼 한글이 영문의 두 배 폭인 고정폭 글꼴을 쓰면 정확히 맞습니다.)

## 행 고르기, 칸 모으기

```python
for row in records:              # 성공한 출동의 암호만
    if row[2] == "성공":
        print(row[1])

total = 0                        # 틀린 횟수 칸만 모아 합계
for row in records:
    total += row[3]
```

## 실행 예시

`lesson06_records.py`를 실행한 화면입니다. ①~⑧을 먼저 예측해 보고 실행해 확인하세요.

```text
① records[0]       → [1, 'help', '성공', 1]
② records[1][2]    → 실패
③ records[2][1]    → rescue
④ len(records)     → 3
⑤ 기록표
출동       | 암호       | 결과       | 틀린 횟수
1          | help       | 성공       | 1
2          | safe       | 실패       | 6
3          | rescue     | 성공       | 2
⑥ 성공한 암호: help rescue
⑦ 틀린 횟수 합계 9, 평균 3.0
⑧ 추가한 뒤 출동 횟수: 4 / 마지막 행: [4, 'hope', '성공', 0]
```

게임 `word_rescue.py`에서는 출동할 때마다 기록표가 한 행씩 늘어납니다(1차시 실행 예시 참고).

## 전체 코드

### lesson06_records.py

```python
"""영단어 구조대 - 출동 기록표(2차원 리스트) 연습                 [6차시]

게임을 3번 출동한 뒤의 기록표가 아래 records 라고 하자.
  한 행 = [출동 번호, 암호, 결과, 틀린 횟수]
  records[행][칸] → '몇 번째 출동의 몇 번째 칸'

① ~ ⑧ 의 출력을 먼저 예측해서 활동지에 적은 뒤 실행해 확인하세요.
실행 방법: python lesson06_records.py   (word_rescue.py 와 같은 폴더에서)
"""
from word_rescue import text_width     # 게임 코드의 함수를 가져와 다시 쓴다 (4차시)

records = [[1, "help", "성공", 1],
           [2, "safe", "실패", 6],
           [3, "rescue", "성공", 2]]

print("① records[0]       →", records[0])        # 한 행 = 1번 출동 기록 전체
print("② records[1][2]    →", records[1][2])     # 2번 출동의 결과
print("③ records[2][1]    →", records[2][1])     # 3번 출동의 암호
print("④ len(records)     →", len(records))      # 행의 개수 = 출동 횟수

# ⑤ 중첩 for: 바깥 for 는 행(출동), 안쪽 for 는 칸
#    한글은 화면에서 2칸이므로 text_width()로 화면 칸 수를 세어 빈칸을 채운다
print("⑤ 기록표")
for row in [["출동", "암호", "결과", "틀린 횟수"]] + records:
    cells = []
    for item in row:
        text = str(item)
        cells.append(text + " " * (10 - text_width(text)))
    print(" | ".join(cells).rstrip())

# ⑥ 행을 하나씩 보며 조건에 맞는 것만 고르기 (성공한 출동의 암호)
print("⑥ 성공한 암호:", end=" ")
for row in records:
    if row[2] == "성공":
        print(row[1], end=" ")
print()

# ⑦ 한 칸(열)만 모아 계산하기: 틀린 횟수 합계와 평균
total = 0
for row in records:
    total += row[3]
print(f"⑦ 틀린 횟수 합계 {total}, 평균 {total / len(records):.1f}")

# ⑧ 새 출동 기록을 한 행 추가하기
records.append([4, "hope", "성공", 0])
print("⑧ 추가한 뒤 출동 횟수:", len(records), "/ 마지막 행:", records[-1])
```

## 실습 활동

1. 연습 파일의 ①~⑧ 출력을 먼저 활동지에 예측하고 실행해 확인하세요. **[활동지]**
2. 게임을 3번 출동한 뒤 화면의 기록표를 종이에 옮겨 적고, 행·칸 번호를 붙여 보세요.
3. **실습 미션** (부록 04-7 산출물 예시 과제 B)
   - 미션 ① 출동을 3번으로 정해 자동으로 끝나게 하기
   - 미션 ② 기록표에서 성공한 출동만 골라 출력하기
   - 미션 ③ (도전) 성공률(%) 출력하기

활동지: [lesson06_records_2d_list.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson06_records_2d_list.md)

## 도전 과제 (기본 · 응용 · 심화)

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | 기록표 마지막에 `총 n번 출동`을 출력하기 (`len(records)`) |
| 응용 | main()을 `for i in range(3):`로 바꾸어 3번 출동 뒤 기록표를 **한 번만** 출력하기 (들여쓰기 위치 주의) |
| 심화 | 성공한 출동만 골라 출력하고 성공률을 계산하는 `print_success(records)` 함수 만들기. 기록표의 암호 칸(`row[1]`)을 단어장의 키로 넣어 뜻도 함께 출력해 보기 |

## 확인 퀴즈

**Q1.** `records = [[1, "help", "성공", 1], [2, "safe", "실패", 6]]`일 때 `records[1][2]`의 값은?

- ① `"help"`
- ② `"성공"`
- ③ `"실패"`
- ④ 6

**Q2.** 같은 records에서 `records[0]`이 뜻하는 것은?

- ① 1번 출동의 기록 전체(한 행)
- ② 모든 출동의 암호
- ③ 1번 출동의 결과
- ④ 행의 개수

**Q3.** 새 출동 기록 한 행을 추가하는 코드는?

- ① `records + [3, "hope", "성공", 0]`
- ② `records.append([3, "hope", "성공", 0])`
- ③ `records[3] = "hope"`
- ④ `records.add(3, "hope")`

**Q4.** 행이 3개, 한 행의 칸이 4개인 records를 중첩 for로 모두 출력하면 안쪽 for 문은 모두 몇 번 반복되는가?

- ① 3번
- ② 4번
- ③ 7번
- ④ 12번

**Q5.** records에서 성공한 출동의 암호만 출력하는 코드로 알맞은 것은?

- ① 행마다 row[1]을 모두 출력한다
- ② 행마다 row[2]가 "성공"인지 보고, 맞으면 row[1]을 출력한다
- ③ `records["성공"]을 출력한다`
- ④ `records[2]가 "성공"이면 records[1]을 출력한다`

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 기록표에서 출동 찾기 (기본)

첫째 줄에 n, 다음 n줄에 `출동번호 암호 결과 틀린횟수`가 주어집니다. 이를 2차원 리스트에 저장한 뒤, 마지막 줄에 출동 번호 k가 주어지면 `k번 출동: 암호 (결과, 틀린 횟수 t)`를 출력하세요.

- 입력: n, n줄의 기록, 찾을 출동 번호 k
- 출력: `k번 출동: 암호 (결과, 틀린 횟수 t)`

예제 입력 1

```text
3
1 help 성공 1
2 safe 실패 6
3 rescue 성공 2
2
```

예제 출력 1

```text
2번 출동: safe (실패, 틀린 횟수 6)
```

예제 입력 2

```text
1
1 hope 성공 0
1
```

예제 출력 2

```text
1번 출동: hope (성공, 틀린 횟수 0)
```

### 문제 2. 출동 기록 분석 (도전)

첫째 줄에 n, 다음 n줄에 `암호 결과 틀린횟수`가 주어집니다(결과는 `성공` 또는 `실패`). 결과별 횟수를 `성공: a번`, `실패: b번`으로 출력하고, 성공한 기록 중 틀린 횟수가 가장 많은 출동을 `가장 아슬아슬한 구조: 암호 (틀림 k)`로 출력하세요(같으면 먼저 나온 것). 성공 기록이 없으면 `성공 기록 없음`을 출력합니다.

- 입력: n, n줄의 기록
- 출력: 결과별 횟수, 가장 아슬아슬한 구조

예제 입력 1

```text
3
help 성공 2
hope 실패 6
rescue 성공 5
```

예제 출력 1

```text
성공: 2번
실패: 1번
가장 아슬아슬한 구조: rescue (틀림 5)
```

예제 입력 2

```text
1
safe 실패 6
```

예제 출력 2

```text
성공: 0번
실패: 1번
성공 기록 없음
```

정답과 해설은 **[부록] 04-1-06. 6차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-06-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 2차원 리스트 = 리스트를 담은 리스트, 한 행 = 한 번의 출동
- `records[행][칸]` → 몇 번째 출동의 몇 번째 칸 (둘 다 0부터)
- `records.append([...])`로 행을 쌓는다
- 중첩 for: 바깥은 행, 안쪽은 칸 → 반복 횟수 = 행 수 × 칸 수
- 한글은 화면에서 2칸 → 글자 수가 아니라 화면 칸 수(`text_width`)로 빈칸을 채워야 표가 맞는다
- 행을 돌며 조건으로 고르거나(성공만), 한 칸을 모아 계산한다(합계·평균)

## 수업 흐름 (50분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 5분 | 지난 시간 출구 티켓 확인, 핵심 질문: 여러 번의 결과를 어떻게 모을까? |
| 전개 1 | 12분 | 2차원 리스트 표 그리기, `records[행][칸]` 읽기 퀵 퀴즈 |
| 전개 2 | 10분 | 연습 파일 예측·실행 [활동지], 중첩 for 실행 횟수 세기 |
| 전개 3 | 15분 | 실습 미션 ①~③ (짝 프로그래밍) |
| 정리 | 8분 | 확인 퀴즈, 7차시 예고(이상한 입력 테스트) |

## 교사용 메모

- 학생이 가장 많이 헷갈리는 것은 칸 번호입니다. `records[0][3]`을 '결과'로 착각하는 경우가 많으니 표에 칸 번호를 크게 적어 두세요.
- 표의 세로줄이 어긋나는 문제는 '한글은 몇 칸일까?'라는 질문으로 시작하면 좋습니다. `len("출동")`(2)과 화면에서 차지하는 칸(4)이 다르다는 것을 직접 확인하게 하세요.
- 하 수준 학생은 기록표를 종이에 옮겨 적고 손가락으로 행과 칸을 짚으며 읽게 합니다(부록 04-7 예시 B-하).
- 미션 ①에서 `print_records(records)`를 반복 안에 두면 출동마다 표가 다시 출력됩니다. 틀린 것이 아니라 '들여쓰기 위치'를 생각해 보는 좋은 피드백 지점입니다(예시 B-중).
- 이 차시는 성취기준 [12정보03-06] 다차원 데이터 구조의 핵심 차시입니다. 수행평가 '다차원 데이터 구조의 적용(25점)'과 연결해 관찰합니다.

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `lesson06_records.py` | [lesson06_records.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/lesson06_records.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/lesson06_records.py) |
| 소스코드 `word_rescue.py` | [word_rescue.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/word_rescue.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/word_rescue.py) |
| 학습용 PPT | [lesson06_records_2d_list.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/lesson06_records_2d_list.pptx) |
| 학생 활동지 | [lesson06_records_2d_list.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/lesson06_records_2d_list.md) |
| 코딩 테스트 1 정답 코드 | [lesson06_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson06_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson06_test1.py) |
| 코딩 테스트 2 정답 코드 | [lesson06_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson06_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson06_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
