'''
https://school.programmers.co.kr/learn/courses/30/lessons/12916
'''

def solution(s):
    p, y = 0, 0
    for i in range(len(s)):
        if s[i] in ['p', 'P']:
            p += 1
        elif s[i] in ['y', 'Y']:
            y += 1
    if p != y:
        return False
    else:
        return True

s = input()
print(solution(s))

# pPoooyY
# Pyy