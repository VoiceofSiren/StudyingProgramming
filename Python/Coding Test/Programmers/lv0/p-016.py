'''
https://school.programmers.co.kr/learn/courses/30/lessons/181835
'''

def solution(num_list, k):
    if k % 2 == 1:
        for i in range(len(num_list)):
            num_list[i] *= k
    else:
        for i in range(len(num_list)):
            num_list[i] += k
    return num_list

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

num_list = str_to_list(input())
k = int(input())

print(solution(num_list, k))

# [1, 2, 3, 100, 99, 98] 3