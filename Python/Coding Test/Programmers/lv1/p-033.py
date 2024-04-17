'''
https://school.programmers.co.kr/learn/courses/30/lessons/12930
'''

def solution(s):
    str_list = s.split(' ')
    word_list = [ '' for _ in range(len(str_list)) ]
    for i, word in enumerate(str_list):
        for j, w in enumerate(word):
            if j%2 == 0:
                temp_char = w.upper()
            else:
                temp_char = w.lower()
            word_list[i] += temp_char
    return ' '.join(word_list)

s = input()
print(solution(s))

# try hello world
# TRY HELLO WORLD
# Try helLO woRLd