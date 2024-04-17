'''
https://school.programmers.co.kr/learn/courses/30/lessons/86051
'''

def solution(numbers):
    answer = 0
    digits = [ 0 for i in range(10) ]
    for num in numbers:
        digits[num] += 1
    for i in range(len(digits)):
        if digits[i] == 0:
            answer += i
    return answer

def str_to_num_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

numbers = str_to_num_list(input())
print(solution(numbers))

# [1,2,3,4,6,7,8,0]
# [5,8,4,0,6,7,9]