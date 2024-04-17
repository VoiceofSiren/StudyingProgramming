'''
https://school.programmers.co.kr/learn/courses/30/lessons/12917
'''

def solution(s):
    answer = ''
    str_list = sorted(str_to_list(s), reverse=True)
    for i in range(len(str_list)):
        answer += str_list[i]
    return answer

def str_to_list(string):
    return [ char for char in string ]

s = input()
print(solution(s))

# Zbcdefg