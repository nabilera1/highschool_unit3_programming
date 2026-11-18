> 7차시 **딕셔너리와 2차원 리스트로 게임 확장하기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `d = {'help': '도움', 'hope': '희망'}`일 때 `d['hope']`의 값은?

- ① help
- ② 희망
- ③ 도움
- ④ 오류

> **정답: ② 희망**  
> 키 'hope'에 짝지어진 값 '희망'이 나옵니다.

**Q2.** 딕셔너리에 없는 키 `d['safe']`를 꺼내면?

- ① None
- ② 빈 문자열
- ③ KeyError 오류
- ④ False

> **정답: ③ KeyError 오류**  
> 없는 키를 꺼내면 KeyError가 납니다. `'safe' in d`로 먼저 확인할 수 있습니다.

**Q3.** `난이도표[0][2]`의 값은? (본문의 난이도표 기준)

- ① 쉬움
- ② 3
- ③ 5
- ④ True

> **정답: ③ 5**  
> 0행 ['쉬움', 3, 5, True]의 2열이므로 5입니다.

**Q4.** 딕셔너리를 `for 단어 in 뜻사전:`으로 반복하면 단어에 들어가는 것은?

- ① 값
- ② 키
- ③ (키, 값)
- ④ 인덱스

> **정답: ② 키**  
> 딕셔너리를 for로 돌리면 키가 하나씩 나옵니다.

**Q5.** 키보드판(3줄)을 중첩 for로 출력할 때 바깥 반복은 몇 번 도는가?

- ① 3번
- ② 9번
- ③ 10번
- ④ 26번

> **정답: ① 3번**  
> 바깥 반복은 행(줄)마다 한 번, 키보드판은 3줄입니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ③ | ③ | ② | ① |

## 코딩 테스트 1. 뜻 힌트 사전

```python
뜻사전 = {}
n = int(input())
for _ in range(n):
    단어, 뜻 = input().split()      # 'help 도움' → 'help', '도움'
    뜻사전[단어] = 뜻
m = int(input())
for _ in range(m):
    단어 = input()
    if 단어 in 뜻사전:              # 키가 있는지 먼저 확인
        print(뜻사전[단어])
    else:
        print('단어장에 없어요')
```

**해설** 빈 딕셔너리에 `뜻사전[키] = 값`으로 짝을 하나씩 추가합니다. 꺼내기 전에 `in`으로 확인하면 KeyError를 막을 수 있습니다.

정답 코드 파일: [new_ch07_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch07_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch07_test1.py)

## 코딩 테스트 2. 출동 기록 분석

```python
기록표 = []                          # 2차원 리스트
점수 = {'구조': 0, '재출동': 0}       # 딕셔너리
n = int(input())
for _ in range(n):
    단어, 결과, 틀림 = input().split()
    기록표.append([단어, 결과, int(틀림)])
    점수[결과] += 1

print(f'구조: {점수["구조"]}명')
print(f'재출동: {점수["재출동"]}번')

아슬 = None                          # 아직 못 찾음
for 행 in 기록표:
    if 행[1] == '구조':
        if 아슬 is None or 행[2] > 아슬[2]:
            아슬 = 행
if 아슬 is None:
    print('구조 기록 없음')
else:
    print(f'가장 아슬아슬한 구조: {아슬[0]} (틀림 {아슬[2]})')
```

**해설** 기록을 2차원 리스트에 쌓고, 결과 이름을 키로 하는 딕셔너리로 횟수를 셉니다. 최댓값을 찾을 때 '아직 없음'을 `None`으로 두면 구조 기록이 하나도 없는 경우도 처리할 수 있습니다.

정답 코드 파일: [new_ch07_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch07_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch07_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
