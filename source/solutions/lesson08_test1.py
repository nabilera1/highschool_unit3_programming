"""8차시 코딩 테스트 1. print_success 함수 (형성평가 11번) (기본)

출동 기록표 records를 받아 결과가 성공인 출동의 암호만 한 줄씩 출력하는 함수 print_success(records)를 만드세요. 첫째 줄에 n, 다음 n줄에 출동번호 암호 결과 틀린횟수가 주어집니다. 성공한 출동이 없으면 아무것도 출력하지 않습니다.

실행: python lesson08_test1.py  (예제 입력을 한 줄씩 넣어 확인)
"""
def print_success(records):
    for row in records:
        if row[2] == "성공":
            print(row[1])

records = []
n = int(input())
for i in range(n):
    no, word, result, wrong = input().split()
    records.append([int(no), word, result, int(wrong)])
print_success(records)
