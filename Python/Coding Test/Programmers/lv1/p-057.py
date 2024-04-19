'''
https://school.programmers.co.kr/learn/courses/30/lessons/161989
'''

def solution(n, m, sections):
    answer = 0
    tiles = [0]*(n+m-1)
    for section in sections:
        tiles[section-1] = 1
    for i in range(len(tiles)):
        if tiles[i] == 1:
            for j in range(i, i + m):
                tiles[j] = 0
            answer += 1
    return answer

n, m, sections = int(input()), int(input()), eval(input())
print(solution(n, m, sections))

'''
8
4
[2, 3, 6]
'''

'''
5
4
[1, 3]
'''

'''
4
1
[1, 2, 3, 4]
'''