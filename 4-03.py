# 4차 문제 3
# [4차] 문제3) 획득 점수 구하기. 도박은 안돼요.

def solution(n, bundle):
	a_cards = func_a(bundle, 0)[:n]
	b_cards = func_a(bundle, 1)[:n]
	a_score = func_c(a_cards)
	b_score = func_c(b_cards)
	return func_b(a_score, b_score)