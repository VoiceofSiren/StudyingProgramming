'''
https://school.programmers.co.kr/learn/courses/30/lessons/181885
'''

def solution(todo_list, finished):
    answer = []
    for i in range(len(finished)):
        if not finished[i]:
            answer.append(todo_list[i])
    return answer

def str_to_list(string):
    return string.strip('[]').split(', ')

todo_list, finished = str_to_list(input()), str_to_list(input())
for i in range(len(finished)):
    if finished[i] == 'False':
        finished[i] = False
    else:
        finished[i] = True
print(solution(todo_list, finished))

# [problemsolving, practiceguitar, swim, studygraph]
# [True, False, True, False]