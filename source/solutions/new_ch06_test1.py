"""6차시 코딩 테스트 1: 모두맞췄는지 함수 (기본) - 정답 예시 코드

`모두맞췄는지(비밀단어, 맞춘단어)` 함수를 만드세요. 첫째 줄에 암호, 둘째 줄에 n, 다음 n줄에 맞춘 글자들이 주어지면 각 줄마다 함수의 결과(True/False)를 출력합니다.
"""

def 모두맞췄는지(비밀단어, 맞춘단어):
    for 글자 in 비밀단어:
        if 글자 not in 맞춘단어:
            return False
    return True

비밀단어 = input()
n = int(input())
for _ in range(n):
    print(모두맞췄는지(비밀단어, input()))
