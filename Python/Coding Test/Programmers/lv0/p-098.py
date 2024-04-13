'''
https://school.programmers.co.kr/learn/courses/30/lessons/181922
'''

def solution(arr, queries):
    for query in queries:
        s, e, k = query
        for i in range(s, e+1):
            if i%k == 0:
                arr[i] += 1
    return arr

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

def str_to_2darray(string):
    list_data = eval(string)
    return [ list(row) for row in list_data ]

arr, queries = str_to_num_list(input()), str_to_2darray(input())
print(solution(arr, queries))

# [0, 1, 2, 4, 3]
# [[0, 4, 1],[0, 3, 2],[0, 3, 3]]