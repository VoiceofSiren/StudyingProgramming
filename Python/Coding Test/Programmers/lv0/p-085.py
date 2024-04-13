'''
https://school.programmers.co.kr/learn/courses/30/lessons/181912
'''

def solution(intStrs, k, s, l):
    answer = []
    for i in intStrs:
        sliced_num = int(i[s:s+l])
        if sliced_num > k:
            answer.append(sliced_num)
    return answer

def str_to_list(string):
    return string.strip('[]').split(', ')

intStrs = str_to_list(input())
k, s, l = map(int, input().split())
print(solution(intStrs, k, s, l))

# [0123456789, 9876543210, 9999999999999]
# 50000 5 5