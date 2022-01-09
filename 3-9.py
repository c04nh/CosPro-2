# 3차 문제 9
# [3차] 문제9) 주차장에 몇대가 들어올수 있는 거야?

def solution(day, numbers):
	count = 0
	for number in numbers:
		if number%2 == day%2:
			count += 1
	return count