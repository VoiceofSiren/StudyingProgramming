'''
https://school.programmers.co.kr/learn/courses/30/lessons/181880
'''

def solution(num_list):
    answer = 0
    for num in num_list:
        answer += count_operation(num)
    return answer

def count_operation(num):
    count = 0
    while True:
        if num == 1:
            break
        if num%2 == 0:
            num //= 2
        else:
            num = int((num-1)/2)
        count += 1
    return count

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

num_list = str_to_num_list(input())
print(solution(num_list))

# [12, 4, 15, 1, 14]