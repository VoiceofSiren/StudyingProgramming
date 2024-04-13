'''
https://school.programmers.co.kr/learn/courses/30/lessons/181838
'''

def solution(date1, date2):
    y1, m1, d1 = date1
    y2, m2, d2 = date2
    if y1 < y2:
        return 1
    elif y1 == y2:
        if m1 < m2:
            return 1
        elif m1 == m2:
            if d1 < d2:
                return 1
            else:
                return 0
        else:
            return 0
    else:
        return 0

def str_to_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

date1, date2 = str_to_list(input()), str_to_list(input())
print(solution(date1, date2))

# [2021, 12, 28] [2021, 12, 29]
# [1024, 10, 24] [1024, 10, 24]