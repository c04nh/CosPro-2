# 1차 문제 8
# [1차] 문제8) 팰린드롬 판단하기

def solution(sentence):
	str = ''
	for c in sentence:
		if c != '.' and c != ' ':
			str += c
	size = len(str)
	for i in range(size // 2):
		if str[i] != str[size - 1 - i]:
			return False
	return True