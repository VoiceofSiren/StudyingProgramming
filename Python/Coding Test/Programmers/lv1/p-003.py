'''
https://school.programmers.co.kr/learn/courses/30/lessons/12928?language=python3
'''

def solution(n):
    return sum([ i for i in range(1, n+1) if n%i == 0 ])

n = int(input())
print(solution(n))

# 12
# 5