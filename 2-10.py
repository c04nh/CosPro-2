# 2차 문제 10
# [2차] 문제10) 상품권 총 지급액구하기

def solution(purchase):
	total = 0
	for p in purchase:
		if p >= 1000000:
			total += 50000
		elif p >= 600000:
			total += 30000
		elif p >= 400000:
			total += 20000
		elif p >= 200000:
			total += 10000
	return total