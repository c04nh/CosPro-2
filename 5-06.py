# 5차 문제 6
# [5차] 문제6) 이제 수학 시험에 모든 걸 건다.

def solution(korean, english):
	answer = 0
	math = 210 - (korean + english)
	if math > 100:
		answer = -1
	else:
		answer = math
	return answer