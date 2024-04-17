'''
https://school.programmers.co.kr/learn/courses/30/lessons/77884
'''

def solution(left, right):
    answer = 0
    for num in range(left, right+1):
        if count_factors(num)%2 == 0:
            answer += num
        else:
            answer -= num
    return answer

def count_factors(num):
    factors = 0
    for i in range(1, num+1):
        if num%i == 0:
            factors += 1
    return factors

left, right = map(int, input().split())
print(solution(left, right))

# 13 17
# 24 27