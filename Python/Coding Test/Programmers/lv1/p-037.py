'''
https://school.programmers.co.kr/learn/courses/30/lessons/86491
'''

def solution(sizes):
    max_width, max_height = 0, 0
    for size in sizes:
        width, height = size
        max_width = max(max_width, max(width, height))
        max_height = max(max_height, min(width, height))
    return max_width * max_height

def str_to_2d_array(string):
    return [ list(row) for row in eval(string) ]

sizes = str_to_2d_array(input())
print(solution(sizes))

# [[60, 50], [30, 70], [60, 30], [80, 40]]
# [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
# [[14, 4], [19, 7], [6, 16], [18, 6], [7, 11]]