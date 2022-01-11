# 6차 문제 10
# [6차] 문제10) 사과 박스 무게의 불량 검사

def solution(weight, boxes):
	answer = 0
	for x in boxes:
		if x < weight * 0.9 or x > weight * 1.1:
			answer += 1
	return answer