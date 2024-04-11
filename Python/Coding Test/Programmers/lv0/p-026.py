'''
https://school.programmers.co.kr/learn/courses/30/lessons/181854
'''

def solution(arr, n):
    if len(arr) % 2 == 1:
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
        for i in range(1, len(arr), 2):
            arr[i] += n
    return arr

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr, n = str_to_list(input()), int(input())
print(solution(arr, n))

# [49, 12, 100, 276, 33] 27