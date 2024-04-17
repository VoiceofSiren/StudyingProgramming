'''
https://school.programmers.co.kr/learn/courses/30/lessons/12931
'''

def solution(n):
    n = str(n)
    return sum([ int(n[i]) for i in range(len(n))])

n = int(input())
print(solution(n))

# 123
# 987