'''
https://school.programmers.co.kr/learn/courses/30/lessons/181837
'''

def solution(order):
    cost = 0
    for o in order:
        if o.find('americano') != -1:
            cost += 4500
        elif o.find('cafelatte') != -1:
            cost += 5000
        else:
            cost += 4500
    return cost

def str_to_num_list(string):
    return string.strip('[]').split(', ')

order = str_to_num_list(input())
print(solution(order))

# [cafelatte, americanoice, hotcafelatte, anything]
# [americanoice, americano, iceamericano]