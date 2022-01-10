# 5차 문제 8
# [5차] 문제8) 상수도 요금 구하기.

def solution(usage):
	answer = 0
	if usage > 30:
		answer = 20 * 430 + 10 * 570 + (usage - 30) * 840
	elif usage > 20:
		answer = 20 * 430 + (usage - 20) * 570
	else:
		answer = usage * 430
	return answer