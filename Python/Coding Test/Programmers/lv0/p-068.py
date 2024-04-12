'''
https://school.programmers.co.kr/learn/courses/30/lessons/181895
'''

def solution(arr, intervals):
    return arr[intervals[0][0]:intervals[0][1]+1] + arr[intervals[1][0]:intervals[1][1]+1]

def str_to_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

def string_to_2darray(string):
    # 리스트 형식으로 변환
    list_data = eval(string)
    # 2차원 배열로 변환
    arr_2d = [list(row) for row in list_data]
    return arr_2d

arr, intervals = str_to_list(input()), string_to_2darray(input())
print(solution(arr, intervals))

# [1, 2, 3, 4, 5]
# [[1, 3], [0, 4]]