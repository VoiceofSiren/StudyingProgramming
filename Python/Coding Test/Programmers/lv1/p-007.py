'''
https://school.programmers.co.kr/learn/courses/30/lessons/12934
'''

def solution(n):
    root = int(n**0.5)
    if n == root**2:
        return (root + 1)**2
    else:
        return -1

n = int(input())
print(solution(n))

# 121
# 3