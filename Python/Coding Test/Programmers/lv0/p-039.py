'''
https://school.programmers.co.kr/learn/courses/30/lessons/181878
'''

def solution(myString, pat):
    return to_lower_case(pat) in to_lower_case(myString) and 1 or 0

def to_lower_case(string):
    new_string = ''
    for i in range(len(string)):
        if 65 <= ord(string[i]) <= 90:
            new_string += chr(ord(string[i]) + 32)
        else:
            new_string += string[i]
    return new_string

myString, pat = input().split()
print(solution(myString, pat))


# AbCdEfG aBc
# aaAA aaaaa