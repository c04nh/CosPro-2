# 5차 문제 3
# [5차] 문제3) 벌금 구하기!

def solution(speed, cars):
	answer = 0
	for x in cars:
		if x >= speed * 11 / 10 and x < speed * 12 / 10:
			answer += 3
		elif x >= speed * 12 / 10 and x < speed * 13 / 10:
			answer += 5
		elif x >= speed * 13 / 10:
			answer += 7
	return answer