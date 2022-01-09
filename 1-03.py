# 1차 문제 3
# 시작 날짜와 끝 날짜의 사이 날짜구하기

def func_a(month, day):
    month_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0;
    for i in range(month - 1):
        total += month_list[i]
    total += day
    return total - 1
