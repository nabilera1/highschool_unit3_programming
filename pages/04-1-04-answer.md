> 4차시 **while과 조건문으로 기본 버전 완성하기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `while True:` 반복을 끝내는 명령은?

- ① stop
- ② exit
- ③ break
- ④ end

> **정답: ③ break**  
> `break`를 만나면 가장 가까운 반복문을 즉시 빠져나갑니다.

**Q2.** 신호그림이 7개일 때 `len(신호그림) - 1`의 값은?

- ① 5
- ② 6
- ③ 7
- ④ 8

> **정답: ② 6**  
> 7 - 1 = 6. 6번 틀리면 신호가 끊깁니다.

**Q3.** 틀린단어가 `'zx'`일 때 출력되는 그림은?

- ① 신호그림[0]
- ② 신호그림[1]
- ③ 신호그림[2]
- ④ 신호그림[3]

> **정답: ③ 신호그림[2]**  
> `len('zx')`는 2이므로 `신호그림[2]`가 출력됩니다.

**Q4.** `비밀단어='safe'`, `맞춘단어='sfa'`일 때 깃발 변수 `모두맞춤`의 값은?

- ① True
- ② False
- ③ None
- ④ 오류

> **정답: ② False**  
> 'e'를 아직 못 맞혔으므로 깃발이 내려가 False입니다.

**Q5.** 횟수를 미리 알 수 없는 반복에 알맞은 것은?

- ① for i in range(3)
- ② while
- ③ if
- ④ print

> **정답: ② while**  
> 암호를 완성할 때까지처럼 조건으로 끝나는 반복에는 while이 알맞습니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ③ | ② | ③ | ② | ② |

## 코딩 테스트 1. 신호 배터리 그리기

```python
k = int(input())
남은칸 = 6 - k
print('[' + '■' * 남은칸 + '□' * k + ']')    # 문자열 반복과 이어 붙이기
print(f'남은 배터리: {남은칸}칸')
```

**해설** 그림 7개를 리스트에 모두 적는 대신 **문자열 반복**으로 그림을 만들 수도 있습니다. `'■' * 0`은 빈 문자열이라 k가 6일 때도 올바르게 출력됩니다.

정답 코드 파일: [new_ch04_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch04_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch04_test1.py)

## 코딩 테스트 2. 구조 출동 시뮬레이션

```python
비밀단어 = input()
입력들 = input()
맞춘단어, 틀린단어 = '', ''
결과 = '암호 미완성'
i = 0
while i < len(입력들):              # 글자가 남아 있는 동안
    guess = 입력들[i]
    i += 1
    if guess in 비밀단어:
        맞춘단어 += guess
        모두맞춤 = True
        for 글자 in 비밀단어:
            if 글자 not in 맞춘단어:
                모두맞춤 = False
        if 모두맞춤:
            결과 = f'구조 성공! 틀린 횟수 {len(틀린단어)}'
            break
    else:
        틀린단어 += guess
        if len(틀린단어) == 6:
            결과 = '신호 끊김'
            break
print(결과)
```

**해설** 기본 버전의 판정 부분을 그대로 쓰고, 입력만 키보드 대신 미리 주어진 문자열에서 꺼냅니다. 이렇게 입력을 고정하면 게임을 **자동으로 테스트**할 수 있습니다. 결과 변수를 '암호 미완성'으로 초기화해 두는 것이 세 번째 경우를 처리하는 열쇠입니다.

정답 코드 파일: [new_ch04_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch04_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch04_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
