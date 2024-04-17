'''
https://school.programmers.co.kr/learn/courses/30/lessons/12944
'''

def solution(arr):
    return sum(arr)/len(arr)

def str_to_num_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr = str_to_num_list(input())
print(solution(arr))

# [1,2,3,4]
# [5,5]