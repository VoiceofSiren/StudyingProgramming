'''
https://school.programmers.co.kr/learn/courses/30/lessons/1845
'''

def solution(nums):
    num_set = set()
    for num in nums:
        num_set.add(num)
    return min(len(num_set), len(nums)//2)

nums = eval(input())
print(solution(nums))

# [3,1,2,3]
# [3,3,3,2,2,4]
# [3,3,3,2,2,2]