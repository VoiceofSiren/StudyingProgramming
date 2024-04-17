'''
https://school.programmers.co.kr/learn/courses/30/lessons/12910
'''

def solution(arr, divisor):
    answer = []
    for num in arr:
        if num%divisor == 0:
            answer.append(num)
    return len(answer)>0 and sorted(answer) or [-1]

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr, divisor = str_to_num_list(input()), int(input())
print(solution(arr, divisor))

# [5, 9, 7, 10] 5
# [2, 36, 1, 3] 1
# [3, 2, 6] 10