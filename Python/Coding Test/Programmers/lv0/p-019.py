'''
https://school.programmers.co.kr/learn/courses/30/lessons/181841
'''

def solution(str_list, ex):
    answer = ''
    for s in str_list:
        if ex not in s:
            answer += s
    return answer

def str_to_list(string):
    return string.strip('[]').split(', ')

str_list, ex = str_to_list(input()), input()
print(solution(str_list, ex))

# [abc, def, ghi] ef