'''
https://school.programmers.co.kr/learn/courses/30/lessons/181873
'''

def solution(my_string, alp):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] == alp:
            answer += chr(ord(alp) - 32)
        else:
            answer += my_string[i]
    return answer

my_string, alp = input().split()
print(solution(my_string, alp))

# programmers p
# lowercase x