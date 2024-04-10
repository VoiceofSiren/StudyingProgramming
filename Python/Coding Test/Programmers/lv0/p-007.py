'''
https://school.programmers.co.kr/learn/courses/30/lessons/181889
'''

def solution(num_list, n):
    answer = []
    for i in range(n):
        answer.append(int(num_list[i]))
    return answer


def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in num_list:
        i = int(i)
    return num_list

num_list = str_to_list(input())
n = int(input())
print(solution(num_list, n))
# [2, 1, 6]