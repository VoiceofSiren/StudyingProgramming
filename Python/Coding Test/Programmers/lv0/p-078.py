'''
https://school.programmers.co.kr/learn/courses/30/lessons/181904
'''

def solution(my_string, m, c):
    answer = ''
    array_2d = str_to_2darray(my_string, m)
    for i in range(len(array_2d)):
        answer += array_2d[i][c-1]
    return answer

def str_to_2darray(my_string, m):
    x, y = int(len(my_string)/m), m
    array_2d = [
        [ '' for _ in range(y) ]
        for _ in range(x)
    ]
    z = 0
    for i in range(x):
        for j in range(y):
            array_2d[i][j] += my_string[z]
            z += 1
    return array_2d

my_string, m, c = input().split()
m, c = int(m), int(c)
print(solution(my_string, m, c))

# ihrhbakrfpndopljhygc 4 2
# programmers 1 1