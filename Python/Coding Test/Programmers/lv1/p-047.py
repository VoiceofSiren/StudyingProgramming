'''
https://school.programmers.co.kr/learn/courses/30/lessons/138477
'''

def solution(k, score):
    answer = []
    score_list = []
    for i in range(len(score)):
        day = i + 1
        if day <= k:
            score_list.append(score[i])
            answer.append(min(score_list))
        else:
            if score[i] <= min(score_list):
                answer.append(min(score_list))
                continue
            else:
                del score_list[score_list.index(min(score_list))]
                score_list.append(score[i])
                answer.append(min(score_list))
    return answer

k, score = int(input()), eval(input())
print(solution(k, score))

'''
3
[10, 100, 20, 150, 1, 100, 200]
'''
'''
4
[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]
'''