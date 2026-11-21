"""[산출물 예시] 과제 A · 하 – 교사의 도움을 받아 단어장에서 뜻 읽기

과제 A: 단어장에 서로 돕는 말을 추가하고, 출동이 끝나면 시도 기록(틀린 글자, 남은 배터리)을 출력하시오.
하 수준 예시는 게임 대신 파일 맨 아래에서 단어장과 암호판을 읽는 코드를 실행합니다.
'# ★' 주석이 달린 줄이 학생이 바꾸거나 추가한 줄입니다.
※ 실제 학생 산출물이 아니라, 교사 연수·수업 전 기대 수준 공유를 위해 만든 예시입니다.
실행 방법: python taskA_low.py
"""
import random

# 암호 단어장: {영단어(키): 뜻(값)}  - 서로 돕는 말
WORDS = {"help": "도움", "safe": "안전한", "hope": "희망", "rescue": "구조하다",
         "friend": "친구", "share": "나누다", "smile": "미소", "together": "함께"}
MAX_BATTERY = 6          # 구조 신호 배터리 칸 수 = 틀릴 수 있는 횟수
WORDS["thanks"] = "고마움"         # ★ 선생님과 함께 단어 1개 추가


def pick_word(words):
    """단어장에서 암호(영단어) 하나를 무작위로 골라 돌려준다"""
    return random.choice(list(words))          # list(words): 딕셔너리의 키만 모은 리스트


def make_board(word, guessed):
    """맞힌 글자는 보여 주고 나머지는 _ 로 가린 암호판 문자열을 돌려준다"""
    board = []
    for ch in word:                            # 암호의 글자를 하나씩
        if ch in guessed:
            board.append(ch)
        else:
            board.append("_")
    return " ".join(board)                     # ["_", "_", "_", "p"] → "_ _ _ p"


def make_battery(battery):
    """남은 칸은 ■, 쓴 칸은 □ 로 배터리 그림 문자열을 돌려준다"""
    return "■" * battery + "□" * (MAX_BATTERY - battery)


def ask_letter(guessed):
    """아직 말하지 않은 알파벳 한 글자가 들어올 때까지 다시 묻고, 그 글자를 돌려준다"""
    while True:
        g = input("알파벳 한 글자 > ").strip().lower()   # 앞뒤 공백 제거, 소문자로
        if len(g) != 1 or g not in "abcdefghijklmnopqrstuvwxyz":
            print("알파벳 한 글자만 입력하세요.")
        elif g in guessed:
            print("이미 말한 글자예요.")
        else:
            return g


def play(word):
    """암호 word 로 한 번 출동한다. (성공 여부, 틀린 횟수)를 돌려준다"""
    guessed = []                               # 지금까지 말한 글자
    battery = MAX_BATTERY
    while battery > 0:                         # 배터리가 남아 있는 동안 반복
        board = make_board(word, guessed)
        print(f"암호판: {board}   배터리: {make_battery(battery)}")
        if "_" not in board:                   # 가린 글자가 없으면 = 모두 맞힘
            print(f"구조 성공! 암호 {word} = {WORDS[word]}")
            return True, MAX_BATTERY - battery
        g = ask_letter(guessed)
        guessed.append(g)
        if g not in word:
            battery -= 1
            print("암호에 없는 글자예요. 신호가 약해집니다.")
    print(f"신호가 끊겼어요. 암호는 {word}({WORDS[word]})였어요.")
    return False, MAX_BATTERY


def text_width(text):
    """화면에서 차지하는 칸 수를 센다 (한글은 2칸, 영문·숫자·기호는 1칸)"""
    width = 0
    for ch in text:
        if "가" <= ch <= "힣":                  # 한글 글자는 화면에서 두 칸
            width += 2
        else:
            width += 1
    return width


def print_records(records):
    """출동 기록표(2차원 리스트)를 중첩 for 문으로 출력한다

    한글은 화면에서 2칸을 차지하므로, 글자 수가 아니라 화면 칸 수(text_width)로
    빈칸을 채워야 표의 세로줄이 맞는다.
    """
    for row in [["출동", "암호", "결과", "틀린 횟수"]] + records:   # 바깥 for: 행
        cells = []
        for item in row:                                            # 안쪽 for: 칸
            text = str(item)
            cells.append(text + " " * (10 - text_width(text)))      # 화면에서 10칸이 되게 채우기
        print(" | ".join(cells).rstrip())


def main():
    print("=== 영단어 구조대 === 암호를 완성해 친구를 구조하세요!")
    records = []                               # [[출동 번호, 암호, 결과, 틀린 횟수], ...]
    while True:
        word = pick_word(WORDS)
        success, wrong = play(word)
        records.append([len(records) + 1, word, "성공" if success else "실패", wrong])
        print_records(records)
        if input("다시 출동할까요? (y/n) > ").strip().lower() != "y":
            break
    print("오늘도 수고했어요, 구조대원님!")


if __name__ == "__main__":
    print(WORDS["help"])                      # ★ 단어장에서 뜻 꺼내 읽기
    print(WORDS["thanks"])                    # ★ 스스로 추가
    print(make_board("thanks", ["t", "s"]))   # ★ 암호판 읽기
    # main()                                  # ★ 게임은 잠시 꺼 둠
