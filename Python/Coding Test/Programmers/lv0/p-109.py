'''
https://school.programmers.co.kr/learn/courses/30/lessons/181934
'''

def solution(ineq, eq, n, m):
    operator = get_operator(ineq, eq)
    if operator == '>=':
        return n >= m and 1 or 0
    elif operator == '<=':
        return n <= m and 1 or 0
    elif operator == '>':
        return n > m and 1 or 0
    else:
        return n < m and 1 or 0

def get_operator(ineq, eq):
    if eq == '=':
        return ineq+eq
    else:
        return ineq

ineq, eq, n, m = input().split()
n, m = int(n), int(m)
print(solution(ineq, eq, n, m))

'''
< = 20 50
> ! 41 78
'''