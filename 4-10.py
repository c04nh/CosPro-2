# 4차 문제 10
# [4차] 문제10) XX시험 합격자 수 구하기

def solution(scores, cutline):
	answer = 0
	for score in scores:
		if score >= cutline:
			answer += 1
	return answer