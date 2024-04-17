'''
https://school.programmers.co.kr/learn/courses/30/lessons/12954
'''

def solution(x, n):
    return [ x*i for i in range(1, n+1)]

x, n = map(int, input().split())
print(solution(x, n))

# 2 5
# 4 3
# -4 2