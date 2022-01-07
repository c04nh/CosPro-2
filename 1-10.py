# 1차 문제 10
# [1차] 문제10) 평균 이하의 개수 구하기

def solution(data):
	total = sum(data)
	average = total / len(data)
	cnt = 0
	for d in data:
		if d < average:
			cnt += 1
	return cnt