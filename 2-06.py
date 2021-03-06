# 2차 문제 6
# [2차] 문제6) 엘리베이터의 총 이동거리구하기

def solution(floors):
	dist = 0
	length = len(floors)
	for i in range(1, length):
		if floors[i] > floors[i - 1]:
			dist += floors[i] - floors[i-1]
		else:
			dist += floors[i-1] - floors[i]
	return dist