'''
https://school.programmers.co.kr/learn/courses/30/lessons/250121
'''

def solution(data, ext, val_ext, sort_by):
    answer = []

    my_dict = {
        'code': 0,
        'date': 1,
        'maximum': 2,
        'remain': 3
    }

    for i in range(len(data)):
        if data[i][my_dict[ext]] < val_ext:
            answer.append(data[i])

    answer = sorted(answer, key=lambda x: x[my_dict[sort_by]], reverse=False)

    return answer

def str_to_2d_array(string):
    return [ list(row) for row in eval(string) ]

data, ext, val_ext, sort_by = str_to_2d_array(input()), input(), int(input()), input()
print(solution(data, ext, val_ext, sort_by))

'''
[[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]]
date
20300501
remain
'''