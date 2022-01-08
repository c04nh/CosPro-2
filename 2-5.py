# 2차 문제 5
# [2차] 문제5) 몬스터 공격하기

def solution(attack, recovery, hp):
	count = 0
	while(True):
		count += 1
		hp -= attack
		if hp <= 0:
			break
		hp += recovery
	return count