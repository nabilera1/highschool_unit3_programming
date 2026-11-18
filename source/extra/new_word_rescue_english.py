"""영단어 구조대 (영어 변수 이름 버전) - 딕셔너리, 리스트, for 반복문, 함수

실행 방법: python new_word_rescue_english.py
"""

# =====================================================================
# 이야기
#   산에서 길을 잃은 친구가 SOS 구조 신호를 보냈어요!
#   신호는 영단어 암호로 되어 있어요. 뜻(힌트)을 보고 알파벳을 한 글자씩 맞혀
#   암호를 완성하면 구조 헬기가 출동해 친구를 구할 수 있어요.
#
# 게임 규칙
#   - 맞힌 글자가 늘어날수록 구조대가 친구에게 가까워져요.  [=====>     ]
#   - 암호에 없는 글자를 말하면 구조 신호 배터리가 한 칸 줄어요.  ■■■■□□
#   - 배터리가 남아 있는 동안 암호를 완성하면 구조 성공!
#   - 배터리가 다 닳아도 괜찮아요. 정답을 확인하고 다시 출동할 수 있어요.
#
# (원래 '행맨' 게임과 규칙은 같지만, 무서운 그림 대신 '사람을 돕는' 이야기로 바꿨어요.)
#
# 이 게임에서 쓰는 자료구조
#   딕셔너리 WORDS   : {영단어: 뜻}        → 암호 단어장.  WORDS["help"] → "도움"
#   리스트   guessed : 지금까지 말한 글자   → ['h', 'e', 'z']
#
# 암호판(보드)이 만들어지는 원리
#   word = "help", guessed = ['h', 'p']
#   단어의 글자를 하나씩 보면서 → 말한 글자면 그대로, 아니면 "_"
#   h → h,  e → _,  l → _,  p → p      →  "h _ _ p"
# =====================================================================

import random

# 암호 단어장 딕셔너리 {영단어: 뜻} - 서로 돕고 지키는 것과 관련된 단어들
# ← 여기에 단어를 더 추가해 보세요!
WORDS = {
    "help": "도움",
    "rescue": "구조",
    "safe": "안전한",
    "hope": "희망",
    "friend": "친구",
    "doctor": "의사",
    "together": "함께",
}
MAX_BATTERY = 6     # 구조 신호 배터리 칸 수 (대문자 = 바뀌지 않는 값, 상수)
ROAD = 10           # 구조대가 친구에게 가는 길의 칸 수


def make_board(word, guessed):
    """맞힌 글자는 보여 주고, 아직 못 맞힌 글자는 _ 로 가린 문자열을 돌려준다"""
    board = ""
    for ch in word:                 # 단어의 글자를 하나씩 꺼내서
        if ch in guessed:           # 이미 말한 글자면
            board += ch + " "       #   그 글자를 보여 주고
        else:
            board += "_ "           #   아니면 _ 로 가림
    return board.strip()            # 맨 끝 공백 하나를 지우고 돌려줌


def make_road(word, guessed):
    """맞힌 글자 비율만큼 구조대가 친구에게 다가간 모습을 문자열로 돌려준다"""
    found = 0
    for ch in word:                 # 단어에서 이미 맞힌 글자 수 세기
        if ch in guessed:
            found += 1
    step = found * ROAD // len(word)            # 맞힌 비율 → 0 ~ ROAD 칸
    # "=" 로 지나온 길, ">" 는 구조대, " " 는 남은 길
    return "구조대 [" + "=" * step + ">" + " " * (ROAD - step) + "] 친구"


def ask_letter(guessed):
    """알파벳 한 글자이면서, 아직 말하지 않은 글자가 들어올 때까지 다시 묻는다"""
    while True:
        ch = input("알파벳 한 글자 > ").strip().lower()   # 공백 제거 + 소문자로 통일
        if len(ch) != 1 or not ("a" <= ch <= "z"):
            # 두 글자 이상이거나, a~z 가 아니면 (한글 자판 상태에서 친 'ㅁ' 등도 여기서 걸러짐)
            print("영어 알파벳 한 글자만 입력하세요!")
        elif ch in guessed:
            print("이미 말한 글자예요!")
        else:
            return ch                                    # 올바른 글자 → 돌려주고 함수 끝


def play():
    """한 번 출동하고, 구조에 성공하면 True / 실패하면 False 를 돌려준다"""
    word = random.choice(list(WORDS))    # list(WORDS) → 영단어(키) 목록, 그중 하나를 무작위로
    guessed = []                         # 말한 글자 기록 (빈 리스트에서 시작)
    battery = MAX_BATTERY
    print(f"\n[SOS] 친구의 구조 신호 도착! 암호의 뜻: {WORDS[word]}  /  글자 수: {len(word)}")

    while battery > 0:                   # 배터리가 남아 있는 동안 반복
        board = make_board(word, guessed)
        print(make_road(word, guessed))
        # '■' * 4 → '■■■■' (문자열 반복). ■ □ 입력: 한글 상태에서 ㅁ + [한자] 키 → 목록에서 선택
        print(f"암호: {board}   신호 배터리: {'■' * battery}{'□' * (MAX_BATTERY - battery)}   말한 글자: {guessed}")

        if "_" not in board:             # 가려진 칸이 하나도 없으면 → 암호 완성!
            print(f"구조 성공! 암호 '{word}'({WORDS[word]})로 헬기가 출동해 친구가 무사히 돌아왔어요!")
            return True

        ch = ask_letter(guessed)
        guessed.append(ch)               # 말한 글자를 기록에 추가
        if ch in word:                   # 문자열에도 in 을 쓸 수 있어요: 'p' in 'help' → True
            print("좋아요! 구조대가 한 걸음 더 다가갔어요.")
        else:
            battery -= 1                 # 없는 글자면 배터리 1칸 감소
            print("암호에 없는 글자예요. 신호 배터리가 한 칸 줄었어요.")

    # 반복이 끝났다 = 배터리를 모두 썼다
    print(f"신호가 약해졌어요. 암호는 '{word}'({WORDS[word]})였어요. 다시 출동해서 친구를 구해 볼까요?")
    return False


def main():
    print("=== 영단어 구조대 === 영단어 암호를 완성해 친구를 구조하세요!")
    rescued = trips = 0
    while True:
        trips += 1
        if play():                       # play() 가 True 를 돌려주면 구조 성공
            rescued += 1
        print(f"출동: {trips}번 / 구조한 친구: {rescued}명")
        if input("또 출동할까요? (y/n) > ").strip().lower() != "y":
            print("오늘도 수고했어요, 구조대원님!")
            break


if __name__ == "__main__":
    main()
