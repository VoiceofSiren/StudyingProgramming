'''
https://school.programmers.co.kr/learn/courses/30/lessons/181896
'''

def solution(num_list):
    answer = -1
    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            break
    return answer

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

num_list = str_to_list(input())
print(solution(num_list))

# [12, 4, 15, 46, 38, -2, 15]