'''
https://school.programmers.co.kr/learn/courses/30/lessons/181909
'''

def solution(my_string):
    return sorted([
        my_string[len(my_string) - i - 1:] for i in range(len(my_string))
    ])

my_string = input()
print(solution(my_string))