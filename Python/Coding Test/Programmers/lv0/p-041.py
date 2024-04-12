'''
https://school.programmers.co.kr/learn/courses/30/lessons/181884
'''

def solution(numbers, n):
    answer = 0
    for i in numbers:
        answer += i
        if answer > n:
            break
    return answer

def str_to_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

numbers, n = str_to_list(input()), int(input())
print(solution(numbers, n))

# [34, 5, 71, 29, 100, 34] 123