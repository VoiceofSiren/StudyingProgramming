'''
https://school.programmers.co.kr/learn/courses/30/lessons/181925
'''

def solution(numLog):
    answer = ''
    for i in range(len(numLog)-1):
        diff = numLog[i + 1] - numLog[i]
        if diff == 1:
            answer += 'w'
        elif diff == -1:
            answer += 's'
        elif diff == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer

def str_to_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

numLog = str_to_list(input())
print(solution(numLog))

# [0, 1, 0, 10, 0, 1, 0, 10, 0, -1, -2, -1]