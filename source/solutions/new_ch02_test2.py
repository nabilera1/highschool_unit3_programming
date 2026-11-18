"""2차시 코딩 테스트 2: 가장 긴 암호, 가장 짧은 암호 (도전) - 정답 예시 코드

첫째 줄에 단어들이 공백으로 구분되어 주어집니다. 가장 긴 단어와 가장 짧은 단어를 찾아 출력하세요. 길이가 같으면 먼저 나온 단어를 고릅니다.
"""

words = input().split()
longest = words[0]           # 첫 단어를 일단 '최고'로 정해 두고
shortest = words[0]
for w in words:              # 나머지와 하나씩 비교
    if len(w) > len(longest):     # 더 길 때만 바꾼다 (같으면 먼저 나온 것 유지)
        longest = w
    if len(w) < len(shortest):
        shortest = w
print(f'가장 긴 암호: {longest} ({len(longest)}글자)')
print(f'가장 짧은 암호: {shortest} ({len(shortest)}글자)')
