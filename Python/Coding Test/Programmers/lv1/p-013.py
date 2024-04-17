'''
https://school.programmers.co.kr/learn/courses/30/lessons/12912
'''

def solution(a, b):
    a, b = min(a, b), max(a, b)
    return sum([ i for i in range(a, b+1) ])

a, b = map(int, input().split())
print(solution(a, b))

# 3 5
# 3 3
# 5 3