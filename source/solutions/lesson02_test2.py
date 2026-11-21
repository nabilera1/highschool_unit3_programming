"""2차시 코딩 테스트 2. 배터리 그림 그리기 (도전)

틀린 횟수 k(0~6)가 주어질 때, 배터리 6칸 중 남은 칸은 ■, 쓴 칸은 □로 [■■■■□□]처럼 출력하고, 다음 줄에 남은 배터리: n칸을 출력하세요.

실행: python lesson02_test2.py  (예제 입력을 한 줄씩 넣어 확인)
"""
MAX_BATTERY = 6
k = int(input())
battery = MAX_BATTERY - k
print("[" + "■" * battery + "□" * k + "]")
print(f"남은 배터리: {battery}칸")
