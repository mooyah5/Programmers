# 옹알이
# Lv 0

# 문제
# 애가 아직 'aya', 'ye', 'woo', 'ma'
# 4가지 발음을 최대 1번 씩 사용해 이어붙인 발음밖에 못함

# 입력
# babbling : 문자열 배열

# 출력
# 애가 발음할 수 있는 단어 개수

# 예제2) ["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]
# "aya"+"ye" / "ye" / "ye"+"ma"+"woo" 3가지 가능 답 3
# 안되는 예_ "ayaa" 는 뒤에 a가 붙어서 안됨.

def solution(babbling):
    bab_list = ['aya', 'ye', 'woo', 'ma']
    answer = 0
    for bab in babbling:                    # 단어 하나씩 추출
        word = ''
        cnt = 0
        for b in bab:                       # 단어의 글자씩 추출하여 word 이어붙이다가
            word += b
            if word in bab_list:            # 이어붙인 word가 발음 가능하면 cnt증가 후 word 초기화
                word = ''
                cnt += 1
        if len(word) == 0 and cnt > 0:      # 단어 하나 회문 돌고나서 남은 쓰레기 단어가 없고, cnt가 존재하면 answer 증가!
            answer += 1
    return answer
