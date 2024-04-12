'''
https://school.programmers.co.kr/learn/courses/30/lessons/181937
'''

def solution(num, n):
    return num%n == 0 and 1 or 0

num, n = list(map(int, input().split()))
print(solution(num, n))

# 98	2