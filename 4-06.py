# 4차 문제 6
# [4차] 문제6) 열심히 모은 point, 돌려드립니다.

def solution(point):
	if point < 1000:
		return 0
	return point // 100 * 100