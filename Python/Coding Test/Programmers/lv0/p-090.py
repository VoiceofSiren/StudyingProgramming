'''
https://school.programmers.co.kr/learn/courses/30/lessons/181872
'''

def solution(myString, pat):
    return myString[:find_func(myString, pat) + len(pat)]

def find_func(myString, pat):
    idx_list = []
    for i in range(len(myString) - len(pat) + 1):
        is_same = True
        for j in range(len(pat)):
            if myString[i+j] != pat[j]:
                is_same = False
        if is_same:
            idx_list.append(i)
    return max(idx_list)


myString, pat = input().split()
print(solution(myString, pat))

# AbCdEFG dE
# AAAAaaaa a