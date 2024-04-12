'''
https://school.programmers.co.kr/learn/courses/30/lessons/181886
'''

def solution(names):
    answer = []
    for i in range(len(names)):
        if i%5 == 0:
            answer.append(names[i])
    return answer

def str_to_list(string):
    return string.strip('[]').split(', ')

names = str_to_list(input())
print(solution(names))

# [nami, ahri, jayce, garen, ivern, vex, jinx"]