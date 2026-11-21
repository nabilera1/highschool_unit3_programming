"""2차시 코딩 테스트 1. 번호로 암호 꺼내기 (기본)

첫째 줄에 단어들이 공백으로 구분되어 주어지고, 둘째 줄에 번호 k(1부터 시작)가 주어집니다. k번째 단어와 그 글자 수를 공백으로 구분해 출력하세요.

실행: python lesson02_test1.py  (예제 입력을 한 줄씩 넣어 확인)
"""
words = input().split()
k = int(input())
word = words[k - 1]          # 사람은 1부터, 파이썬은 0부터 센다
print(word, len(word))
