'''
https://school.programmers.co.kr/learn/courses/30/lessons/181871
'''

def solution(myString, pat):
    answer = 0
    for i in range(len(myString) - len(pat) + 1):
        is_same = True
        for j in range(len(pat)):
            if myString[i+j] != pat[j]:
                is_same = False
        if is_same:
            answer += 1
    return answer

myString, pat = input().split()
print(solution(myString, pat))

# banana ana
# aaaa aa