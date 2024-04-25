'''
https://school.programmers.co.kr/learn/courses/30/lessons/12909
'''

def solution(s):
    answer = True
    s = list(s)

    stack_list = list()
    for element in s:
        stack_list.append(element)
        if len(stack_list) > 1:
            if stack_list[-2:] == ['(', ')']:
                stack_list.pop()
                stack_list.pop()

    if len(stack_list) > 0:
        answer = False

    return answer

s = eval(input())
print(solution(s))

# "()()"
# "(())()"
# ")()("
# "(()("