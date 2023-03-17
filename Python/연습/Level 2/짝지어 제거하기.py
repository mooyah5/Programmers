def solution(s):
    s_list = list(map(str, s))
    answer = -1
    i = 0
    while (i < len(s_list) - 1):
        if s_list[i] == s_list[i+1]:
            s_list.pop(i+1)
            s_list.pop(i)
            i = max(0, i-1)
        else:
            i += 1

    if s_list:
        answer = 0
    else:
        answer = 1
    return answer

# 시간초과
