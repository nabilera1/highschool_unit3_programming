"""1차시 코딩 테스트 1. 밑줄 암호 만들기 (기본)

영단어 암호 하나를 입력받아 첫째 줄에 글자 수: n, 둘째 줄에 글자 수만큼의 _를 한 칸씩 띄어 출력하세요.

실행: python lesson01_test1.py  (예제 입력을 한 줄씩 넣어 확인)
"""
word = input()
print(f"글자 수: {len(word)}")
print(" ".join(["_"] * len(word)))
