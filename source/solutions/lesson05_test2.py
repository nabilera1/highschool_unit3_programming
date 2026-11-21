"""5차시 코딩 테스트 2. 구조 출동 시뮬레이션 (도전)

첫째 줄에 암호, 둘째 줄에 입력할 알파벳들이 한 줄로 주어집니다(중복 없음). 앞에서부터 한 글자씩 게임 규칙(배터리 6칸)대로 처리하여, 모두 맞히면 구조 성공! 틀린 횟수 n, 배터리가 0칸이 되면 신호 끊김, 글자를 다 써도 끝나지 않으면 암호 미완성을 출력하세요. 게임이 끝나면 남은 글자는 무시합니다.

실행: python lesson05_test2.py  (예제 입력을 한 줄씩 넣어 확인)
"""
MAX_BATTERY = 6

def play(word, letters):
    guessed = []
    battery = MAX_BATTERY
    i = 0
    while battery > 0:
        done = True
        for ch in word:
            if ch not in guessed:
                done = False
        if done:
            return f"구조 성공! 틀린 횟수 {MAX_BATTERY - battery}"
        if i == len(letters):               # 입력할 글자를 다 썼다
            return "암호 미완성"
        g = letters[i]
        i += 1
        guessed.append(g)
        if g not in word:
            battery -= 1
    return "신호 끊김"

print(play(input(), input()))
