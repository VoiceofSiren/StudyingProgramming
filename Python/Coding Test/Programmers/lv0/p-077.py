'''
https://school.programmers.co.kr/learn/courses/30/lessons/181919
'''

def solution(n):
    answer = [n]
    while True:
        if n%2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        answer.append(n)
        if n == 1:
            break
    return answer

n = int(input())
print(solution(n))