# 5차 문제 9
# [5차] 문제9) 시험 등수 구하기.

def solution(score):
	answer = [1 for a in range(len(score))]
	for a in range(len(score)):
		for b in range(len(score)):
			if score[a] < score[b]:
				answer[a] += 1
	return answer