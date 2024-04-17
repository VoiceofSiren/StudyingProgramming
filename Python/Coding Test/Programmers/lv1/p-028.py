'''
https://school.programmers.co.kr/learn/courses/30/lessons/12950?language=python3
'''

def solution(arr1, arr2):
    row, column = len(arr1), len(arr1[0])
    answer = [
        [ 0 for _ in range(column) ]
        for _ in range(row)
    ]
    for i in range(row):
        for j in range(column):
            answer[i][j] = arr1[i][j] + arr2[i][j]
    return answer

def str_to_2d_array(string):
    return [ list(row) for row in eval(string) ]

arr1, arr2 = str_to_2d_array(input()), str_to_2d_array(input())
print(solution(arr1, arr2))

'''
[[1,2],[2,3]]
[[3,4],[5,6]]
'''
'''
[[1],[2]]
[[3],[4]]
'''