'''
https://school.programmers.co.kr/learn/courses/30/lessons/142086
'''

def solution(s):
    answer = []
    str_list = []
    for i, char in enumerate(s):
        if char not in str_list:
            answer.append(-1)
            str_list.append(char)
        else:
            for j, c in enumerate(str_list[::-1]):
                if char == c:
                    answer.append(j+1)
                    str_list.append(char)
                    break
    return answer

s = input()
print(solution(s))

# banana
# foobar