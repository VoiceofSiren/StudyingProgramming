'''
https://school.programmers.co.kr/learn/courses/30/lessons/181929
'''

def solution(num_list):
    v1, v2 = 1, 0
    for num in num_list:
        v1 *= num
        v2 += num
    v2 **= 2
    return v1 < v2 and 1 or 0

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

num_list = str_to_list(input())
print(solution(num_list))

# [3, 4, 5, 2, 1]