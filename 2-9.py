# 2차 문제 9
# [2차] 문제9) 투표에 대한 후보 찾기

def solution(votes, N, K):
	counter = [0 for _ in range(N + 1)]
	for x in votes:
		counter[x] += 1
	answer = 0
	for c in counter:
		if c == K:
			answer += 1
	return answer