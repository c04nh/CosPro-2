# 5차 문제 5
# [5차] 문제5) n일장이 함께 열리는 날은 언제인가요.

def solution(a, b):
	answer = 0
	for i in range(1, b + 1):
		if (a * i) % b == 0:
			answer = a * i
			break
	return answer