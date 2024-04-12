'''
https://school.programmers.co.kr/learn/courses/30/lessons/181941
'''

def solution(arr):
    answer = ''
    for i in range(len(arr)):
        answer += arr[i]
    return answer

def str_to_list(string):
    return string.strip('[]').split(', ')

arr = str_to_list(input())
print(solution(arr))

# [a, b, c]