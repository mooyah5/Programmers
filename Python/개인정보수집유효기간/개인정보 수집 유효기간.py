from datetime import datetime


def solution(today, terms, privacies):
    answer = []
    terms_data = dict([tuple(item.split()) for item in terms])
    splited_privacies = [i.split() for i in privacies]
    for i in range(len(splited_privacies)):
        date, expiration_period = splited_privacies[i][0], splited_privacies[i][1]
        print(date, expiration_period)
        add = int(terms_data.get(expiration_period))    # 더할 유효기간
        YYYY, MM, DD = map(int, date.split('.'))        # 날짜를 년, 월, 일 숫자로 분리

        # 유효기간 더하기
        # #1. DD: 1일이면 28일로 변경 후 MM - 1, 그 외는 DD - 1
        # if DD == 1:
        #     DD = 28
        #     MM -= 1
        # else:
        #     DD -= 1
        # 2. MM: MM+유효기간이 12 초과하면 12로 나눈 값은 Y에, 나머지는 M에 더하기
        MM += add
        if MM > 12:
            YYYY += MM // 12
            if MM % 12 == 0:
                MM = 1
                # YYYY -= 1
            else:
                MM = MM % 12
        print('답', YYYY, MM, DD)

        DT, TodayDT = datetime(
            YYYY, MM, DD), datetime.strptime(today, '%Y.%m.%d')
        print(i, '_', '비교', DT, '오늘', TodayDT)
        if TodayDT >= DT:
            print('초과', i+1)
            answer.append(i+1)

    return answer
