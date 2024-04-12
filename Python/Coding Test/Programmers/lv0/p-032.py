'''
https://school.programmers.co.kr/learn/courses/30/lessons/181867
'''

def solution(myString):
    answer = []
    new_list = myString.split('x')
    for elem in new_list:
        answer.append(len(elem))
    return answer

myString = input()
print(solution(myString))

# oxooxoxxox