'''
https://school.programmers.co.kr/learn/courses/30/lessons/181879
'''

def solution(num_list):
    if len(num_list) >= 11:
        answer = 0
        for i in num_list:
            answer += int(i)
        return answer
    else:
        answer = 1
        for i in num_list:
            answer *= int(i)
        return answer

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

num_list = str_to_list(input())

print(solution(num_list))
# [3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]