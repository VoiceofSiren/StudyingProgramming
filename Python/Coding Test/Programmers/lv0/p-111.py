'''
https://school.programmers.co.kr/learn/courses/30/lessons/181858
'''

def solution(arr, k):
    answer = []
    for i in range(len(arr)):
        if not num_exists(answer, arr[i]):
            answer.append(arr[i])
        if k == len(answer):
            break
    return answer + [-1]*(k-len(answer))

def num_exists(num_list, n):
    result = False
    for num in num_list:
        if num == n:
            result = True
            break
    return result

def str_to_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr, k = str_to_list(input()), int(input())
print(solution(arr, k))

'''
[0, 1, 1, 2, 2, 3]
3
'''
'''
[0, 1, 1, 1, 1]
4
'''