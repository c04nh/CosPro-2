# 3차 문제 8
# [3차] 문제8) TV 애청자 A씨

def solution(programs):
    answer = 0
    used_tv = [0] * 25

    for program in programs:
        for i in range(program[0], program[1]):
            used_tv[i] = used_tv[i] + 1

    for i in used_tv:
        if i > 1:
            answer = answer + 1
    return answer