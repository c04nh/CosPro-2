# 1차 문제 9
# [1차] 문제9) 중복문자 삭제하기

def solution(characters):
	result = ""
	result += characters[0]
	for i in range(1, len(characters)):
		if characters[i - 1] != characters[i]:
			result += characters[i]
	return result