'''
https://school.programmers.co.kr/learn/courses/30/lessons/181926
'''

def solution(n, control):
    for i in range(len(control)):
        if control[i] == 'w':
            n += 1
        elif control[i] == 's':
            n -= 1
        elif control[i] == 'd':
            n += 10
        else:
            n -= 10
    return n

n, control = int(input()), input()
print(solution(n, control))

# 0 wsdawsdassw