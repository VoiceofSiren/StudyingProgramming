'''
https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=python3
'''

def solution(x):
    x = str(x)
    digits = [ int(x[i]) for i in range(len(x)) ]
    return int(x) % sum(digits) == 0 and True or False

x = int(input())
print(solution(x))

# 10
# 12
# 11
# 13