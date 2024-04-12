'''
https://school.programmers.co.kr/learn/courses/30/lessons/181931
'''

def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += a + d*i
    return answer

def str_to_list(string):
    bool_list = string.strip('[]').split(', ')
    for i in range(len(bool_list)):
        if bool_list[i] == 'true':
            bool_list[i] = True
        else:
            bool_list[i] = False
    return bool_list

a, d = map(int, input().split())
included = str_to_list(input())
print(solution(a, d, included))

# 3 4
# [true, false, false, true, true]

# 7 1
# [false, false, false, true, false, false, false]