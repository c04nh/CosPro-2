# 4차 문제 4
# [4차] 문제4) 조교의 수 구하기.

def solution(classes, m):
	answer = 0
	for students in classes:
		answer += students // m
		if students % m != 0:
			answer += 1
	return answer