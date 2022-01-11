# 6차 문제 4
# [6차] 문제4) 카드뽑기 게임! (도박은 안돼요!)

def solution(cards):
	answer = 0
	cnt = [0, 0, 0]
	for i in range(len(cards)):
		if cards[i][0] == 'red':
			cnt[0] += 1
		elif cards[i][0] == 'blue':
			cnt[1] += 1
		else:
			cnt[2] += 1
		answer += int(cards[i][1])
	for item in cnt:
		if item == 3:
			answer *= 3
		elif item == 2:
			answer *= 2
	return answer