'''
https://school.programmers.co.kr/learn/courses/30/lessons/181887
'''

def solution(num_list):
    sum1, sum2 = 0, 0
    for i in range(len(num_list)):
        if i%2 == 0:
            sum1 += num_list[i]
        else:
            sum2 += num_list[i]
    return max(sum1, sum2)

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

num_list = str_to_list(input())
print(solution(num_list))

# [4, 2, 6, 1, 7, 6]