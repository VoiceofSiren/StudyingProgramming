'''
https://school.programmers.co.kr/learn/courses/30/lessons/87389
'''

def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n%i == 1:
            answer = i
            break
    return answer

n = int(input())
print(solution(n))

# 10
# 12