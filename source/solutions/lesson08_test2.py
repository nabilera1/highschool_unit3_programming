"""8차시 코딩 테스트 2. count_wrong 함수 (형성평가 12번) (도전)

암호 word와 말한 글자 리스트 guessed를 받아 틀린 글자의 개수를 돌려주는 함수 count_wrong(word, guessed)를 만드세요. 첫째 줄에 암호, 둘째 줄에 말한 글자들이 공백으로 구분되어 주어지면 함수의 결과를 출력합니다.

실행: python lesson08_test2.py  (예제 입력을 한 줄씩 넣어 확인)
"""
def count_wrong(word, guessed):
    count = 0
    for g in guessed:
        if g not in word:
            count += 1
    return count

word = input()
guessed = input().split()
print(count_wrong(word, guessed))
