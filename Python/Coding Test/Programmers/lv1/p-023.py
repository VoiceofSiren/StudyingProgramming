'''
https://school.programmers.co.kr/learn/courses/30/lessons/70128
'''

def solution(a, b):
    answer = 0
    n = len(a)
    for i in range(n):
        answer += a[i]*b[i]
    return answer

def str_to_num_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

a, b = str_to_num_list(input()), str_to_num_list(input())
print(solution(a, b))

'''
[1,2,3,4]
[-3,-1,0,2]
'''
'''
[-1,0,1]
[1,0,-1]
'''