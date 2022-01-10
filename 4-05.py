# 4차 문제 5
# [4차] 문제5) A씨의 추가 운동 여부 알려주기

def solution(calorie):
	min_cal = calorie[0]
	answer = 0
	for cal in calorie:
		if cal > min_cal:
			answer += cal - min_cal
		min_cal = min(min_cal, cal)
	return answer