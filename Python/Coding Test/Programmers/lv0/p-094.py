'''
https://school.programmers.co.kr/learn/courses/30/lessons/181855
'''

def solution(strArr):
    count_list = [0] * 31
    for str in strArr:
        count_list[len(str)] += 1
    return max(count_list)

def str_to_list(string):
    return string.strip('[]').split(', ')

strArr = str_to_list(input())
print(solution(strArr))

# [a, bc, d, efg, hi]