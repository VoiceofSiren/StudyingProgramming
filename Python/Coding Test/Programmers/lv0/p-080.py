'''
https://school.programmers.co.kr/learn/courses/30/lessons/181829
'''

def solution(board, k):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i + j <= k:
                answer += board[i][j]
    return answer

def str_to_2darray(string):
    list_data = eval(string)
    return [ list(row) for row in list_data]

board = str_to_2darray(input())
k = int(input())
print(solution(board, k))

# [[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]]