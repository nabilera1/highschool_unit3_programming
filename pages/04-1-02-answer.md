> 2차시 **리스트·random·문자열로 암호 고르기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `words = ['help', 'safe', 'hope']`일 때 `words[1]`의 값은?

- ① help
- ② safe
- ③ hope
- ④ 오류

> **정답: ② safe**  
> 인덱스는 0부터 시작하므로 1번은 두 번째 항목 'safe'입니다.

**Q2.** `len('rescue')`의 값은?

- ① 5
- ② 6
- ③ 7
- ④ 'rescue'

> **정답: ② 6**  
> r-e-s-c-u-e 6글자입니다.

**Q3.** `'e' in 'help'`의 결과는?

- ① True
- ② False
- ③ 1
- ④ 오류

> **정답: ① True**  
> 'help' 안에 'e'가 있으므로 True입니다.

**Q4.** 리스트에서 항목 하나를 무작위로 고르는 함수는?

- ① random.pick()
- ② random.choice()
- ③ random.list()
- ④ choice.random()

> **정답: ② random.choice()**  
> `random.choice(리스트)`를 사용합니다. 먼저 `import random`이 필요합니다.

**Q5.** `words = ['a', 'b', 'c']`일 때 오류가 나는 것은?

- ① words[0]
- ② words[2]
- ③ words[-1]
- ④ words[3]

> **정답: ④ words[3]**  
> 항목이 3개면 인덱스는 0~2입니다. 3은 범위를 벗어나 IndexError가 납니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ① | ② | ④ |

## 코딩 테스트 1. 번호로 암호 꺼내기

```python
words = input().split()      # 'help rescue' → ['help', 'rescue']
k = int(input())
word = words[k - 1]          # 사람의 번호(1부터) → 인덱스(0부터)
print(word, len(word))
```

**해설** `split()`은 공백을 기준으로 문자열을 나눠 리스트를 만듭니다. 사람이 쓰는 번호는 1부터, 인덱스는 0부터이므로 `k - 1`이 필요합니다.

정답 코드 파일: [new_ch02_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch02_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch02_test1.py)

## 코딩 테스트 2. 가장 긴 암호, 가장 짧은 암호

```python
words = input().split()
longest = words[0]           # 첫 단어를 일단 '최고'로 정해 두고
shortest = words[0]
for w in words:              # 나머지와 하나씩 비교
    if len(w) > len(longest):     # 더 길 때만 바꾼다 (같으면 먼저 나온 것 유지)
        longest = w
    if len(w) < len(shortest):
        shortest = w
print(f'가장 긴 암호: {longest} ({len(longest)}글자)')
print(f'가장 짧은 암호: {shortest} ({len(shortest)}글자)')
```

**해설** 첫 항목을 기준값으로 두고 하나씩 비교하며 갱신하는 **최댓값·최솟값 찾기** 알고리즘입니다. `>=`가 아니라 `>`를 써야 길이가 같을 때 먼저 나온 단어가 남습니다.

정답 코드 파일: [new_ch02_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch02_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch02_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
