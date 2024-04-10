'''
https://school.programmers.co.kr/learn/courses/30/lessons/181899
'''

def solution(n, m):
    return [i for i in range(n, m - 1, -1)]

n, m = int(input()), int(input())
print(solution(n, m))