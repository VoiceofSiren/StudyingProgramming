'''
https://school.programmers.co.kr/learn/courses/30/lessons/68935
'''

def solution(n):
    answer = 0
    t = decimal_to_ternary_list(n)
    for i in range(len(t)):
        answer += t[i]*(3**i)
    return answer

# 10진수 -> 3진수
def decimal_to_ternary_list(decimal):
    ternary_list = []
    while decimal > 0:
        ternary_list.append(decimal%3)
        decimal //= 3
    return ternary_list[::-1]

n = int(input())
print(solution(n))

# 45
# 125