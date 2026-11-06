기본 버전의 코드를 하는 일별로 함수로 나누고 `main()` 구조로 정리했습니다. 입력 검증 함수 `알파벳한글자리턴()`이 포함되어 있습니다.

내려받기: [hangman_2_function.py](https://cdn.jsdelivr.net/gh/nabilera1/highschool_unit3_programming@main/downloads/hangman_2_function.py)

```python
# ================================================================
#  행맨 게임 - 2단계 함수 버전 (6차시)
#  사용 요소: 함수(매개변수·반환값), main() 구조, 입력 검증, 리스트, 반복·조건
#  기본 버전(game_행맨_1_기본.py)의 코드를 '하는 일'별로 함수로 나누었습니다.
# ================================================================
import random

# 리스트: 틀린 횟수(0~6)가 곧 그림의 인덱스
# (r'''...''' : 역슬래시(\)를 글자 그대로 쓰기 위한 raw 문자열)
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

words = 'ant baboon badger bat bear beaver camel cat clam cobra \
cougar coyote crow deer dog donkey duck eagle ferret fox frog \
goat goose hawk lion lizard llama mole monkey moose mouse mule \
newt otter owl panda parrot pigeon python rabbit ram rat raven \
rhino salmon seal shark sheep skunk sloth snake spider stork swan \
tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def 행맨게임소개():
    """게임 규칙을 안내한다"""
    print('*' * 30)
    print('행맨 게임을 시작합니다')
    print('숨겨진 단어 맞추기 게임입니다.')
    print('알파벳 1자를 입력하면서 숨겨진 단어를 찾아주세요')
    print('기회는 6번 주어집니다.')
    print('행운을 빕니다.')
    print('*' * 30)


def 비밀단어생성(words):
    """단어 리스트에서 무작위로 하나를 골라 돌려준다"""
    n = random.randint(0, len(words) - 1)
    return words[n]


def 게임화면생성(행맨그림, 틀린단어, 맞춘단어, 비밀단어):
    """그림, 틀린 글자, 밑줄(맞힌 글자만 공개)을 출력한다"""
    print(행맨그림[len(틀린단어)])
    print()
    print('틀린 단어 표시 :', end=' ')
    for i in 틀린단어:
        print(i, end=' ')
    print()

    밑줄 = '_' * len(비밀단어)
    for i in range(len(비밀단어)):           # 맞힌 글자 자리만 밑줄을 글자로 바꾸기
        if 비밀단어[i] in 맞춘단어:
            밑줄 = 밑줄[:i] + 비밀단어[i] + 밑줄[i+1:]   # 문자열 슬라이싱
    for i in 밑줄:
        print(i, end=' ')
    print()


def 알파벳한글자리턴(단어목록):   # 단어목록 == 틀린단어 + 맞춘단어 (이미 사용한 글자)
    """올바른 알파벳 한 글자가 입력될 때까지 다시 묻고, 그 글자를 돌려준다"""
    while True:
        guess = input('입력하세요 : ')
        guess = guess.lower()                # 대문자 → 소문자
        if len(guess) != 1:
            print('한 글자만 입력해 주세요.')
        elif guess in 단어목록:
            print('그 글자는 먼저 사용했던 글자입니다. 다른 것을 선택하세요.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('알파벳 한 글자를 입력해주세요.')
        else:
            return guess


def 모두맞췄는지(비밀단어, 맞춘단어):
    """비밀 단어의 모든 글자를 맞혔으면 True, 아니면 False"""
    for 글자 in 비밀단어:
        if 글자 not in 맞춘단어:
            return False
    return True


def 게임재실행():
    """다시 할지 묻고 y로 시작하면 True"""
    print('다시 게임하실래요? (yes or no)')
    return input().lower().startswith('y')


def main():
    행맨게임소개()
    틀린단어 = ''
    맞춘단어 = ''
    비밀단어 = 비밀단어생성(words)
    게임종료 = False

    while True:
        게임화면생성(행맨그림, 틀린단어, 맞춘단어, 비밀단어)
        guess = 알파벳한글자리턴(틀린단어 + 맞춘단어)

        if guess in 비밀단어:
            맞춘단어 = 맞춘단어 + guess
            if 모두맞췄는지(비밀단어, 맞춘단어):
                print('축하합니다. ' + 비밀단어 + ' 당신이 이겼어요.')
                게임종료 = True
        else:
            틀린단어 = 틀린단어 + guess
            if len(틀린단어) == len(행맨그림) - 1:
                게임화면생성(행맨그림, 틀린단어, 맞춘단어, 비밀단어)
                print('맞출 기회를 다 놓쳤네요.')
                print(str(len(틀린단어)) + '번 틀림')
                print(str(len(맞춘단어)) + '번 맞춤')
                print('비밀단어는 ' + 비밀단어)
                게임종료 = True

        if 게임종료:
            if 게임재실행():
                틀린단어 = ''
                맞춘단어 = ''
                게임종료 = False
                비밀단어 = 비밀단어생성(words)
            else:
                break


if __name__ == '__main__':
    main()
```
