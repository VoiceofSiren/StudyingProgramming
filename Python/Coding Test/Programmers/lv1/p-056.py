'''
https://school.programmers.co.kr/learn/courses/30/lessons/12977
'''

def solution(nums):
    answer = 0
    for i in range(0, len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                num = nums[i] + nums[j] + nums[k]
                if is_prime_number(num):
                    answer += 1
    return answer

def is_prime_number(num):
    if num <= 1:
        return True
    count_val = 0
    for i in range(1, int(num**0.5)+1):
        if num%i == 0:
            count_val += 1
            if count_val == 2:
                return False
    return True

nums = eval(input())
print(solution(nums))

# [1,2,3,4]
# [1,2,7,6,4]