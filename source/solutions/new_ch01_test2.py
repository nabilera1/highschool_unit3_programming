"""1차시 코딩 테스트 2: 이 글자는 몇 번? (도전) - 정답 예시 코드

첫째 줄에 암호, 둘째 줄에 알파벳 한 글자를 입력받아 그 글자가 암호에 몇 번 있는지 출력하세요. 있으면 `n번 있어요`, 없으면 `없어요`를 출력합니다. (반복문으로 직접 세어 보세요.)
"""

word = input()
letter = input()
count = 0
for ch in word:          # 암호의 글자를 하나씩 보면서
    if ch == letter:     # 찾는 글자와 같으면
        count += 1       # 1 증가
if count > 0:
    print(f'{count}번 있어요')
else:
    print('없어요')
