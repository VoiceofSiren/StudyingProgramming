'''
https://school.programmers.co.kr/learn/courses/30/lessons/181905
'''

def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]



my_string, s, e = input().split()
s, e = int(s), int(e)
print(solution(my_string, s, e))

# Progra21Sremm3 6 12
# Stanley1yelnatS 4 10