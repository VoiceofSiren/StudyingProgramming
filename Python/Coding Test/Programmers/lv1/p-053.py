'''
https://school.programmers.co.kr/learn/courses/30/lessons/135808
'''

def solution(k, m, scores):
    answer = 0
    sorted_apples = sorted(scores, reverse=True)[:len(scores)-len(scores)%m]
    for i in range(0, len(sorted_apples), m):
        answer += min(sorted_apples[i:i+m])*m
    return answer

k, m, scores = int(input()), int(input()), eval(input())
print(solution(k, m, scores))

'''
3
4
[1, 2, 3, 1, 2, 3, 1]
'''
'''
4
3
[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
'''