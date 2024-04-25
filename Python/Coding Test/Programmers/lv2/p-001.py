'''
https://school.programmers.co.kr/learn/courses/30/lessons/12939
'''

def solution(s):
    s = list(map(int, s.split()))
    answer = str(min(s)) + ' ' + str(max(s))
    return answer

s = eval(input())
print(solution(s))

'''
"1 2 3 4"
'''

'''
"-1 -2 -3 -4"
'''

'''
"-1 -1"
'''