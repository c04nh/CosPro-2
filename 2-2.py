# 2차 문제 2
# [2차] 문제2) 더 많은 배수 구하기

def solution(arr):
	count_three = func_c(arr)
	count_five = func_a(arr)
	answer = func_b(count_three, count_five)
	return answer