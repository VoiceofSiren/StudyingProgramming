'''
https://school.programmers.co.kr/learn/courses/30/lessons/181923
'''

def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        new_list = []
        for i in range(s, e+1):
            if arr[i] > k:
                new_list.append(arr[i])
        if len(new_list) == 0:
            answer.append(-1)
        else:
            answer.append(min(new_list))
    return answer

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

def str_to_2d_array(string):
    return [ list(row) for row in eval(string) ]

arr, queries = str_to_num_list(input()), str_to_2d_array(input())
print(solution(arr, queries))

'''
[0, 1, 2, 4, 3]
[[0, 4, 2],[0, 3, 2],[0, 2, 2]]
'''