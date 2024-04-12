'''
https://school.programmers.co.kr/learn/courses/30/lessons/181930
'''

def solution(a, b, c):
    answer = 1
    num = condition(a, b, c)
    for i in range(1, num + 1):
        answer *= sum_squares(a, b, c, i)
    return answer

def condition(a, b, c):
    if a!=b and b!=c and c!=a:
        return 1
    elif a==b==c:
        return 3
    else:
        return 2

def sum_squares(a, b, c, num):
    return a**num + b**num + c**num

a, b, c = list(map(int, input().split()))
print(solution(a, b, c))

# 2 6 1
# 5 3 3
# 4 4 4