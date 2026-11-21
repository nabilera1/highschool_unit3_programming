"""영단어 구조대 심화 - 글자 빈도로 '먼저 말할 글자' 찾기         [8차시 심화]

질문: 처음에 어떤 알파벳을 말하면 맞힐 가능성이 가장 높을까?
방법: 단어장의 각 알파벳이 '들어 있는 단어'가 몇 개인지 센다.
      (한 단어에 같은 글자가 여러 번 나와도 1번만 센다 → set(word) 사용)
      확률(%) = 그 글자가 들어 있는 단어 수 / 전체 단어 수 × 100

배우는 것: 딕셔너리로 개수 세기(get), 중첩 for, 정렬, 확률, 데이터에 근거한 전략
실행 방법: python lesson08_letter_freq.py
"""
from word_rescue import WORDS      # 게임과 같은 단어장을 가져온다 (함수 파일의 장점!)

freq = {}                                      # 딕셔너리: 글자 → 그 글자가 들어 있는 단어 수
for word in WORDS:                             # 바깥 for: 단어 하나씩
    for ch in set(word):                       # 안쪽 for: 그 단어의 '서로 다른' 글자 하나씩
        freq[ch] = freq.get(ch, 0) + 1         # 처음 나온 글자면 0 + 1

# (글자, 개수) 쌍을 개수가 큰 순서로 정렬 (개수가 같으면 알파벳 순)
ranking = sorted(sorted(freq.items()), key=lambda pair: pair[1], reverse=True)

print(f"단어 {len(WORDS)}개 기준, 처음에 말하면 맞힐 확률 (상위 5개)")
for ch, count in ranking[:5]:
    print(f"{ch}: {count}개 단어 ({count / len(WORDS) * 100:.1f}%) " + "■" * count)

print("\n잘 나오지 않는 글자")
for ch in "zqxj":
    print(f"{ch}: {freq.get(ch, 0)}개 단어 ({freq.get(ch, 0) / len(WORDS) * 100:.1f}%)")
