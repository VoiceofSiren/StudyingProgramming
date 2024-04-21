'''
https://school.programmers.co.kr/learn/courses/30/lessons/161990
'''

def solution(wallpaper):

    lux, luy, rdx, rdy = 0, 0, 0, 0
    for i in range(len(wallpaper)):
        if list(wallpaper[i]).count('#') > 0:
            lux = i
            break

    for i in range(len(wallpaper)):
        if list(wallpaper[len(wallpaper)-i-1]).count('#') > 0:
            rdx = len(wallpaper)-i-1
            break

    wallpaper = reverse_2d_array(wallpaper)
    for i in range(len(wallpaper)):
        if list(wallpaper[i]).count('#') > 0:
            luy = i
            break

    for i in range(len(wallpaper)):
        if list(wallpaper[len(wallpaper)-i-1]).count('#') > 0:
            rdy = len(wallpaper)-i-1
            break

    answer = [lux, luy, rdx+1, rdy+1]
    return answer

def reverse_2d_array(wallpaper):
    len_x, len_y = len(wallpaper), len(wallpaper[0])
    new_2d_array = [
        ['' for _ in range(len_x)]
        for _ in range(len_y)
    ]
    for i in range(len(wallpaper)):
        wallpaper[i] = list(wallpaper[i])

    for i in range(len_y):
        for j in range(len_x):
            new_2d_array[i][j] += wallpaper[j][i]

    return new_2d_array



wallpaper = eval(input())
print(solution(wallpaper))
# [".#...", "..#..", "...#."]
# ["..........", ".....#....", "......##..", "...##.....", "....#....."]
# [".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."]
# ["..", "#."]