def solution(a, b, flag):
    if flag == True:
        return a + b
    else:
        return a - b

a, b, flag = int(input()), int(input()), bool(input())
print(solution(a, b, flag))