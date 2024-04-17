'''
https://school.programmers.co.kr/learn/courses/30/lessons/131705
'''

def solution(number):
    answer = 0
    for i in range(0, len(number)-2):
        for j in range(i+1, len(number)-1):
            for k in range(j+1, len(number)):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    return answer

number = eval(input())
print(solution(number))

# [-2, 3, 0, 2, -5]
# [-3, -2, -1, 0, 1, 2, 3]
# [-1, 1, -1, 1]