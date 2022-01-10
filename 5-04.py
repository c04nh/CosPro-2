# 5차 문제 4
# [5차] 문제4) 선수가 획득한 점수를 구해주세요.

def solution(taekwondo, running, shooting):
	answer = 0
	if taekwondo >= 25:
		answer += 250
	else:
		answer += taekwondo * 8
	answer += 250 + (60 - running) * 5
	count = 0
	for s in shooting:
		answer += s
		if s == 10:
			count += 1
	if count >= 7:
		answer += 100
	return answer