'''
https://school.programmers.co.kr/learn/courses/30/lessons/181839
'''

def solution(a, b):
    if a%2 == 1 and b%2 == 1:
        return a**2 + b**2
    elif a%2 == 0 and b%2 == 0:
        return max(a,b) - min(a,b)
    else:
        return 2*(a + b)

a, b = list(map(int, input().split()))
print(solution(a, b))

# 3 5