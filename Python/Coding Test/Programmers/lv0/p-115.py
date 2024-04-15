'''
https://school.programmers.co.kr/learn/courses/30/lessons/181830
'''

def solution(arr):
    row, column = len(arr), len(arr[0])
    answer = [
        [ 0 for j in range(max(row, column))]
        for i in range(max(row, column))
    ]
    for i in range(row):
        for j in range(column):
            answer[i][j] = arr[i][j]
    return answer

def str_to_2d_array(string):
    return [ list(row) for row in eval(string) ]

arr = str_to_2d_array(input())
print(solution(arr))

# [[572, 22, 37], [287, 726, 384], [85, 137, 292], [487, 13, 876]]
# [[57, 192, 534, 2], [9, 345, 192, 999]]
# [[1, 2], [3, 4]]