'''
https://school.programmers.co.kr/learn/courses/30/lessons/181844
'''

def solution(arr, delete_list):
    answer = []
    for num in arr:
        if num not in delete_list:
            answer.append(num)
    return answer

def str_to_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list


arr, delete_list = str_to_list(input()), str_to_list(input())
print(solution(arr, delete_list))

# [293, 1000, 395, 678, 94]
# [94, 777, 104, 1000, 1, 12]