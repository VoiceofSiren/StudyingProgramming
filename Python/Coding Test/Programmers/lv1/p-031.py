'''
https://school.programmers.co.kr/learn/courses/30/lessons/12940
'''

def solution(n, m):
    return [calculate_gcd(n, m), calculate_lcm(n, m)]

# GCD: Greatest Common Divisor
def calculate_gcd(n, m):
    gcd = 1
    for i in range(1, min(n, m) + 1):
        if n%i == 0 and m%i == 0:
            gcd = i
    return gcd

# LCM: Lowest Common Multiple
def calculate_lcm(n, m):
    return n*m//calculate_gcd(n, m)

n, m = map(int, input().split())
print(solution(n, m))

# 3 12
# 2 5