'''
https://school.programmers.co.kr/learn/courses/30/lessons/181935
'''

def solution(n):
    if n%2 == 1:
        return sum([ i for i in range(1, n+1) if i%2 == 1])
    else:
        return sum([ i**2 for i in range(1, n+1) if i%2 == 0])

n = int(input())
print(solution(n))