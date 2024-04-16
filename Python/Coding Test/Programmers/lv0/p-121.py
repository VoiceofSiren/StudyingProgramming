'''
https://school.programmers.co.kr/learn/courses/30/lessons/181932
'''

def solution(code):
    mode = 0
    ret = ''
    for idx in range(len(code)):
        if mode == 0:
            if code[idx] != '1':
                if idx%2 == 0:
                    ret += code[idx]
            else:
                mode = 1
        else:
            if code[idx] != '1':
                if idx%2 == 1:
                    ret += code[idx]
            else:
                mode = 0
    return len(ret) == 0 and "EMPTY" or ret

code = input()
print(solution(code))

# abc1abc1abc