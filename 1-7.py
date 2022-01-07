# 1차 문제 7
# [1차] 문제7) 영어 수강 대상자 수 구하기

def solution(scores):
	count = 0
	for s in scores:
		if 650 <= s and s < 800:
			count += 1
	return count