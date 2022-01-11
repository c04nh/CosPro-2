# 6차 문제 8
# [6차] 문제8) 주어진 수와 뒤집은 수의 차구하기

def solution(number):
	answer = 0
	digit = func_b(number)
	convert_number = func_c(number, digit)
	answer = func_a(number, convert_number)
	return answer