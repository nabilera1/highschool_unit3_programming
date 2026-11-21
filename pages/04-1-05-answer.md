> 5차시 **while 문으로 영단어 구조대 게임 완성하기**의 퀴즈와 코딩 테스트 정답·해설입니다. 교사용 채점 자료로도 사용할 수 있습니다.

## 확인 퀴즈 정답

**Q1.** `while battery > 0:`의 뜻으로 알맞은 것은?

- ① 배터리가 0이 될 때까지 한 번만 실행
- ② 배터리가 남아 있는 동안 반복
- ③ 배터리가 0이면 반복
- ④ 배터리를 0으로 만든다

> **정답: ② 배터리가 남아 있는 동안 반복**  
> while 문은 조건이 참인 동안 반복합니다. 조건이 거짓(battery가 0)이 되면 반복을 마칩니다.

**Q2.** play() 안에서 `"_" not in board`가 참이 되는 때는?

- ① 배터리가 0칸일 때
- ② 암호의 글자를 모두 맞혔을 때
- ③ 처음 시작할 때
- ④ 틀린 글자를 말했을 때

> **정답: ② 암호의 글자를 모두 맞혔을 때**  
> 암호판에 가린 칸 `_`가 하나도 없으면 모든 글자를 맞힌 것입니다.

**Q3.** `return True, MAX_BATTERY - battery`에 대한 설명으로 옳은 것은?

- ① 반복만 끝나고 함수는 계속된다
- ② 값 두 개를 한 번에 돌려주고 함수가 끝난다
- ③ `True만 돌려준다`
- ④ 반복문 안에서는 쓸 수 없다

> **정답: ② 값 두 개를 한 번에 돌려주고 함수가 끝난다**  
> 쉼표로 여러 값을 돌려줄 수 있고, 받는 쪽에서 `success, wrong = play(word)`처럼 나누어 받습니다.

**Q4.** play()에서 `battery -= 1`을 지우고 틀린 글자만 계속 입력하면?

- ① 바로 구조 성공
- ② 반복이 끝나지 않는다
- ③ 오류가 나며 멈춘다
- ④ 배터리가 2칸씩 준다

> **정답: ② 반복이 끝나지 않는다**  
> while 조건에 쓰인 `battery`가 바뀌지 않으므로 조건이 계속 참입니다. Ctrl+C로 멈춥니다.

**Q5.** 구조대 게임의 글자 입력 반복에 for보다 while이 알맞은 까닭은?

- ① `while이 더 빠르다`
- ② 몇 번 입력할지 미리 알 수 없다
- ③ `for 문은 문자열에 쓸 수 없다`
- ④ `while은 들여쓰기가 필요 없다`

> **정답: ② 몇 번 입력할지 미리 알 수 없다**  
> for는 횟수가 정해진 반복, while은 조건으로 끝나는 반복에 알맞습니다.

| 문항 | Q1 | Q2 | Q3 | Q4 | Q5 |
| --- | --- | --- | --- | --- | --- |
| 정답 | ② | ② | ② | ② | ② |

## 코딩 테스트 1. 배터리가 다 닳을 때까지

```python
battery = int(input())
while battery > 0:
    print("■" * battery, f"({battery}칸)")
    battery -= 1                # 조건에 쓰인 변수를 바꾼다
print("신호 끊김")
```

**해설** `battery -= 1`이 없으면 끝나지 않는 반복이 됩니다. 반복이 끝난 뒤의 `print`는 들여쓰기를 하지 않아 한 번만 실행됩니다.

정답 코드 파일: [lesson05_test1.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson05_test1.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson05_test1.py)

## 코딩 테스트 2. 구조 출동 시뮬레이션

```python
MAX_BATTERY = 6

def play(word, letters):
    guessed = []
    battery = MAX_BATTERY
    i = 0
    while battery > 0:
        done = True
        for ch in word:
            if ch not in guessed:
                done = False
        if done:
            return f"구조 성공! 틀린 횟수 {MAX_BATTERY - battery}"
        if i == len(letters):               # 입력할 글자를 다 썼다
            return "암호 미완성"
        g = letters[i]
        i += 1
        guessed.append(g)
        if g not in word:
            battery -= 1
    return "신호 끊김"

print(play(input(), input()))
```

**해설** 게임의 `play()`와 같은 구조에서 `input()` 대신 주어진 글자를 차례로 씁니다. 끝나는 경우가 세 가지이므로 각각 `return`으로 결과 문장을 돌려줍니다.

정답 코드 파일: [lesson05_test2.py 보기](https://github.com/nabilera1/highschool_unit3_programming/blob/main/source/solutions/lesson05_test2.py) · [내려받기(Raw)](https://raw.githubusercontent.com/nabilera1/highschool_unit3_programming/main/source/solutions/lesson05_test2.py)

## 채점 포인트

- 예제 입력에 대해 출력이 **글자 하나까지** 같은가? (공백·줄바꿈 포함)
- 예제 외의 경계값·예외 입력에도 올바른가? (교사가 추가 입력으로 확인)
- 변수 이름과 주석으로 풀이 과정을 설명할 수 있는가? (구술 확인)
- 정답 코드는 하나의 예시입니다. 출력이 같고 경계·예외 입력에도 올바르면 다른 풀이도 정답입니다.
