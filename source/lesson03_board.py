"""영단어 구조대 - 2단계: 뜻이 있는 단어장과 암호판             [3차시]

이번 단계에서 배우는 것
  - 딕셔너리        : {영단어(키): 뜻(값)}  WORDS["help"] → "도움"
  - 딕셔너리에 추가 : WORDS["thanks"] = "고마움"
  - list(WORDS)     : 딕셔너리의 키(영단어)만 모은 리스트
  - for ch in word  : 암호의 글자를 앞에서부터 하나씩 꺼낸다
  - " ".join(board) : ["h", "_", "_", "p"] → "h _ _ p"

암호판이 만들어지는 원리 (word = "help", guessed = ["h", "p"])
  h → guessed에 있음 → h
  e → 없음           → _
  l → 없음           → _
  p → 있음           → p          암호판:  h _ _ p

※ 4차시에는 이 암호판 코드를 make_board(word, guessed) 함수로 만듭니다.
실행 방법: python lesson03_board.py
"""
import random

WORDS = {"help": "도움", "safe": "안전한", "hope": "희망", "rescue": "구조하다",
         "friend": "친구", "share": "나누다", "smile": "미소"}
WORDS["together"] = "함께"                 # 딕셔너리에 새 단어 추가

word = random.choice(list(WORDS))          # 키(영단어) 중 하나를 고른다
print(f"[SOS] {len(word)}글자 암호, 뜻 힌트: {WORDS[word]}")

guessed = []
for turn in range(3):                      # 이번 단계에서는 3번만 입력 (횟수가 정해진 반복 → for)
    g = input("알파벳 한 글자 > ")
    guessed.append(g)

    board = []                             # 암호판 만들기
    for ch in word:
        if ch in guessed:
            board.append(ch)
        else:
            board.append("_")
    print("암호판:", " ".join(board))

print("정답 확인(교사용):", word)
