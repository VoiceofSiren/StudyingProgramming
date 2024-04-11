'''
https://school.programmers.co.kr/learn/courses/30/lessons/181843
'''

def solution(my_string, target):
    return target in my_string and 1 or 0

my_string, target = input().split()
print(solution(my_string, target))

# banana ana
# banana wxyz