'''
https://school.programmers.co.kr/learn/courses/30/lessons/133502
'''

def solution(ingredient):
    answer = 0
    collect = []
    for igd in ingredient:
        collect.append(igd)
        if collect[-4:] == [1, 2, 3, 1]:
            answer += 1
            for _ in range(4):
                collect.pop()
    return answer

ingredient = eval(input())
print(solution(ingredient))

# [2, 1, 1, 2, 3, 1, 2, 3, 1]
# [1, 3, 2, 1, 2, 1, 3, 1, 2]

'''
def solution(ingredient):
    answer = 0
    i = 0
    while i < len(ingredient) - 3:
        if ingredient[i:i+4] == [1, 2, 3, 1]:
            print(f'i = {i}')
            ingredient[:] = ingredient[:i] + ingredient[i+4:]
            answer += 1
            i = 0
        else:
            i += 1
    return answer
'''