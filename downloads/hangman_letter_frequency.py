# ================================================================
#  행맨 심화 탐구 (7차시) - 어떤 글자부터 고르면 유리할까?
#  딕셔너리로 '각 글자가 들어 있는 단어 수'를 세고, 확률로 바꾸어 비교합니다.
#  수학 연계: 확률 = (그 글자가 들어 있는 단어 수) / (전체 단어 수)
# ================================================================
words = 'ant baboon badger bat bear beaver camel cat clam cobra \
cougar coyote crow deer dog donkey duck eagle ferret fox frog \
goat goose hawk lion lizard llama mole monkey moose mouse mule \
newt otter owl panda parrot pigeon python rabbit ram rat raven \
rhino salmon seal shark sheep skunk sloth snake spider stork swan \
tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()

빈도 = {}                              # 딕셔너리: 글자 → 그 글자가 들어 있는 단어 수
for 단어 in words:                     # 바깥 반복: 단어 하나씩
    for 글자 in set(단어):             # 안쪽 반복: 단어 속 서로 다른 글자 (set으로 중복 제거)
        if 글자 in 빈도:
            빈도[글자] += 1
        else:
            빈도[글자] = 1

# 많이 나온 순서로 정렬 (값을 기준으로 내림차순)
순위 = sorted(빈도.items(), key=lambda 쌍: 쌍[1], reverse=True)

print(f'전체 단어 수: {len(words)}개\n')
print('순위  글자  단어 수   확률     막대')
for i in range(len(순위)):
    글자, 수 = 순위[i]
    확률 = 수 / len(words)
    print(f'{i + 1:>3}   {글자}    {수:>3}개   {확률:6.1%}   ' + '■' * 수)

# 생각해 보기
#  1) 처음 한 글자를 고른다면 어떤 글자가 가장 유리할까? 그 확률은?
#  2) 'x'나 'z'를 먼저 고르면 왜 불리할까?
#  3) 단어 목록(주제)이 바뀌면 순위도 바뀔까? 내 게임의 단어 목록으로 바꾸어 실행해 보자.
