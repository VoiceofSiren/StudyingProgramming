'''
https://school.programmers.co.kr/learn/courses/30/lessons/181831
'''

def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

def string_to_2darray(string):
    # 리스트 형식으로 변환
    list_data = eval(string)
    # 2차원 배열로 변환
    arr_2d = [list(row) for row in list_data]
    return arr_2d


arr = string_to_2darray(input())
print(solution(arr))

# [[5, 192, 33], [192, 72, 95], [33, 95, 999]]
# [[19, 498, 258, 587], [63, 93, 7, 754], [258, 7, 1000, 723], [587, 754, 723, 81]]