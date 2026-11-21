"""7차시 코딩 테스트 2. 이미 말한 글자 걸러 내기 (도전)

첫째 줄에 n, 다음 n줄에 입력이 주어집니다. 기본 문제의 검사에 더해, 이미 통과한 글자가 다시 들어오면 이미 말한 글자를 출력하세요. 마지막 줄에는 통과한 글자를 리스트로 guessed: [...] 형식으로 출력합니다.

실행: python lesson07_test2.py  (예제 입력을 한 줄씩 넣어 확인)
"""
guessed = []
n = int(input())
for i in range(n):
    g = input().strip().lower()
    if len(g) != 1:
        print("한 글자만")
    elif g not in "abcdefghijklmnopqrstuvwxyz":
        print("알파벳만")
    elif g in guessed:
        print("이미 말한 글자")
    else:
        guessed.append(g)
        print("OK", g)
print("guessed:", guessed)
