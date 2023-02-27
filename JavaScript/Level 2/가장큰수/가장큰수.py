def solution(numbers):
    strnbs = list(map(str, numbers))
    strnbs.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(strnbs)))
