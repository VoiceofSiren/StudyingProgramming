'''
https://school.programmers.co.kr/learn/courses/30/lessons/181928
'''

def solution(num_list):
    odd, even = '', ''
    for num in num_list:
        if num % 2 == 1:
            odd += str(num)
        else:
            even += str(num)
    return int(odd) + int(even)

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

num_list = str_to_list(input())
print(solution(num_list))

# [3, 4, 5, 2, 1]