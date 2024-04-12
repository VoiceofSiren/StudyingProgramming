'''
https://school.programmers.co.kr/learn/courses/30/lessons/181901
'''

def solution(n, k):
    return [
        i for i in range(k, n+1, k)
    ]

n, k = list(map(int, input().split()))
print(solution(n, k))

# 10 3