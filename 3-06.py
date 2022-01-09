# 3차 문제 6
# [3차] 문제6) 타일 색칠 방법 구하기

def solution(tile_length):
	answer = ''
	com = 'RRRGGB'
	if tile_length%6 == 1 or tile_length%6 == 2 or tile_length%6 == 4:
		answer = '-1'
	else:
		for i in range(tile_length):
			answer += com[i % 6]
	return answer