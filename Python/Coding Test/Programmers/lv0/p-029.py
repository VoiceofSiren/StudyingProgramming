'''
https://school.programmers.co.kr/learn/courses/30/lessons/181863
'''

def solution(rny_string):
    answer = ''
    for i in range(len(rny_string)):
        if rny_string[i] == 'm':
            answer += 'rn'
        else:
            answer += rny_string[i]
    return answer

rny_string = input()
print(solution(rny_string))

# masterpiece