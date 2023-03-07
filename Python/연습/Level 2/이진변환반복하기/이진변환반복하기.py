def solution(S):
    answer = [0, 0]  # 0항은 '0'을 없앤 횟수, 1항은 없앤 '0'의 개수

    def binary(S):
        # 재귀함수 진행 중 S가 '1'이 되면 리턴하고 끝낸다.
        if S == '1':
            return answer
        newStr = S.replace('0', '')  # '0' 없애주기
        answer[0] += 1              # '0' 없앤 횟수 + 1
        # 이전 S 개수에서 '0' 없앤 S의 개수를 뺀 값을 ans[1]에 누적
        answer[1] += len(S) - len(newStr)

        # 현재 S의 길이만큼 이진법 변화시키고 재귀 리턴
        X = len(newStr)
        XX = bin(X)[2:]
        return binary(XX)
    binary(S)
    return answer
