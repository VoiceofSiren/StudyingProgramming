'''
https://school.programmers.co.kr/learn/courses/30/lessons/181893
'''

def solution(arr, query):
    for i in range(len(query)):
        if i%2 == 0:
            arr = arr[:query[i]+1]
        else:
            arr = arr[query[i]:]
    return arr

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr, query = str_to_num_list(input()), str_to_num_list(input())
print(solution(arr, query))

'''
[0, 1, 2, 3, 4, 5]
[4, 1, 2]
'''