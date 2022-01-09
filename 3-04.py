# 3차 문제 4
# [3차] 문제4) 단어의 오타 수정하기

def solution(words, word):
	count = 0
	for a in words:
		for b in range(len(a)):
			if a[b] != word[b]:
				count += 1
	return count