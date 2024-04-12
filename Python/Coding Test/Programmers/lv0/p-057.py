'''
https://school.programmers.co.kr/learn/courses/30/lessons/181936
'''

def solution(number, n, m):
    return (number%n == 0 and number%m == 0) and 1 or 0

number, n, m = list(map(int, input().split()))
print(solution(number, n, m))

# 60 2 3
# 55 10 5