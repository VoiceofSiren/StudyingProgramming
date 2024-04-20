'''
https://school.programmers.co.kr/learn/courses/30/lessons/64061
'''


def solution(board, moves):
    answer = 0
    basket = []
    n = len(board)
    for move in moves:
        for i in range(n):
            if board[i][move-1] > 0:
                basket.append(board[i][move-1])
                board[i][move-1] = 0
                break
        if len(basket) > 1 and basket[-2] == basket[-1]:
            basket.pop()
            basket.pop()
            answer += 2
    return answer

def str_to_2d_array(string):
    return [ list(row) for row in eval(string) ]

board, moves = str_to_2d_array(input()), eval(input())
print(solution(board, moves))

'''
[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
[1,5,3,5,1,2,1,4]
'''