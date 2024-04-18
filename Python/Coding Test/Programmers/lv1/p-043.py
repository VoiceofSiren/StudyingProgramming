'''
https://school.programmers.co.kr/learn/courses/30/lessons/42748
'''

def solution(array, commands):
    answer = []
    for command in commands:
        i, j, k = command
        answer.append(sorted(array[i-1:j])[k-1])
    return answer

array, commands = eval(input()), eval(input())
print(solution(array, commands))

'''
[1, 5, 2, 6, 3, 7, 4]
[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
'''