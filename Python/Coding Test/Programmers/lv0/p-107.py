'''
https://school.programmers.co.kr/learn/courses/30/lessons/181890
'''

def solution(str_list):
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            return str_list[:i]
        elif str_list[i] == 'r':
            return str_list[i+1:]
        if not contains(str_list, 'l') and not contains(str_list, 'r'):
            return []

def contains(str_list, c):
    result = False
    for s in str_list:
        if s == c:
            result = True
    return result

def str_to_list(string):
    return string.strip('[]').split(', ')

str_list = str_to_list(input())
print(solution(str_list))

# [u, u, l, r]
# [l]