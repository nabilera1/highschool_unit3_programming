"""6차시 코딩 테스트 2. 출동 기록 분석 (도전)

첫째 줄에 n, 다음 n줄에 암호 결과 틀린횟수가 주어집니다(결과는 성공 또는 실패). 결과별 횟수를 성공: a번, 실패: b번으로 출력하고, 성공한 기록 중 틀린 횟수가 가장 많은 출동을 가장 아슬아슬한 구조: 암호 (틀림 k)로 출력하세요(같으면 먼저 나온 것). 성공 기록이 없으면 성공 기록 없음을 출력합니다.

실행: python lesson06_test2.py  (예제 입력을 한 줄씩 넣어 확인)
"""
records = []
n = int(input())
for i in range(n):
    word, result, wrong = input().split()
    records.append([word, result, int(wrong)])

count = {"성공": 0, "실패": 0}          # 결과별 횟수 (딕셔너리)
best = None                          # 가장 아슬아슬한 구조 행
for row in records:
    count[row[1]] += 1
    if row[1] == "성공":
        if best is None or row[2] > best[2]:
            best = row
print(f"성공: {count['성공']}번")
print(f"실패: {count['실패']}번")
if best is None:
    print("성공 기록 없음")
else:
    print(f"가장 아슬아슬한 구조: {best[0]} (틀림 {best[2]})")
