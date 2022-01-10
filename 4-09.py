# 4차 문제 9
# [4차] 문제9) 위험한 지역 몇개인지 알려주기

def solution(height):
	count = 0
	for a in range(4):
		for b in range(4):
			if a == 0:
				if b == 0:
					if height[a][b + 1] > height[a][b] and height[a + 1][b] > height[a][b]:
						count += 1
				elif b == 3:
					if height[a][b - 1] > height[a][b] and height[a + 1][b] > height[a][b]:
						count += 1
				else:
					if height[a][b - 1] > height[a][b] and height[a][b + 1] > height[a][b] and height[a + 1][b] > height[a][b]:
						count += 1
			elif a == 3:
				if b == 0:
					if height[a][b + 1] > height[a][b] and height[a - 1][b] > height[a][b]:
						count += 1
				elif b == 3:
					if height[a][b - 1] > height[a][b] and height[a - 1][b] > height[a][b]:
						count += 1
				else:
					if height[a][b - 1] > height[a][b] and height[a][b + 1] > height[a][b] and height[a - 1][b] > height[a][b]:
						count += 1
			else:
				if b == 0:
					if height[a][b + 1] > height[a][b] and height[a - 1][b] > height[a][b] and height[a + 1][b] > height[a][b]:
						count += 1
				elif b == 3:
					if height[a][b - 1] > height[a][b] and height[a - 1][b] > height[a][b] and height[a + 1][b] > height[a][b]:
						count += 1
				else:
					if height[a][b - 1] > height[a][b] and height[a][b + 1] > height[a][b] and height[a - 1][b] > height[a][b] and height[a + 1][b] > height[a][b]:
						count += 1
	return count