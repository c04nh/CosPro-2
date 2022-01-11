# 6차 문제 1
# [6차] 문제1) 저는 따뜻한 날이 좋아요.

def solution(temperature, A, B):
	answer = 0
	for i in range(A, B + 1):
		if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
			answer += 1
	return answer