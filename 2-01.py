# 2차 문제 1
# [2차] 문제1) 최대한 많은 쌍의 장갑 갯수 구하기

def func_a(gloves):
	counter = [0 for _ in range(max_product_number + 1)]
	for x in gloves:
		counter[x] += 1
	return counter