'''
https://school.programmers.co.kr/learn/courses/30/lessons/181917
'''

def solution(x1, x2, x3, x4):
    return (x1 or x2) and (x3 or x4)

def str_to_bool_tuple(string):
    bool_list = string.split()
    for i in range(len(bool_list)):
        if bool_list[i] == 'true':
            bool_list[i] = True
        else:
            bool_list[i] = False
    return bool_list

x1, x2, x3, x4 = str_to_bool_tuple(input())
print(solution(x1, x2, x3, x4))

# false true true true
# true false false false