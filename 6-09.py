# 6차 문제 9
# [6차] 문제9) 난 양말색이 달라도 잘 신는 착한 어린이

def solution(socks):
	answer = 0
	count = [0 for _ in range(10)]
	for s in socks:
		count[s] += 1
	for c in count:
		answer += (c // 2)
	return answer