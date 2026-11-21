"""영단어 구조대 (함수 없는 버전)                              [4차시 비교용]

word_rescue.py 와 하는 일·화면이 똑같은 게임을 '함수(def) 없이'
위에서 아래로 한 덩어리로 쓴 코드입니다.

4차시에는 두 코드를 나란히 놓고
  ① 같은 입력이면 화면도 똑같은지 실행해 확인하고
  ② 이 파일의 [A]~[F] 구간이 word_rescue.py 의 어느 함수가 되었는지 짝짓고
  ③ 같은 기능을 더할 때 어느 쪽이 고치기 쉬운지 비교합니다.

구간 표시
  [A] 암호 고르기        → pick_word()
  [B] 암호판 만들기      → make_board()
  [C] 배터리 그림        → make_battery()
  [D] 글자 입력·검사     → ask_letter()
  [E] 한 판 진행         → play()
  [F] 출동 기록표 출력   → print_records(), text_width()
  (전체 흐름)            → main()

실행 방법: python word_rescue_nofunc.py   (Python 3.10 이상)
"""
import random

# 암호 단어장: {영단어(키): 뜻(값)}  - 서로 돕는 말
WORDS = {"help": "도움", "safe": "안전한", "hope": "희망", "rescue": "구조하다",
         "friend": "친구", "share": "나누다", "smile": "미소", "together": "함께"}
MAX_BATTERY = 6          # 구조 신호 배터리 칸 수 = 틀릴 수 있는 횟수

print("=== 영단어 구조대 === 암호를 완성해 친구를 구조하세요!")
records = []                                   # [[출동 번호, 암호, 결과, 틀린 횟수], ...]
while True:
    # [A] 암호 고르기
    word = random.choice(list(WORDS))

    # [E] 한 판 진행 ------------------------------------------------
    guessed = []
    battery = MAX_BATTERY
    success = False                            # 함수가 없으니 결과를 변수에 담아 둔다
    while battery > 0:
        # [B] 암호판 만들기
        board = []
        for ch in word:
            if ch in guessed:
                board.append(ch)
            else:
                board.append("_")
        board = " ".join(board)
        # [C] 배터리 그림
        battery_img = "■" * battery + "□" * (MAX_BATTERY - battery)
        print(f"암호판: {board}   배터리: {battery_img}")
        if "_" not in board:
            print(f"구조 성공! 암호 {word} = {WORDS[word]}")
            success = True
            break                              # return 대신 break 로 반복을 빠져나온다
        # [D] 글자 입력·검사
        while True:
            g = input("알파벳 한 글자 > ").strip().lower()
            if len(g) != 1 or g not in "abcdefghijklmnopqrstuvwxyz":
                print("알파벳 한 글자만 입력하세요.")
            elif g in guessed:
                print("이미 말한 글자예요.")
            else:
                break
        guessed.append(g)
        if g not in word:
            battery -= 1
            print("암호에 없는 글자예요. 신호가 약해집니다.")
    if not success:
        print(f"신호가 끊겼어요. 암호는 {word}({WORDS[word]})였어요.")
    wrong = MAX_BATTERY - battery
    # ----------------------------------------------------------------

    records.append([len(records) + 1, word, "성공" if success else "실패", wrong])

    # [F] 출동 기록표 출력
    for row in [["출동", "암호", "결과", "틀린 횟수"]] + records:
        cells = []
        for item in row:
            text = str(item)
            width = 0                          # 화면 칸 수 세기 (한글은 2칸)
            for ch in text:
                if "가" <= ch <= "힣":
                    width += 2
                else:
                    width += 1
            cells.append(text + " " * (10 - width))
        print(" | ".join(cells).rstrip())

    if input("다시 출동할까요? (y/n) > ").strip().lower() != "y":
        break
print("오늘도 수고했어요, 구조대원님!")
