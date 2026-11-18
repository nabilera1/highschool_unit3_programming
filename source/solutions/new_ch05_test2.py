"""5차시 코딩 테스트 2: 이미 입력한 글자 걸러 내기 (도전) - 정답 예시 코드

첫째 줄에 n, 다음 n줄에 입력이 주어집니다. 기본 문제의 검사에 더해, 이미 통과한 글자가 다시 들어오면 `이미 입력`을 출력하세요. 마지막 줄에는 통과한 글자를 순서대로 이어 `사용한 글자: ...` 형식으로 출력합니다.
"""

알파벳 = 'abcdefghijklmnopqrstuvwxyz'
사용한글자 = ''
n = int(input())
for _ in range(n):
    guess = input().strip().lower()
    if len(guess) != 1:
        print('한 글자만')
    elif guess not in 알파벳:
        print('알파벳만')
    elif guess in 사용한글자:
        print('이미 입력')
    else:
        사용한글자 += guess
        print('OK', guess)
print('사용한 글자:', 사용한글자)
