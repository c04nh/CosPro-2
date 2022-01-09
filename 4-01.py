# 4차 문제 1
# [4차] 문제1) 상담 선생님은 너무 바빠요

def solution(schedule):
	answer = []
	for idx, i in enumerate(schedule):
		if i == 'X':
			answer.append(idx + 1)
	return answer