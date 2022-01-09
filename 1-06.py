# 1차 문제 6
# [1차] 문제6) 369 게임 박수의 갯수 구하기

def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        while current != 0:
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:
                count += 1
            current = current // 10
    return count
