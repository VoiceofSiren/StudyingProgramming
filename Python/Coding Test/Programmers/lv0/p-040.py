'''
https://school.programmers.co.kr/learn/courses/30/lessons/181882
'''

def solution(arr):
    for i in range(len(arr)):
        if arr[i] >= 50 and arr[i]%2 == 0:
            arr[i] //= 2
            continue
        elif arr[i] < 50 and arr[i]%2 == 1:
            arr[i] *= 2
    return arr

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr = str_to_list(input())
print(solution(arr))

# [1, 2, 3, 100, 99, 98