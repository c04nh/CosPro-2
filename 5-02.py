# 5차 문제 2
# [5차] 문제2) 공강시간 구하기

def solution(time_table):
	answer = 0
	first_class = func_c(time_table)
	last_class = func_a(time_table)
	answer = func_b(time_table, first_class, last_class)
	return answer