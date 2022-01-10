# 5차 문제 1
# [5차] 문제1) 사다리 게임의 승리자를 구해주세요!

def solution(ladders, win):
	answer = 0
	player = [1, 2, 3, 4, 5, 6]
	for e in ladders:
		temp = player[e[0]-1]
		player[e[0]-1] = player[e[0]]
		player[e[0]] = temp
	answer = player[win-1]
	return answer