'''
https://school.programmers.co.kr/learn/courses/30/lessons/181877
'''

def solution(myString):
    answer = ''
    for i in range(len(myString)):
        ascii_num = ord(myString[i])
        if 97 <= ascii_num <= 122:
            ascii_num -= 32
        answer += chr(ascii_num)
    return answer

myString = input()
print(solution(myString))

# aBcDeFg