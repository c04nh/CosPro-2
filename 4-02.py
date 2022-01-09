# 4차 문제 2
# [4차] 문제2) 시험 합격자가 몇명이지?

def solution(scores):
	answer = 0
	for my_score in scores:
		passed = func_c(my_score)
		non_passed = func_b(my_score)
		answer += func_a(passed, non_passed)
	return answer