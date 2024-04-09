def solution(my_string, n):
    return my_string[n*(-1):-1] + my_string[-1]

my_string, n = input(), int(input())
print(solution(my_string, n))

# ProgrammerS123 11