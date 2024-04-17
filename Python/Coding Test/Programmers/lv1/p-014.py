'''
https://school.programmers.co.kr/learn/courses/30/lessons/12919?language=python3
'''

def solution(seoul):
    idx = 0
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            idx = i
            break
    return f"김서방은 {idx}에 있다"

def str_to_list(string):
    return string.strip('[]').split(', ')

seoul = str_to_list(input())
print(solution(seoul))

# [Jane, Kim]