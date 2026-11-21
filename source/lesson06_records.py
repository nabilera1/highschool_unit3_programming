"""영단어 구조대 - 출동 기록표(2차원 리스트) 연습                 [6차시]

게임을 3번 출동한 뒤의 기록표가 아래 records 라고 하자.
  한 행 = [출동 번호, 암호, 결과, 틀린 횟수]
  records[행][칸] → '몇 번째 출동의 몇 번째 칸'

① ~ ⑧ 의 출력을 먼저 예측해서 활동지에 적은 뒤 실행해 확인하세요.
실행 방법: python lesson06_records.py   (word_rescue.py 와 같은 폴더에서)
"""
from word_rescue import text_width     # 게임 코드의 함수를 가져와 다시 쓴다 (4차시)

records = [[1, "help", "성공", 1],
           [2, "safe", "실패", 6],
           [3, "rescue", "성공", 2]]

print("① records[0]       →", records[0])        # 한 행 = 1번 출동 기록 전체
print("② records[1][2]    →", records[1][2])     # 2번 출동의 결과
print("③ records[2][1]    →", records[2][1])     # 3번 출동의 암호
print("④ len(records)     →", len(records))      # 행의 개수 = 출동 횟수

# ⑤ 중첩 for: 바깥 for 는 행(출동), 안쪽 for 는 칸
#    한글은 화면에서 2칸이므로 text_width()로 화면 칸 수를 세어 빈칸을 채운다
print("⑤ 기록표")
for row in [["출동", "암호", "결과", "틀린 횟수"]] + records:
    cells = []
    for item in row:
        text = str(item)
        cells.append(text + " " * (10 - text_width(text)))
    print(" | ".join(cells).rstrip())

# ⑥ 행을 하나씩 보며 조건에 맞는 것만 고르기 (성공한 출동의 암호)
print("⑥ 성공한 암호:", end=" ")
for row in records:
    if row[2] == "성공":
        print(row[1], end=" ")
print()

# ⑦ 한 칸(열)만 모아 계산하기: 틀린 횟수 합계와 평균
total = 0
for row in records:
    total += row[3]
print(f"⑦ 틀린 횟수 합계 {total}, 평균 {total / len(records):.1f}")

# ⑧ 새 출동 기록을 한 행 추가하기
records.append([4, "hope", "성공", 0])
print("⑧ 추가한 뒤 출동 횟수:", len(records), "/ 마지막 행:", records[-1])
