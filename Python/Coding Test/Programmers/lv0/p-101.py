'''
https://school.programmers.co.kr/learn/courses/30/lessons/181903
'''


def solution(q, r, code):
    answer = ''
    for i in range(len(code)):
        if i%q  == r:
            answer += code[i]
    return answer

q, r, code = input().split()
q, r = int(q), int(r)
print(solution(q, r, code))

# 3 1 qjnwezgrpirldywt
# 1 0 programmers