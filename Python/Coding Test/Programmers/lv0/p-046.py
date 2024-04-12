'''
https://school.programmers.co.kr/learn/courses/30/lessons/181891
'''

def solution(num_list, n):
    return num_list[n:] + num_list[:n]

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

num_list, n = str_to_list(input()), int(input())
print(solution(num_list, n))

# [2, 1, 6] 1