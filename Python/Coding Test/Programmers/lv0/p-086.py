'''
https://school.programmers.co.kr/learn/courses/30/lessons/181942
'''

def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i]
        answer += str2[i]
    return answer

str1, str2 = input().split()
print(solution(str1, str2))

# aaaaa bbbbb