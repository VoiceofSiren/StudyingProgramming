'''
https://school.programmers.co.kr/learn/courses/30/lessons/155652
'''

def solution(s, skip, index):
    answer = ''

    for c in s:
        aci = ord(c)
        for i in range(index):
            aci = rotate(aci + 1)
            while chr(aci) in skip:
                aci = rotate(aci + 1)
        answer += chr(aci)

    return answer

def rotate(aci):
    return (aci - 97) % 26 + 97

s, skip, index = input(), input(), int(input())
print(solution(s, skip, index))

'''
aukks
wbqd
5
'''