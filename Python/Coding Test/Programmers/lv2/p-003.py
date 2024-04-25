'''
https://school.programmers.co.kr/learn/courses/30/lessons/12941?language=python3
'''

def solution(A, B):
    answer = 0

    A, B = sorted(A), sorted(B, reverse=True)
    for i in range(len(A)):
        answer += A[i]*B[i]

    return answer

A, B = eval(input()), eval(input())
print(solution(A, B))

'''
[1, 4, 2]
[5, 4, 4]
'''

'''
[1,2]
[3,4]
'''