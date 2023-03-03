# i, j로 각 배열 길이만큼 for문을 돌아 순회하면서
# i = j일 때를 제외하고 i+j 를 answer에 더해준다.
def solution(n):
    answer = []
    for i in range(len(n)):
        for j in range(len(n)):
            if i != j:
                answer.append(n[i] + n[j])
    answer = sorted(list(set(answer)))
    return answer
