'''
https://school.programmers.co.kr/learn/courses/30/lessons/181918
'''

def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if len(stk) == 0:
            stk.append(arr[i])
            i += 1
        else:
            if stk[-1] >= arr[i]:
                stk = stk[:-1]
            else:
                stk.append(arr[i])
                i += 1
    return stk

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr = str_to_num_list(input())
print(solution(arr))

# [1, 4, 2, 5, 3]