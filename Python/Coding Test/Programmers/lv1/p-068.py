'''
https://school.programmers.co.kr/learn/courses/30/lessons/250125
'''

def solution(board, h, w):
    answer = 0
    #      E  S   W  N
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dir_num = 0
    x, y = h, w
    color = board[x][y]

    for dir_num in range(4):
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if not in_range(nx, ny, board):
            continue
        if board[nx][ny] == color:
            answer += 1
    return answer

def in_range(x, y, board):
    return 0 <= x < len(board) and 0 <= y < len(board)

board, h, w = eval(input()), int(input()), int(input())
print(solution(board, h, w))

'''
[["blue", "red", "orange", "red"], ["red", "red", "blue", "orange"], ["blue", "orange", "red", "red"], ["orange", "orange", "red", "blue"]]
1
1
'''

'''
[["yellow", "green", "blue"], ["blue", "green", "yellow"], ["yellow", "blue", "blue"]]
0
1
'''