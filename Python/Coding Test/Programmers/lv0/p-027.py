'''
https://school.programmers.co.kr/learn/courses/30/lessons/181856
'''

def solution(arr1, arr2):
    answer = 0
    if len(arr1) > len(arr2):
        answer = 1
    elif len(arr1) < len(arr2):
        answer = -1
    else:
        if sum(arr1) > sum(arr2):
            answer = 1
        elif sum(arr1) < sum(arr2):
            answer = -1
        else:
            answer = 0
    return answer

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr1, arr2 = str_to_list(input()), str_to_list(input())
print(solution(arr1, arr2))

# [49, 13] [70, 11, 2]
# [100, 17, 84, 1] [55, 12, 65, 36]
# [1, 2, 3, 4, 5] [3, 3, 3, 3, 3]