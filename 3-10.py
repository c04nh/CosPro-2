# 3차 문제 10
# [3차] 문제10) 내 절반이 여기에 있는가?

def solution(arr):
	answer = 0
	for i in arr:
		if i/2 in arr:
			answer += 1
	return answer