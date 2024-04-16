'''
https://school.programmers.co.kr/learn/courses/30/lessons/181832
'''

def solution(n):
    #     S  E  N   W
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x, y = 0, 0
    dir_num = 0

    answer = [
        [ 0 for j in range(n) ]
        for i in range(n)
    ]

    num = 1
    for num in range(1, n**2+1):
        answer[x][y] = num
        nx = x + dx[dir_num]
        ny = y + dy[dir_num]
        if not in_range(nx, ny) or is_checked(nx, ny, answer):
            dir_num = (dir_num + 1) % 4
            x = x + dx[dir_num]
            y = y + dy[dir_num]
            continue
        x, y = nx, ny
    return answer

def in_range(x, y):
    return 0 <= x < n and 0 <= y <n

def is_checked(x, y, arr):
    return arr[x][y] != 0

n = int(input())
print(solution(n))

# 4
# 5