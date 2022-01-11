# 6차 문제 5
# [6차] 문제5) 음료수 마시기.

def solution(money, price, n):
	answer = 0
	empty_bottle = answer = money // price
	while n <= empty_bottle:
		empty_bottle = empty_bottle - n
		answer += 1
		empty_bottle += 1
	return answer