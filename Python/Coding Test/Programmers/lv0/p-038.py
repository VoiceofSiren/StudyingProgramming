'''
https://school.programmers.co.kr/learn/courses/30/lessons/181875
'''

def solution(strArr):
    answer = []
    for i in range(len(strArr)):
        if i % 2 == 0:
            answer.append(to_lower_case(strArr[i]))
        else:
            answer.append(to_upper_case(strArr[i]))
    return answer


def str_to_list(string):
    return string.strip('[]').split(', ')

def to_lower_case(string):
    new_string = ''
    for i in range(len(string)):
        if 65 <= ord(string[i]) <= 90:
            new_string += chr(ord(string[i]) + 32)
        else:
            new_string += string[i]
    return new_string

def to_upper_case(string):
    new_string = ''
    for i in range(len(string)):
        if 97 <= ord(string[i]) <= 122:
            new_string += chr(ord(string[i]) - 32)
        else:
            new_string += string[i]
    return new_string

strArr = str_to_list(input())
print(solution(strArr))

# [AAA, BBB, CCC, DDD]
# [aBc, AbC]