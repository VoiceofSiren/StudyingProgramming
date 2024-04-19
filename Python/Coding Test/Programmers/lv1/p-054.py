'''
https://school.programmers.co.kr/learn/courses/30/lessons/136798
'''

def solution(number, limit, power):
    d_list = []
    for num in range(1, number+1):
        d_list.append(count_d(num))
    for i in range(len(d_list)):
        if d_list[i] > limit:
            d_list[i] = power
    return sum(d_list)

def count_d(num):
    result = 0
    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            result += 1
    return num == int(num**0.5)**2 and (2*result - 1) or 2*result

number, limit, power = map(int, input().split())
print(solution(number, limit, power))

# 5 3 2
# 10 3 2