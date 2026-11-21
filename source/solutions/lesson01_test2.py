"""1차시 코딩 테스트 2. 이 글자는 몇 번? (도전)

첫째 줄에 암호, 둘째 줄에 알파벳 한 글자를 입력받아 그 글자가 암호에 몇 번 있는지 출력하세요. 있으면 n번 있어요, 없으면 없어요를 출력합니다. (for 문으로 직접 세어 보세요.)

실행: python lesson01_test2.py  (예제 입력을 한 줄씩 넣어 확인)
"""
word = input()
g = input()
count = 0
for ch in word:
    if ch == g:
        count += 1
if count > 0:
    print(f"{count}번 있어요")
else:
    print("없어요")
