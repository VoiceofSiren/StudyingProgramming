'''
https://school.programmers.co.kr/learn/courses/30/lessons/181842
'''


def solution(str1, str2):
    return (str1 in str2) and 1 or 0


str1, str2 = input().split()
print(solution(str1, str2))

# abc aabcc
# tbt tbbttb