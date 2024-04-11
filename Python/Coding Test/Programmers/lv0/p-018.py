'''
https://school.programmers.co.kr/learn/courses/30/lessons/181840
'''

def solution(num_list, n):
    if num_list.count(n) == 0:
        return 0
    else:
        return 1

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

num_list = str_to_list(input())
n = int(input())

print(solution(num_list, n))

# [1, 2, 3, 4, 5] 3