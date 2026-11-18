"""2차시 코딩 테스트 1: 번호로 암호 꺼내기 (기본) - 정답 예시 코드

첫째 줄에 단어들이 공백으로 구분되어 주어지고, 둘째 줄에 번호 k(1부터 시작)가 주어집니다. k번째 단어와 그 글자 수를 공백으로 구분해 출력하세요.
"""

words = input().split()      # 'help rescue' → ['help', 'rescue']
k = int(input())
word = words[k - 1]          # 사람의 번호(1부터) → 인덱스(0부터)
print(word, len(word))
