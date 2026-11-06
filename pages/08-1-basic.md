함수 없이 위에서 아래로 실행되는 코드입니다. 7차시 테스트 활동을 위해 **입력 검사를 일부러 넣지 않았습니다.** 대문자 `A`, 숫자 `1`, 두 글자 `ab`, 단어 전체를 입력해 보세요.

내려받기: [hangman_1_basic.py](https://cdn.jsdelivr.net/gh/nabilera1/highschool_unit3_programming@main/downloads/hangman_1_basic.py)

```python
# ================================================================
#  행맨 게임 - 1단계 기본 버전 (5차시)
#  사용 요소: 리스트, 문자열, 반복문(while·for), 조건문(if·else), random
#  ※ 함수 없이 위에서 아래로 실행되는 코드입니다.
#  ※ 7차시 '테스트 및 개선' 활동을 위해 입력 검사를 일부러 넣지 않았습니다.
#     (대문자, 숫자, 두 글자 이상, 이미 입력한 글자를 넣으면 어떻게 될까요?)
# ================================================================
import random

# 리스트: 틀린 횟수(0~6)가 곧 그림의 인덱스가 됩니다.
행맨그림 = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

# 리스트: 비밀 단어 후보 (split()으로 공백 기준 나누기)
words = 'ant baboon badger bat bear beaver camel cat clam cobra \
cougar coyote crow deer dog donkey duck eagle ferret fox frog \
goat goose hawk lion lizard llama mole monkey moose mouse mule \
newt otter owl panda parrot pigeon python rabbit ram rat raven \
rhino salmon seal shark sheep skunk sloth snake spider stork swan \
tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

print('*' * 30)
print('행맨 게임을 시작합니다')
print('알파벳 1자를 입력하면서 숨겨진 단어를 찾아주세요')
print('기회는 6번 주어집니다.')
print('*' * 30)

비밀단어 = random.choice(words)   # 리스트에서 무작위로 하나 고르기
맞춘단어 = ''                      # 맞힌 글자를 모아 두는 문자열
틀린단어 = ''                      # 틀린 글자를 모아 두는 문자열

while True:
    # ---------- 출력: 그림, 틀린 글자, 밑줄 ----------
    print(행맨그림[len(틀린단어)])
    print('틀린 글자 :', end=' ')
    for 글자 in 틀린단어:
        print(글자, end=' ')
    print()

    for 글자 in 비밀단어:            # 맞힌 글자는 보여 주고, 아니면 밑줄
        if 글자 in 맞춘단어:
            print(글자, end=' ')
        else:
            print('_', end=' ')
    print()

    # ---------- 입력 ----------
    guess = input('입력하세요 : ')

    # ---------- 처리: 판정 ----------
    if guess in 비밀단어:
        맞춘단어 = 맞춘단어 + guess
    else:
        틀린단어 = 틀린단어 + guess

    # ---------- 종료 조건 ① 모두 맞힘 ----------
    모두맞춤 = True
    for 글자 in 비밀단어:
        if 글자 not in 맞춘단어:
            모두맞춤 = False
            break
    if 모두맞춤:
        print('축하합니다! 비밀 단어는 ' + 비밀단어 + ' 입니다. 당신이 이겼어요.')
        break

    # ---------- 종료 조건 ② 기회 소진 ----------
    if len(틀린단어) >= len(행맨그림) - 1:
        print(행맨그림[-1])
        print('맞출 기회를 다 놓쳤네요. 비밀 단어는 ' + 비밀단어 + ' 입니다.')
        break
```
