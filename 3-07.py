# 3차 문제 7
# [3차] 문제7) 남은 재료로 주스 만들기

def solution(num_apple, num_carrot, k):
	answer = 0

	if num_apple < (3 * num_carrot):
		answer = num_apple // 3
	else:
		answer = num_carrot

	num_apple -= answer * 3
	num_carrot -= answer

	i = 0
	k = k - (num_apple + num_carrot)

	while k > 0:
		if i % 4 == 0:
			answer = answer - 1
		i = i + 1
		k = k - 1

	return answer