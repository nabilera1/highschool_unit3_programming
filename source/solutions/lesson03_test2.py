"""3차시 코딩 테스트 2. 뜻 힌트 사전 (도전)

첫째 줄에 n, 다음 n줄에 영단어 뜻이 주어집니다. 다음 줄에 m, 다음 m줄에 찾을 영단어가 주어지면 뜻을 출력하고, 단어장에 없으면 단어장에 없어요를 출력하세요.

실행: python lesson03_test2.py  (예제 입력을 한 줄씩 넣어 확인)
"""
WORDS = {}
n = int(input())
for i in range(n):
    eng, kor = input().split()
    WORDS[eng] = kor              # 딕셔너리에 추가
m = int(input())
for i in range(m):
    w = input()
    if w in WORDS:                # 키가 있는지 먼저 확인
        print(WORDS[w])
    else:
        print("단어장에 없어요")
