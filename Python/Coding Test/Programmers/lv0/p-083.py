'''
https://school.programmers.co.kr/learn/courses/30/lessons/181900
'''

def solution(my_string, indices):
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:
            answer += my_string[i]
    return answer

def str_to_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

my_string, indices = input(), str_to_list(input())
print(solution(my_string, indices))

# apporoograpemmemprs
# [1, 16, 6, 15, 0, 10, 11, 3]