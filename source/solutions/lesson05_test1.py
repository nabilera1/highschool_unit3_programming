"""5차시 코딩 테스트 1. 배터리가 다 닳을 때까지 (기본)

처음 배터리 칸 수 n(1~10)이 주어집니다. while 문으로 배터리가 0이 될 때까지 한 칸씩 줄이며 ■를 남은 칸 수만큼 출력하고 옆에 (n칸)을 붙이세요. 0칸이 되면 신호 끊김을 출력합니다.

실행: python lesson05_test1.py  (예제 입력을 한 줄씩 넣어 확인)
"""
battery = int(input())
while battery > 0:
    print("■" * battery, f"({battery}칸)")
    battery -= 1                # 조건에 쓰인 변수를 바꾼다
print("신호 끊김")
