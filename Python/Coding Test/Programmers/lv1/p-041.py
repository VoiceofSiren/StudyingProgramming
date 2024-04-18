'''
https://school.programmers.co.kr/learn/courses/30/lessons/12915
'''

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))

strings, n = eval(input()), int(input())
print(solution(strings, n))

'''
["sun", "bed", "car"]
1
'''
'''
["abce", "abcd", "cdx"]
2
'''