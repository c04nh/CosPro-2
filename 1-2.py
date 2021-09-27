# 1차 문제 2
# 쇼핑몰 등급별 할인 금액구하기

import math

def solution(price, grade):
    answer = 0
    if grade == 'S':
        answer = price * 0.95
    elif grade == 'G':
        answer = price * 0.9
    elif grade == 'V':
        answer = price * 0.85
    answer = math.floor(answer)
    return answer
