# 5차 문제 7
# [5차] 문제7) 계산시간을 구해주세요!

def solution(stuffs):
	answer = 0
	small_counter, general_counter = 0, 0
	for s in stuffs:
		if s > 3:
			general_counter += s
		else:
			small_counter += s
	if small_counter > general_counter:
		answer = small_counter
	else:
		answer = general_counter
	return answer