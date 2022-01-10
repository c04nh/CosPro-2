# 5차 문제 10
# [5차] 문제10) 가장 오래 일한 사람을 구해 주세요.

def solution(time_table, n):
	answer = 0
	arr = [0 for a in range(n)]
	for a in range(len(time_table)):
		arr[a % n] += time_table[a]
	answer = max(arr)
	return answer