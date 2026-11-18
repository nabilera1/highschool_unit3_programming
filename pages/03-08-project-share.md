> **3부 자료구조로 확장하고 프로젝트하기** · 8차시 · 수업 단계: **공유·확장**  
> 핵심 개념: 프로젝트, 기능 설계, 글자 빈도, 확률, 발표, 피드백

## 학습 목표

1. 모둠 주제에 맞게 영단어 구조대를 확장하는 기능을 설계하고 구현할 수 있다.
2. 데이터(글자 빈도)를 분석해 게임 전략을 세울 수 있다.
3. 산출물을 시연·발표하고 동료의 작품에 구체적인 피드백을 줄 수 있다.

## 핵심 질문

> **우리 모둠의 영단어 구조대는 누구를, 무엇으로 도울 수 있을까?**

지금까지 만든 영단어 구조대를 바탕으로 **우리 모둠만의 구조대**를 만듭니다. 단어장 주제를 바꾸면 과학 용어, 진로 단어, 환경 단어를 익히는 학습 게임이 됩니다.

또, '처음에 어떤 글자를 말해야 유리할까?'라는 질문에 **데이터로 답하는** 심화 활동도 해 봅니다.

## 프로젝트 진행 순서

| 단계 | 시간 | 할 일 | 산출물 |
| --- | --- | --- | --- |
| 기획 | 10분 | 주제·대상·추가 기능 2개 정하기 | 기획표 (활동지) |
| 구현 | 20분 | `new_rescue_project_template.py`를 고쳐 기능 구현 | 코드 파일 |
| 테스트 | 5분 | 정상·경계·예외 입력으로 확인 | 테스트 표 |
| 발표 | 10분 | 모둠별 1분 시연 + 핵심 코드 설명 | 발표, 동료 피드백 |

출발 코드에는 `[TODO 1]`~`[TODO 4]` 표시가 있어 어디를 고치면 되는지 안내합니다.

## 확장 기능 메뉴 (기본 · 응용 · 심화)

| 수준 | 기능 | 필요한 개념 | 참고 |
| --- | --- | --- | --- |
| 기본 | 주제 단어장으로 바꾸기 | 리스트 | 2차시 |
| 기본 | 성공·실패 메시지 꾸미기 | 문자열 | 1차시 |
| 응용 | 뜻 힌트 보여 주기 | 딕셔너리 | 7차시 |
| 응용 | 구조대 위치 `[===>   ]` 표시 | 함수, 비율 | 6차시 코딩 테스트 |
| 심화 | 출동 기록표 | 2차원 리스트 | 7차시 |
| 심화 | 힌트 아이템 (배터리 1칸과 바꿔 한 글자 공개) | 함수, 조건문 | 직접 설계 |

## 심화: 어떤 글자부터 말할까? (글자 빈도 분석)

단어 24개에서 각 알파벳이 **들어 있는 단어 수**를 세면, 처음에 그 글자를 말했을 때 맞힐 확률을 알 수 있습니다.

```python
빈도 = {}                          # 글자 → 그 글자가 들어 있는 단어 수
for 단어 in words:                 # 바깥 반복: 단어
    for 글자 in set(단어):         # 안쪽 반복: 서로 다른 글자 (중복 제거)
        빈도[글자] = 빈도.get(글자, 0) + 1
```

| 글자 | 들어 있는 단어 수 | 처음에 말하면 맞힐 확률 |
| --- | --- | --- |
| e | 14 | 58.3% |
| r, t | 11 | 45.8% |
| i, o | 10 | 41.7% |
| z, q, x, j | 0 | 0.0% |

**결론:** 우리 단어장에서는 `e`를 먼저 말하는 것이 가장 유리합니다. 단어장이 바뀌면 결과도 바뀝니다. 이처럼 **데이터를 분석해 전략을 세우는 것**도 컴퓨팅 사고입니다.

## 발표와 동료 피드백

발표는 모둠별 1분입니다.

1. **누구를** 돕는 게임인가? (주제와 대상)
2. 추가한 기능 시연
3. 핵심 코드 한 부분 설명 (어떤 자료구조·함수를 썼는지)
4. 해결한 오류 하나

동료 피드백은 **칭찬 1 + 제안 1** 형식으로 씁니다. 예: "뜻 힌트 덕분에 단어를 외우기 쉬웠어요. / 이미 말한 글자를 화면에 보여 주면 더 좋겠어요." 

## 전체 코드

이번 차시의 **전체 프로그램**입니다. 주석(`#` 뒤의 설명)을 함께 읽으며 따라가 보세요.

1. 코드 블록 전체를 복사합니다. (코드 블록 오른쪽 위 복사 버튼 또는 드래그 후 Ctrl + C)
2. IDLE에서 **File → New File**을 열고 붙여 넣습니다. (Ctrl + V)
3. 아래 파일 이름으로 저장한 뒤 **F5**로 실행합니다. (VS Code는 ▶ 실행 버튼)

### new_rescue_4_letter_freq.py

```python
# =====================================================================
# 영단어 구조대 심화 - 글자 빈도로 '먼저 고를 글자' 찾기    [8차시 심화]
#
# 질문: 처음에 어떤 알파벳을 말하면 맞힐 가능성이 가장 높을까?
# 방법: 단어 목록에서 각 알파벳이 '들어 있는 단어'가 몇 개인지 센다.
#       (한 단어에 같은 글자가 여러 번 나와도 1번만 센다 → set(단어) 사용)
#       확률(%) = 그 글자가 들어 있는 단어 수 / 전체 단어 수 × 100
#
# 배우는 것: 딕셔너리로 개수 세기(get), 중첩 반복, 정렬, 확률, 데이터 기반 전략
# 실행 방법: python new_rescue_4_letter_freq.py
# =====================================================================

# new_rescue_3_project.py 의 단어사전에 있는 24개 단어
words = ['help', 'safe', 'rescue', 'doctor', 'nurse', 'hospital', 'emergency', 'firefighter',
         'hope', 'care', 'smile', 'thanks', 'friend', 'kindness', 'together', 'courage',
         'list', 'loop', 'input', 'python', 'output', 'variable', 'function', 'algorithm']

빈도 = {}                                   # 딕셔너리: 글자 → 그 글자가 들어 있는 단어 수
for 단어 in words:                          # 바깥 반복: 단어 하나씩
    for 글자 in set(단어):                  # 안쪽 반복: 그 단어의 '서로 다른' 글자 하나씩
        # 빈도.get(글자, 0): 처음 나온 글자면 0, 이미 있으면 지금까지 센 값
        빈도[글자] = 빈도.get(글자, 0) + 1

# (글자, 개수) 쌍들을 개수가 큰 순서로 정렬
#   key=lambda 쌍: 쌍[1]  → 각 쌍의 1번 칸(개수)을 기준으로 정렬하라는 뜻
#   개수가 같을 때는 원래 순서를 유지하므로, 먼저 알파벳순으로 정렬해 둔다
순위 = sorted(sorted(빈도.items()), key=lambda 쌍: 쌍[1], reverse=True)

print(f'단어 {len(words)}개 기준, 처음에 고르면 맞힐 확률 (상위 10개)')
for 글자, 개수 in 순위[:10]:                # [:10] → 앞에서 10개만
    print(f'{글자}: {개수}개 단어  ({개수 / len(words) * 100:.1f}%)  ' + '■' * 개수)

print('\n잘 나오지 않는 글자')
for 글자 in 'zqxj':
    print(f'{글자}: {빈도.get(글자, 0)}개 단어  ({빈도.get(글자, 0) / len(words) * 100:.1f}%)')
```

파일 받기: [new_rescue_4_letter_freq.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_4_letter_freq.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_4_letter_freq.py)

## 실습 활동

1. 모둠별로 주제·대상·추가 기능 2개를 정해 기획표를 작성하세요.
2. `new_rescue_project_template.py`를 내려받아 `[TODO]` 위치에 기능을 구현하세요.
3. `new_rescue_4_letter_freq.py`의 `words`를 우리 모둠 단어장으로 바꿔 '먼저 말할 글자'를 찾아보세요.
4. 1분 발표 후 다른 모둠 작품에 칭찬 1 + 제안 1 피드백을 남기세요.

활동지: [new_ws08-project-share.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws08-project-share.md)

## 도전 과제 (기본 · 응용 · 심화)

자신의 속도에 맞게 골라 도전하세요. 기본을 마치면 응용, 응용을 마치면 심화로!

| 수준 | 도전 과제 |
| --- | --- |
| 기본 | 주제 단어장 바꾸기 + 메시지 꾸미기 |
| 응용 | 뜻 힌트 + 구조대 위치 표시 |
| 심화 | 출동 기록표 + 힌트 아이템, 또는 글자 빈도로 '추천 글자' 기능 만들기 |

## 확인 퀴즈

**Q1.** `빈도.get('z', 0)`에서 'z'가 딕셔너리에 없으면 결과는?

- ① None
- ② 0
- ③ KeyError
- ④ 'z'

**Q2.** `set('together')`를 쓰는 이유로 알맞은 것은?

- ① 글자를 정렬하려고
- ② 같은 글자를 한 번만 세려고
- ③ 대문자로 바꾸려고
- ④ 글자 수를 세려고

**Q3.** 단어 24개 중 14개에 e가 있다. 처음에 e를 말하면 맞힐 확률은? (소수 첫째 자리)

- ① 14.0%
- ② 41.7%
- ③ 58.3%
- ④ 71.4%

**Q4.** '칭찬 1 + 제안 1' 피드백으로 가장 알맞은 것은?

- ① 별로예요
- ② 좋아요!
- ③ 뜻 힌트가 좋았어요. 틀린 글자도 보여 주면 좋겠어요.
- ④ 제 것이 더 좋아요

**Q5.** 프로젝트 출발 코드에서 `[TODO]` 표시의 역할은?

- ① 오류가 난 곳
- ② 고치거나 기능을 추가할 위치 안내
- ③ 실행하지 않는 코드
- ④ 정답 코드

## 코딩 테스트

각 문제의 입력 형식을 지켜 `input()`으로 읽고, 출력 형식과 **똑같이** 출력하세요.

### 문제 1. 한 단어의 글자 세기 (기본)

영단어 하나가 주어질 때, 딕셔너리로 각 글자가 몇 번 나오는지 세어 알파벳 순서로 `글자 개수`를 한 줄씩 출력하세요.

- 입력: 영단어 하나
- 출력: 알파벳 순서로 `글자 개수`

예제 입력 1

```text
together
```

예제 출력 1

```text
e 2
g 1
h 1
o 1
r 1
t 2
```

예제 입력 2

```text
help
```

예제 출력 2

```text
e 1
h 1
l 1
p 1
```

### 문제 2. 첫 글자 추천 (도전)

첫째 줄에 영단어들이 공백으로 구분되어 주어집니다. 가장 많은 단어에 들어 있는 글자를 찾아 `글자 n개 단어 (p%)` 형식으로 출력하세요. 한 단어 안에서 같은 글자는 한 번만 세고, p는 소수 첫째 자리까지, 개수가 같으면 알파벳 순서가 빠른 글자를 고릅니다.

- 입력: 영단어들 (공백 구분)
- 출력: `글자 n개 단어 (p%)`

예제 입력 1

```text
help hope list loop
```

예제 출력 1

```text
l 3개 단어 (75.0%)
```

예제 입력 2

```text
doctor nurse
```

예제 출력 2

```text
r 2개 단어 (100.0%)
```

정답과 해설은 **[부록] 04-1-08. 8차시 정답과 해설** 페이지([GitHub에서 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/pages/04-1-08-answer.md))에 있습니다. 먼저 스스로 풀어 본 뒤 확인하세요.

## 정리

- 모둠 주제로 단어장을 바꾸면 새로운 학습 게임이 된다
- 기본 · 응용 · 심화 기능 중 골라 확장한다
- 글자 빈도 = 딕셔너리 + 중첩 반복 → 데이터로 전략 세우기
- 발표는 시연 + 핵심 코드, 피드백은 칭찬 1 + 제안 1

## 수업 흐름 (45분 기준, 교사용)

| 단계 | 시간 | 활동 |
| --- | --- | --- |
| 도입 | 5분 | 산출물 예시 시연, 프로젝트 안내 |
| 전개 1 | 20분 | 기획표 작성, 출발 코드로 기능 구현 |
| 전개 2 | 10분 | 테스트, (심화) 글자 빈도 분석 |
| 정리 | 10분 | 1분 발표, 동료 피드백, 자기 평가 |

## 교사용 메모

- 시간이 부족하면 발표를 다음 시간 앞 15분으로 옮기거나, 갤러리 워크(자리 이동하며 다른 모둠 작품 체험) 방식으로 바꿀 수 있습니다.
- 프로젝트 평가는 부록의 **프로젝트 평가 루브릭**을 사용합니다. 산출물만이 아니라 기획표·테스트 기록·피드백도 평가 근거가 됩니다.
- AI를 활용한 모둠은 활동지의 'AI 활용 기록'을 반드시 작성하게 하고, 발표 때 '이 코드가 무슨 일을 하는지' 직접 설명하게 합니다.

## 자료 내려받기

| 자료 | 링크 |
| --- | --- |
| 소스코드 `new_rescue_project_template.py` | [new_rescue_project_template.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_project_template.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_project_template.py) |
| 소스코드 `new_rescue_4_letter_freq.py` | [new_rescue_4_letter_freq.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_4_letter_freq.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_4_letter_freq.py) |
| 소스코드 `new_rescue_3_project.py` | [new_rescue_3_project.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/new_rescue_3_project.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/new_rescue_3_project.py) |
| 학습용 PPT | [new_08-project-share.pptx 내려받기](https://github.com/nabilera1/highschool_unit3_programming/raw/main/slides/new_08-project-share.pptx) |
| 학생 활동지 | [new_ws08-project-share.md](https://github.com/nabilera1/highschool_unit3_programming/blob/main/worksheets/new_ws08-project-share.md) |
| 코딩 테스트 1 정답 코드 | [new_ch08_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch08_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch08_test1.py) |
| 코딩 테스트 2 정답 코드 | [new_ch08_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch08_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch08_test2.py) |
| 전체 자료 한 번에 | [ZIP 내려받기](https://github.com/nabilera1/highschool_unit3_programming/archive/refs/heads/main.zip) |
