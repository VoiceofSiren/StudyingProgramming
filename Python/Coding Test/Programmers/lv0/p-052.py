'''
https://school.programmers.co.kr/learn/courses/30/lessons/181920
'''

def solution(start_num, end_num):
    return [ i for i in range(start_num, end_num + 1)]

start_num, end_num = list(map(int, input().split()))
print(solution(start_num, end_num))

# 3 10