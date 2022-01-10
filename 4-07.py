# 4차 문제 7
# [4차] 문제7) 오른 점수와 떨어진 점수 구하기

def solution(mid_scores, final_scores):
	up = func_a(mid_scores, final_scores)
	down = func_b(final_scores, mid_scores)
	answer = [up, down]
	return answer