# 1. 나의 노가다 풀이 (효율성 15, 16s)
def solution(S):
    answer = True
    pre = [S[0]]
    for i in range(1, len(S)):
        if S[i] == '(':
            pre.append(S[i])
        elif S[i] == ')':
            if len(pre) and pre[-1] == '(':
                pre.pop()
            else:
                return False
    if len(pre) > 0:
        return False
    return answer


# 2. 타인 풀이 (효율성 7s)
def solution(s):
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif not stack or stack.pop() != '(':
            return False
    return False if stack else True


# 3. 타인 풀이 (효율성 6s)
def solution(s):
    i = 0
    for a in s:
        if a == '(':
            i += 1
        else:
            i -= 1
        if i < 0:
            return False
    if i == 0:
        return True
    else:
        return False
    return
