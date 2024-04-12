'''
https://school.programmers.co.kr/learn/courses/30/lessons/181865
'''

def solution(binomial):
    a, op, b = str_to_list(binomial)
    a, b = int(a), int(b)
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return a // b

def str_to_list(string):
    return string.split()

binomial = input()
print(solution(binomial))

# 43 + 12
# 0 - 7777
# 40000 * 40000