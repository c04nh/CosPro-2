# 2차 문제 7
# [2차] 문제7) 섭씨, 화씨 온도 바꾸기

def solution(value, unit):
	converted = 0
	if unit == "C":
		value = value * 1.8 + 32
	if unit == "F":
		value = (value - 32) / 1.8
	converted = int(value)
	return converted