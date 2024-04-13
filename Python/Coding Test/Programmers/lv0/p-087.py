'''
https://school.programmers.co.kr/learn/courses/30/lessons/181860
'''

def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            answer += [arr[i]] * (arr[i] * 2)
        else:
            answer = answer[:(-1)*arr[i]]
    return answer

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

def str_to_bool_list(string):
    bool_list = string.strip('[]').split(', ')
    for i in range(len(bool_list)):
        if bool_list[i] == 'true':
            bool_list[i] = True
        else:
            bool_list[i] = False
    return bool_list

arr, flag = str_to_num_list(input()), str_to_bool_list(input())
print(solution(arr, flag))

# [3, 2, 4, 1, 3]
# [true, false, true, false, false]