def solution(array):
    arr = [0 for i in range(1000)]
    for a in array:
        arr[a] += 1
    maxArr = max(arr)
    lst = [i for i, v in enumerate(arr) if v == maxArr]
    if len(lst) > 1:
        answer = -1
    else:
        answer = arr.index(maxArr)
    return answer
# enumerate는 인덱스와 원소를 동시에 알 수 있는 내장함수로,
# 최댓값에 해당하는 원소가 몇 개, 어느 인덱스에 있는지 알 수 있다.
