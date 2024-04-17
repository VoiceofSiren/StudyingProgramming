'''
https://school.programmers.co.kr/learn/courses/30/lessons/82612
'''

def solution(price, money, count):
    answer = (-1) * money
    for c in range(1, count+1):
        answer += price * c
    return answer > 0 and answer or 0

price, money, count = map(int, input().split())
print(solution(price, money, count))

# 3 20 4