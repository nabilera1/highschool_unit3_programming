"""7차시 코딩 테스트 1. 입력 다듬고 검사하기 (기본)

첫째 줄에 n, 다음 n줄에 사용자가 입력한 문자열이 주어집니다. 각 줄을 strip()과 lower()로 다듬은 뒤, 한 글자가 아니면 한 글자만, a~z가 아니면 알파벳만, 올바르면 OK 글자를 출력하세요.

실행: python lesson07_test1.py  (예제 입력을 한 줄씩 넣어 확인)
"""
n = int(input())
for i in range(n):
    g = input().strip().lower()
    if len(g) != 1:
        print("한 글자만")
    elif g not in "abcdefghijklmnopqrstuvwxyz":
        print("알파벳만")
    else:
        print("OK", g)
