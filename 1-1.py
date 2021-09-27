# 단체 티셔츠를 주문하기

def solution(shirt_size):
    xs = shirt_size.count('XS')
    s = shirt_size.count('S')
    m = shirt_size.count('M')
    l = shirt_size.count('L')
    xl = shirt_size.count('XL')
    xxl = shirt_size.count('XXL')
    answer = [xs, s, m, l, xl, xxl]

    return answer