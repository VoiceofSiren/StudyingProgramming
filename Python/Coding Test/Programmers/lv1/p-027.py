'''
https://school.programmers.co.kr/learn/courses/30/lessons/12918
'''

def solution(s):
    if len(s) in [4, 6]:
        if check_convertible(s):
            return True
        else:
            return False
    else:
        return False

def check_convertible(s):
    result = True
    for i in range(len(s)):
        if ord(s[i]) < 48 or ord(s[i]) > 57:
            result = False
    return result

s = input()
print(solution(s))

# a234
# 1234