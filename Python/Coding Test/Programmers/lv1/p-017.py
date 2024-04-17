'''
https://school.programmers.co.kr/learn/courses/30/lessons/12943?language=python3
'''

def solution(num):
    answer = 0
    while num > 1:
        if answer == 500:
            answer = -1
            break
        if num%2 == 0:
            num //= 2
        else:
            num = num*3 + 1
        answer += 1
    return answer

num = int(input())
print(solution(num))

# 6
# 16
# 626331