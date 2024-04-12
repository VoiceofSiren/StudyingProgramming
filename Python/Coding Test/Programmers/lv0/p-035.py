'''
https://school.programmers.co.kr/learn/courses/30/lessons/181870
'''

def solution(strArr):
    answer = []
    for s in strArr:
        if 'ad' not in s:
            answer.append(s)
    return answer

def str_to_list(string):
    return string.strip('[]').split(', ')

strArr = str_to_list(input())
print(solution(strArr))

# [and, notad, abcd]
# [there, are, no, a, ds]