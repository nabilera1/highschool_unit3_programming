"""6차시 코딩 테스트 1. 기록표에서 출동 찾기 (기본)

첫째 줄에 n, 다음 n줄에 출동번호 암호 결과 틀린횟수가 주어집니다. 이를 2차원 리스트에 저장한 뒤, 마지막 줄에 출동 번호 k가 주어지면 k번 출동: 암호 (결과, 틀린 횟수 t)를 출력하세요.

실행: python lesson06_test1.py  (예제 입력을 한 줄씩 넣어 확인)
"""
records = []
n = int(input())
for i in range(n):
    no, word, result, wrong = input().split()
    records.append([int(no), word, result, int(wrong)])   # 한 행 추가
k = int(input())
row = records[k - 1]                 # 출동 번호는 1부터, 행 번호는 0부터
print(f"{row[0]}번 출동: {row[1]} ({row[2]}, 틀린 횟수 {row[3]})")
