# 1차 문제 5
# [1차] 문제5) 배열의 순서 뒤집기

def solution(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
