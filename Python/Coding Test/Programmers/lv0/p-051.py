'''
https://school.programmers.co.kr/learn/courses/30/lessons/181911
'''

def solution(my_strings, parts):
    answer = ''
    for i in range(len(parts)):
        for j in range(parts[i][0], parts[i][1] + 1):
            answer += my_strings[i][j]
    return answer

def str_to_list(string):
    return string.strip('[]').split(', ')

def string_to_2darray(string):
    # 리스트 형식으로 변환
    list_data = eval(string)
    # 2차원 배열로 변환
    arr_2d = [list(row) for row in list_data]
    return arr_2d

my_strings, parts = str_to_list(input()), string_to_2darray(input())
print(solution(my_strings, parts))

# [progressive, hamburger, hammer, ahocorasick]
# [[0, 4], [1, 2], [3, 5], [7, 7]]