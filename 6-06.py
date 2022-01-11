# 6차 문제 6
# [6차] 문제6) 만드는것 보다 검사하는게 힘들죠.

def solution(password):
	capital_count, small_count, digit_count = 0, 0, 0
	for p in password:
		if p >= 'A' and p <= 'Z':
			capital_count += 1
		elif p >= 'a' and p <= 'z':
			small_count += 1
		elif p >= '0' and p <= '9':
			digit_count += 1
	if capital_count > 0 and small_count > 0 and digit_count > 0:
		answer = True
	else:
		answer = False
	return answer