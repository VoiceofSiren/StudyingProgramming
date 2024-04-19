'''
https://school.programmers.co.kr/learn/courses/30/lessons/12921?language=python3
'''

def solution(n):
    if n == 2:
        return 1
    else:
        answer = 1
        prime_numbers = [2]
        for num in range(3, n+1, 2):
            if is_prime_number(num):
                prime_numbers.append(num)
                answer += 1
        return answer

def is_prime_number(num):
    count_val = 0
    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            count_val += 1
            if count_val == 2:
                return False
    return True

n = int(input())
print(solution(n))

# 10
# 5