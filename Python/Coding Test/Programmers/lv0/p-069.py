'''
https://school.programmers.co.kr/learn/courses/30/lessons/181898
'''

def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i
    return -1

def str_to_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr = str_to_list(input())
idx = int(input())
print(solution(arr, idx))

# [0, 0, 0, 1]
# 1