"""3차시 코딩 테스트 1. 밑줄 암호판 출력 (기본)

첫째 줄에 암호, 둘째 줄에 지금까지 말한 글자들이 공백 없이 주어집니다. 말한 글자는 그대로, 나머지는 _로 바꾸어 한 칸씩 띄어 출력하세요.

실행: python lesson03_test1.py  (예제 입력을 한 줄씩 넣어 확인)
"""
word = input()
guessed = list(input())          # "hp" → ["h", "p"]
board = []
for ch in word:
    if ch in guessed:
        board.append(ch)
    else:
        board.append("_")
print(" ".join(board))
