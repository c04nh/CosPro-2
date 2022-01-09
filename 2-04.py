# 2차 문제 4
# [2차] 문제4) 5글자 이상인 단어 배열하기

def solution(words):
	answer = ''
	for word in words:
		if len(word) >= 5:
			answer += word
	if answer == '':
		answer = 'empty'
	return answer