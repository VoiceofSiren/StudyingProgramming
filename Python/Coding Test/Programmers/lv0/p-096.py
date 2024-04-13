'''
https://school.programmers.co.kr/learn/courses/30/lessons/181894
'''

def solution(arr):
    if get_first_index(arr) == -1:
        return [-1]
    else:
        return arr[get_first_index(arr):get_last_index(arr)+1]

def get_first_index(arr):
    index = -1
    for i in range(len(arr)):
        if arr[i] == 2:
            index = i
            break
    return index

def get_last_index(arr):
    index = -1
    arr = arr[::-1]
    for i in range(len(arr)):
        if arr[i] == 2:
            index = i
            break
    return len(arr) - index - 1

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr = str_to_num_list(input())
print(solution(arr))

# [1, 2, 1, 4, 5, 2, 9]