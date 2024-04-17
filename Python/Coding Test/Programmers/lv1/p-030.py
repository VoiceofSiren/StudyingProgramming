'''
https://school.programmers.co.kr/learn/courses/30/lessons/12906
'''

def solution(arr):
    answer = [arr[0]]
    for i in range(1, len(arr)):
        if answer[-1] != arr[i]:
            answer.append(arr[i])
    return answer

def str_to_num_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr = str_to_num_list(input())
print(solution(arr))

# [1,1,3,3,0,1,1]
# [4,4,4,3,3]