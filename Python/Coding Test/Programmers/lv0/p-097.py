'''
https://school.programmers.co.kr/learn/courses/30/lessons/181897
'''

def solution(n, slicer, num_list):
    a, b, c = slicer
    if n == 1:
        return num_list[:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b+1]
    else:
        return num_list[a:b+1:c]

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

n = int(input())
slicer = str_to_num_list(input())
num_list = str_to_num_list(input())
print(solution(n, slicer, num_list))

'''
3
[1, 5, 2]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''
'''
4
[1, 5, 2]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
'''