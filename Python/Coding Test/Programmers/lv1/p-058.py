'''
https://school.programmers.co.kr/learn/courses/30/lessons/42889
'''

def solution(N, stages):
    answer, rate_list = [0] * N, [0] * N
    stages[:] = sorted(stages)
    for n in range(1, N + 1):
        update_rate_list(rate_list, n, stages)
    for n in range(1, N + 1):
        answer[n-1] = rate_list.index(max(rate_list)) + 1
        rate_list[rate_list.index(max(rate_list))] = -1
    return answer

def update_rate_list(rate_list, n, stages):
    failure_count, stages_length = stages.count(n), len(stages)
    if stages_length == 0:
        rate_list[n - 1] = 0
    elif stages.count(n) == 0:
        rate_list[n - 1] = 0
    else:
        failure_count = stages.count(n)
        stages_length = len(stages)
        stages[:] = stages[failure_count:]
        rate_list[n - 1] = failure_count / stages_length

N, stages = int(input()), eval(input())
print(solution(N, stages))

'''
5
[2, 1, 2, 6, 2, 4, 3, 3]
'''

'''
4
[4,4,4,4,4]
'''

'''
10
[2, 1, 2, 6, 2, 4, 3, 3, 5, 12, 10, 12, 6, 8, 6, 3, 1, 1, 8, 2, 12, 2]
'''
