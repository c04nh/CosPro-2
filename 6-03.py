# 6차 문제 3
# [6차] 문제3) 단체 유니폼 맞추기

def solution(people):
	answer = [0 for _ in range(4)]
	for person in people:
		if person < 95:
			answer[0] += 1
		elif person < 100:
			answer[1] += 1
		elif person < 105:
			answer[2] += 1
		else:
			answer[3] += 1
	return answer