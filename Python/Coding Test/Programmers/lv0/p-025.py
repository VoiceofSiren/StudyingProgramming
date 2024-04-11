'''
https://school.programmers.co.kr/learn/courses/30/lessons/181853
'''

def solution(num_list):
    return sorted(num_list)[:5]

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

num_list = str_to_list(input())
print(solution(num_list))

# [12, 4, 15, 46, 38, 1, 14]