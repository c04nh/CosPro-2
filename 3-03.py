# 3차 문제 3
# [3차] 문제3) 체조 선수의 점수 구해주기

def solution(scores):
	answer = 0
	answer = (sum(scores) - max(scores) - min(scores)) / (len(scores) - 2)
	answer = int(answer)
	return answer