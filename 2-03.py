# 2차 문제 3
# [2차] 문제3) 짝수들의 제곱의 합 구하기

import math
def solution(N, M):
	answer = 0
	for a in range(N, M):
		if a % 2 == 0:
			answer += pow(a, 2)
	return answer