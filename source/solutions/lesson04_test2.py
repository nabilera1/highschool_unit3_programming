"""4차시 코딩 테스트 2. 구조대 위치 함수 (도전)

맞힌 칸의 비율만큼 구조대가 친구에게 다가가는 그림을 돌려주는 함수 rescue_bar(word, guessed)를 만드세요. 공개된 칸 수를 a라 할 때 막대 칸 수는 a * 10 // len(word)이고, 구조대 [ + = × 칸 + > + 공백 × (10 - 칸) + ] 친구 모양입니다. 입력 형식은 문제 1과 같습니다.

실행: python lesson04_test2.py  (예제 입력을 한 줄씩 넣어 확인)
"""
def rescue_bar(word, guessed):
    opened = 0
    for ch in word:
        if ch in guessed:
            opened += 1
    n = opened * 10 // len(word)          # 0 ~ 10칸
    return "구조대 [" + "=" * n + ">" + " " * (10 - n) + "] 친구"

word = input()
k = int(input())
for i in range(k):
    print(rescue_bar(word, list(input())))
