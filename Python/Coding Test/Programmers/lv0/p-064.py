'''
https://school.programmers.co.kr/learn/courses/30/lessons/181834
'''

def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if ord(myString[i]) < ord('l'):
            answer += 'l'
            continue
        else:
            answer += myString[i]
    return answer

myString = input()
print(solution(myString))

# abcdevwxyz
# jjnnllkkmm