'''
https://school.programmers.co.kr/learn/courses/30/lessons/181883
'''

def solution(arr, queries):
    for query in queries:
        s, e = query
        for i in range(s, e+1):
            arr[i] += 1
    return arr

def str_to_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

def str_to_2darray(string):
    list_data = eval(string)
    return [ list(row) for row in list_data ]

arr, queries = str_to_list(input()), str_to_2darray(input())
print(solution(arr, queries))

# [0, 1, 2, 3, 4]
# [[0, 1],[1, 2],[2, 3]]