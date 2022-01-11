# 6차 문제 7
# [6차] 문제7) 의자와 책상을 사고싶어요.

def solution(money, chairs, desks):
	answer = 0
	for chair in chairs:
		for desk in desks:
			price = chair + desk
			if answer < price and money >= price:
				answer = price
	return answer