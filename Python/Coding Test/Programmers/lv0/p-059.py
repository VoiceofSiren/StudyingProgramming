'''
https://school.programmers.co.kr/learn/courses/30/lessons/181939
'''

def solution(a, b):
    return max(operate(a, b), operate(b, a))

def operate(a, b):
    return int(str(a) + str(b))

a, b = list(map(int, input().split()))
print(solution(a, b))

# 9 91
# 89 8