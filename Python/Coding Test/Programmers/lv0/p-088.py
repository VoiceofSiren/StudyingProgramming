'''
https://school.programmers.co.kr/learn/courses/30/lessons/181857
'''

def solution(arr):
    zero_to_add = 1000
    for i in range(11):
        if 2**i < len(arr):
            continue
        zero_to_add = min(2**i - len(arr), zero_to_add)
    arr += [0] * zero_to_add
    return arr

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr = str_to_num_list(input())
print(solution(arr))

# [1, 2, 3, 4, 5, 6]
# [58, 172, 746, 89]