# 3차 문제 2
# [3차] 문제2) 장학생 수 구하기

def solution(current_grade, last_grade):
	rank = func_b(current_grade)
	max_diff_grade = func_c(current_grade, last_grade)
	answer = func_a(current_grade, last_grade, rank, max_diff_grade)
	return answer