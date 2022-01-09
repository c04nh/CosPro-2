# 3차 문제 1
# [3차] 문제1) 학생의 등수 구하기

def solution(scores, n):
	score = func_c(scores, n)
	func_b(scores)
	answer = func_a(scores, score)
	return answer