'''
https://school.programmers.co.kr/learn/courses/30/lessons/181874
'''

def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if myString[i] == 'a':
            answer += 'A'
            continue
        elif 66 <= ord(myString[i]) <= 90:
            answer += chr(ord(myString[i]) + 32)
        else:
            answer += myString[i]
    return answer

myString = input()
print(solution(myString))

# abstract algebra