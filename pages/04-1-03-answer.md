> 3차시 **for 반복문으로 밑줄 암호판 만들기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `for ch in 'safe':`는 몇 번 반복하는가?

- ① 3번
- ② 4번
- ③ 5번
- ④ 무한 반복

> **정답: ② 4번**  
> 문자열의 글자 수만큼 반복합니다. 'safe'는 4글자입니다.

**Q2.** `print('a', end=' ')`의 `end=' '`의 역할은?

- ① 줄을 바꾼다
- ② 줄을 바꾸지 않고 공백을 붙인다
- ③ 출력을 지운다
- ④ 오류가 난다

> **정답: ② 줄을 바꾸지 않고 공백을 붙인다**  
> print는 원래 끝에 줄바꿈을 붙이는데, end로 그 대신 붙일 문자열을 정할 수 있습니다.

**Q3.** `비밀단어='hope'`, `맞춘단어='oe'`일 때 암호판은?

- ① h o p e
- ② _ o _ e
- ③ o _ e _
- ④ _ _ _ _

> **정답: ② _ o _ e**  
> h(✗) o(✓) p(✗) e(✓) → `_ o _ e`입니다.

**Q4.** `s = ''` 다음에 `s = s + 'h'`, `s = s + 'p'`를 실행하면 s는?

- ① 'h'
- ② 'p'
- ③ 'hp'
- ④ 'ph'

> **정답: ③ 'hp'**  
> 뒤에 차례로 이어 붙이므로 'hp'가 됩니다.

**Q5.** `for i in range(3):`에서 i가 갖는 값은?

- ① 1, 2, 3
- ② 0, 1, 2
- ③ 0, 1, 2, 3
- ④ 3

> **정답: ② 0, 1, 2**  
> range(3)은 0부터 3 직전까지, 즉 0, 1, 2입니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ③ | ② |

## 코딩 테스트 1. 밑줄 암호판 출력

```python
비밀단어 = input()
맞춘단어 = input()
for 글자 in 비밀단어:
    if 글자 in 맞춘단어:
        print(글자, end=' ')
    else:
        print('_', end=' ')
print()
```

**해설** 게임 코드의 암호판 부분과 같습니다. `together`처럼 같은 글자가 여러 번 나와도 글자마다 따로 검사하므로 모든 자리에 공개됩니다.

정답 코드 파일: [new_ch03_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch03_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch03_test1.py)

## 코딩 테스트 2. 공개된 칸, 남은 칸

```python
비밀단어 = input()
맞춘단어 = input()
공개 = 0
for 글자 in 비밀단어:
    if 글자 in 맞춘단어:
        공개 += 1
print(f'공개 {공개}칸 / 남은 {len(비밀단어) - 공개}칸')
```

**해설** 암호판을 출력하는 대신 조건이 참인 칸을 **세는** 문제입니다. 남은 칸은 전체 글자 수에서 빼면 됩니다. 이 값은 7차시의 '구조대 위치' 계산에 그대로 쓰입니다.

정답 코드 파일: [new_ch03_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/new_ch03_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/new_ch03_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
