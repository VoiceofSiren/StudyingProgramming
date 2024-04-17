'''
https://school.programmers.co.kr/learn/courses/30/lessons/76501
'''

def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    return answer

def str_to_num_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

def str_to_bool_list(string):
    bool_list = string.strip('[]').split(',')
    for i in range(len(bool_list)):
        if bool_list[i] == 'true':
            bool_list[i] = True
        else:
            bool_list[i] = False
    return bool_list

absolutes, signs = str_to_num_list(input()), str_to_bool_list(input())
print(solution(absolutes, signs))

'''
[4,7,12]
[true,false,true]
'''
'''
[1,2,3]
[false,false,true]
'''