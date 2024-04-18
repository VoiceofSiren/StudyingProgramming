'''
https://school.programmers.co.kr/learn/courses/30/lessons/132267
'''

def solution(a, b, n):
    answer = 0
    while n >= a:
        cola_to_return  = int(n/a)*b
        answer += cola_to_return
        n = cola_to_return + n%a
    return int(answer)

a, b, n = map(int, input().split())
print(solution(a, b, n))

# 2 1 20
# 3 1 20