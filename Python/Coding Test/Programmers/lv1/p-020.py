'''
https://school.programmers.co.kr/learn/courses/30/lessons/12903?language=python3
'''

def solution(s):
    if len(s)%2 == 1:
        return s[len(s)//2]
    else:
        return s[len(s)//2-1:len(s)//2+1]

s = input()
print(solution(s))

# abcde
# qwer