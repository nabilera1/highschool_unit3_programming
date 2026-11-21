"""4차시 코딩 테스트 1. is_rescued 함수 (기본)

암호와 말한 글자 리스트를 받아 암호의 글자를 모두 맞혔으면 True, 아니면 False를 돌려주는 함수 is_rescued(word, guessed)를 만드세요. 첫째 줄에 암호, 둘째 줄에 n, 다음 n줄에 말한 글자들(공백 없이)이 주어지면 각 줄에 대한 함수의 결과를 출력합니다.

실행: python lesson04_test1.py  (예제 입력을 한 줄씩 넣어 확인)
"""
def is_rescued(word, guessed):
    for ch in word:
        if ch not in guessed:
            return False          # 못 맞힌 글자를 하나라도 찾으면 바로 False
    return True                   # 끝까지 없으면 True

word = input()
n = int(input())
for i in range(n):
    print(is_rescued(word, list(input())))
