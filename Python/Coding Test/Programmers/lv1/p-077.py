'''
https://school.programmers.co.kr/learn/courses/30/lessons/172928
'''

def solution(park, routes):

    park = [
        list(row) for row in park
    ]
    routes = [
        [route.split()[0], int(route.split()[1])] for route in routes
    ]

    #      E  S   W  N
    dx = [ 0, 1, 0, -1]
    dy = [ 1, 0, -1, 0]
    dir_dict = {
        'E': 0,
        'S': 1,
        'W': 2,
        'N': 3
    }

    x, y = 0, 0

    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                x, y = i, j

    for row in park:
        print(row)

    for route in routes:
        nx = x + dx[dir_dict[route[0]]] * route[1]
        ny = y + dy[dir_dict[route[0]]] * route[1]
        if not in_range(nx, ny, park):
            continue
        if obstacle_exists(x, y, nx, ny, park):
            continue
        x, y = nx, ny
    return [x, y]

def in_range(x, y, park):
    return 0 <= x < len(park) and 0 <= y < len(park[0])

def obstacle_exists(x, y, nx, ny, park):
    result = False
    x_start, x_end = min(x, nx), max(x, nx)
    y_start, y_end = min(y, ny), max(y, ny)
    if y_start == y_end:
        new_list = []
        for i in range(x_start, x_end + 1):
            new_list.append(park[i][y_start])
        if 'X' in new_list:
            result = True
    if x_start == x_end:
        if 'X' in park[x_start][y_start:y_end+1]:
            result = True
    return result

park, routes = eval(input()), eval(input())
print(solution(park, routes))

'''
["SOO","OOO","OOO"]
["E 2","S 2","W 1"]
'''

'''
["SOO","OXX","OOO"]
["E 2","S 2","W 1"]
'''

'''
["OSO","OOO","OXO","OOO"]
["E 2","S 3","W 1"]
'''