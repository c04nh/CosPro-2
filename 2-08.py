# 2차 문제 8
# [2차] 문제8) 소수의 갯수 구하기

def solution(number):
	count = 0
	while number > 0:
		n = number % 10
		if n == 2 or n == 3 or n == 5 or n == 7:
			count += 1
		number //= 10
	return count