# 요점
# 1. 같은 사람이 같은 사람을 신고한 경우가 중복되면 제거한다. (set)
# 2. ​리스트 말고 딕셔너리를 사용하여 시간을 줄인다. 아래와 같이 확연하게 줄어든다

# 정답코드 1 - 리스트

from collections import defaultdict


def solution(id_list, report, k):
    set_report = list(set(report))  # 중복 제거
    list_ = [[] for i in range(len(id_list))]
    stop_members = []
    cnt = [0 for i in range(len(id_list))]
    for r in set_report:
        a, b = r.split()
        list_[id_list.index(b)].append(a)  # 신고 당한 사람들 리스트 인덱스에 신고한 사람들 이름 넣기
    for i in range(len(list_)):
        if len(list_[i]) >= k:
            stop_members.append(id_list[i])  # 정지 당한 사람들 이름들
    for r in set_report:
        a, b = r.split()
        for name in stop_members:  # 정지 당한 사람 이름을 report에서 찾아서 신고한 사람들 인덱스에 1 추가
            if b == name:
                cnt[id_list.index(a)] += 1
    return cnt


# 정답코드 2 - 딕셔너리


def solution(id_list, report, k):

    # 중복 제거
    set_report = list(set(report))

    # value에 리스트 요소로 추가 가능한 dictionary 생성
    dict_ = defaultdict(list)

    # key : 신고 당한 유저, value : 신고한 유저 이름들
    for r in set_report:
        a, b = r.split()
        dict_[b] += [a]
    # print(dict_)

        # 답안지 딕셔너리 생성
    cnt = {}
    for id in id_list:
        cnt[id] = 0

        # 정지된 사람을 신고한 사람의 cnt 인덱스에 1 추가
    for a, b in dict_.items():
        if len(b) >= k:
            for n in b:
                cnt[n] += 1

                # cnt value 값만 출력
    return list(cnt.values())
