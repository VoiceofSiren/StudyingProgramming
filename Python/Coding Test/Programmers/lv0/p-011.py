'''
https://school.programmers.co.kr/learn/courses/30/lessons/181938
'''

'''
def solution(a, b):
    if sum_func(a, b) >= mul_func(a, b):
        return sum_func(a, b)
    else:
        return mul_func(a, b)
'''
def solution(a, b):
    if sum_func(a, b) >= mul_func(a, b):
        return sum_func(a, b)
    else:
        return mul_func(a, b)

def my_func(b):
    value = 1
    while b > 0:
        b //= 10
        value *= 10
    return value

def sum_func(a, b):
    return a * my_func(b) + b

def mul_func(a, b):
    return 2 * a * b

a, b = int(input()), int(input())
print(solution(a, b))