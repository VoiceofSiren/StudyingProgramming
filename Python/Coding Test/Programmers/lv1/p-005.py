'''
https://school.programmers.co.kr/learn/courses/30/lessons/12932
'''

def solution(n):
    n = str(n)
    return [ int(n[i]) for i in range(len(n))][::-1]

n = int(input())
print(solution(n))

# 12345