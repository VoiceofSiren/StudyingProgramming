'''
https://school.programmers.co.kr/learn/courses/30/lessons/131128
'''

def solution(X, Y):
    answer = ''
    x_list = sorted(list(X))
    y_list = sorted(list(Y))

    commons = sorted(find_commons(x_list, y_list), reverse=True)

    if len(commons) == 0:
        answer = '-1'
    else:
        for common in commons:
            answer += common

    if is_zero(answer):
        answer = '0'

    return answer

def find_commons(x_list, y_list):
    new_list = []
    x_counts, y_counts = [0] * 10, [0] * 10
    for x in x_list:
        x_counts[int(x)] += 1
    for y in y_list:
        y_counts[int(y)] += 1
    for i in range(10):
        for j in range(min(x_counts[i], y_counts[i])):
            new_list.append(str(i))
    return new_list

def is_zero(string):
    result = True
    for i in range(len(string)):
        if string[i] != '0':
            result = False
    return result

X, Y = input().split()
print(solution(X, Y))

# 100 2345
# 100 203045
# 100 123450
# 12321 42531
# 5525 1255