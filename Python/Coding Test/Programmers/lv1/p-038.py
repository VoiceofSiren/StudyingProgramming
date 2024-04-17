'''
https://school.programmers.co.kr/learn/courses/30/lessons/12926
'''

def solution(s, n):
    answer = ''
    for i in range(len(s)):
        if check_blank(s[i]):
            answer += s[i]
        elif check_upper_case(s[i]):
            ascii_code = ord(s[i]) + n
            if ascii_code > 90:
                ascii_code -= 26
            answer += chr(ascii_code)
        else:
            ascii_code = ord(s[i]) + n
            if ascii_code > 122:
                ascii_code -= 26
            answer += chr(ascii_code)
    return answer

def check_blank(char):
    result = False
    if char == ' ':
        result = True
    return result

def check_lower_case(char):
    result = False
    if 97 <= ord(char) <= 122:
        result = True
    return result

def check_upper_case(char):
    result = False
    if 65 <= ord(char) <= 90:
        result = True
    return result

s, n = input(), int(input())
print(solution(s, n))

'''
AB
1
'''
'''
z
1
'''
'''
a B z
4
'''