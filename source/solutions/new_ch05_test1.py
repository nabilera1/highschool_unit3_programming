"""5차시 코딩 테스트 1: 입력 다듬고 검사하기 (기본) - 정답 예시 코드

첫째 줄에 n, 다음 n줄에 사용자가 입력한 문자열이 주어집니다. 각 줄을 `strip()`과 `lower()`로 다듬은 뒤, 한 글자가 아니면 `한 글자만`, a~z가 아니면 `알파벳만`, 올바르면 `OK 글자`를 출력하세요.
"""

알파벳 = 'abcdefghijklmnopqrstuvwxyz'
n = int(input())
for _ in range(n):
    guess = input().strip().lower()
    if len(guess) != 1:
        print('한 글자만')
    elif guess not in 알파벳:
        print('알파벳만')
    else:
        print('OK', guess)
