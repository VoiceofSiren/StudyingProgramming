'''
https://school.programmers.co.kr/learn/courses/30/lessons/147355
'''

def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            answer += 1
    return answer

t, p = input().split()
print(solution(t, p))

# 3141592 271
# 500220839878 7
# 10203 15