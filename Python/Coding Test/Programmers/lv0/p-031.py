'''
https://school.programmers.co.kr/learn/courses/30/lessons/181864
'''

def solution(myString, pat):
    new_str = ''
    for i in range(len(myString)):
        if myString[i] == 'A':
            new_str += 'B'
            continue
        elif myString[i] == 'B':
            new_str += 'A'
            continue
        else:
            new_str += myString[i]
    return pat in new_str and 1 or 0

myString, pat = input().split()
print(solution(myString, pat))

# ABBAA AABB
# ABAB ABAB