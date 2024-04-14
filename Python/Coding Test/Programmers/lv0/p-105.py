'''
https://school.programmers.co.kr/learn/courses/30/lessons/181859
'''

def solution(arr):
    stk = []
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        else:
            if stk[-1] == arr[i]:
                stk = stk[:-1]
            else:
                stk.append(arr[i])
    return len(stk) == 0 and [-1] or stk

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr = str_to_num_list(input())
print(solution(arr))

# [0, 1, 1, 1, 0]
# [0, 1, 0, 1, 0]
# [0, 1, 1, 0]