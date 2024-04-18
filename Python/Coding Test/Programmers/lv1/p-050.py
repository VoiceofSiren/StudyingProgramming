'''
https://school.programmers.co.kr/learn/courses/30/lessons/12901
'''

def solution(a, b):
    week_days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = 0
    for i in range(1, a):
        total_days += month_days[i-1]
    total_days += b-1
    return week_days[(5+total_days)%7]

a, b = map(int, input().split())
print(solution(a, b))

# 5 24