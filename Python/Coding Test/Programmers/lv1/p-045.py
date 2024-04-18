'''
https://school.programmers.co.kr/learn/courses/30/lessons/134240
'''

def solution(food):
    answer = ''
    for i in range(1, len(food)):
        for j in range(food[i]//2):
            answer += str(i)
    return answer + '0' + answer[::-1]

food = eval(input())
print(solution(food))

# [1, 3, 4, 6]
# [1, 7, 1, 2]