"""영단어 구조대 - 1단계: 단어장에서 암호 고르기                [2차시]

이번 단계에서 배우는 것
  - 리스트        : 여러 단어를 한 변수에 순서대로 담는다.   words[0] → "help"
  - random.choice : 리스트에서 하나를 무작위로 고른다.
  - 문자열        : len()으로 글자 수, word[0]으로 첫 글자, in 으로 포함 여부
  - 리스트 append : 말한 글자를 guessed 리스트에 차례로 쌓는다.
  - 문자열 곱하기 : "■" * 5 → "■■■■■"  (배터리 그림)

실행 방법: python lesson02_words.py
"""
import random

# 암호 단어장 (리스트) - 3차시에 '뜻'을 함께 담는 딕셔너리로 바뀝니다
words = ["help", "safe", "hope", "rescue", "friend", "share", "smile", "together"]
MAX_BATTERY = 6

# 1) 암호를 무작위로 하나 고른다
word = random.choice(words)
print(f"[SOS] {len(word)}글자 암호가 도착했어요. 첫 글자는 {word[0]} 입니다.")

# 2) 게임이 기억할 자료를 만든다
guessed = []                  # 말한 글자 리스트 (처음엔 비어 있음)
battery = MAX_BATTERY         # 남은 구조 신호 배터리

# 3) 알파벳 한 글자를 입력받아 판단한다 (반복은 5차시에!)
g = input("알파벳 한 글자 > ")
guessed.append(g)
if g in word:
    print(f"{g} 는 암호에 있어요!")
else:
    battery = battery - 1
    print(f"{g} 는 암호에 없어요. 신호가 약해집니다.")

# 4) 지금 상태를 보여 준다
print("말한 글자:", guessed)
print("배터리:", "■" * battery + "□" * (MAX_BATTERY - battery), f"({battery}칸)")
print("정답 확인(교사용):", word)
