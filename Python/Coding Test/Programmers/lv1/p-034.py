'''
https://school.programmers.co.kr/learn/courses/30/lessons/12982
'''

def solution(d, budget):
    answer = 0
    cost = 0
    while len(d) > 0 and (cost + min(d)) <= budget:
        cost += min(d)
        del d[d.index(min(d))]
        answer += 1
    return answer

d, budget = eval(input()), int(input())
print(solution(d, budget))

'''
[1,3,2,5,4]
9
'''
'''
[2,2,3,3]
10
'''