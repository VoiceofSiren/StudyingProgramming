'''
https://school.programmers.co.kr/learn/courses/30/lessons/181866
'''

def solution(myString):
    old_list = sorted(myString.split('x'))
    new_list = [
        s for s in old_list if s != ''
    ]
    return new_list

myString = input()
print(solution(myString))

# axbxcxdx