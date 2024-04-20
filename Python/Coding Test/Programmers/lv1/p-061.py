'''
https://school.programmers.co.kr/learn/courses/30/lessons/77484
'''

def solution(lottos, win_nums):
    min_count = 0
    zero_count = 0
    for i in range(6):
        if lottos[i] > 0:
            if lottos[i] in win_nums:
                min_count += 1
        else:
            zero_count += 1
    max_count = min_count + zero_count

    answer_list = [max_count, min_count]
    for i, answer in enumerate(answer_list):
        if answer <= 1:
            answer_list[i] = 6
        else:
            answer_list[i] = 7 - answer

    return answer_list

lottos, win_nums = eval(input()), eval(input())
print(solution(lottos, win_nums))

'''
[44, 1, 0, 0, 31, 25]
[31, 10, 45, 1, 6, 19]
'''

'''
[0, 0, 0, 0, 0, 0]
[38, 19, 20, 40, 15, 25]
'''

'''
[45, 4, 35, 20, 3, 9]
[20, 9, 3, 45, 4, 35]
'''