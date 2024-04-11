'''
https://school.programmers.co.kr/learn/courses/30/lessons/181861
'''

def solution(arr):
    answer = []
    for elem in arr:
        for e in range(elem):
            answer.append(elem)
    return answer

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr = str_to_list(input())
print(solution(arr))

# [5, 1, 4]