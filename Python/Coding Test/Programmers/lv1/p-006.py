'''
https://school.programmers.co.kr/learn/courses/30/lessons/12933
'''

def solution(n):
    n = str(n)
    reverse_list = sorted([ n[i] for i in range(len(n)) ], reverse=True)
    answer = ''
    for r in reverse_list:
        answer += r
    return int(answer)

n = int(input())
print(solution(n))

# 118372