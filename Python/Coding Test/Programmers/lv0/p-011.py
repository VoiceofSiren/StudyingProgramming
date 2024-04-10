def solution(a, b):
    if sum_func(a, b) >= mul_func(a, b):
        #print(f'sum / sum = {sum_func(a, b)}, mul = {mul_func(a, b)}')
        return sum_func(a, b)
    else:
        #print(f'mul / sum = {sum_func(a, b)}, mul = {mul_func(a, b)}')
        return mul_func(a, b)

def sum_func(a, b):
    return int(a + b)

def mul_func(a, b):
    return 2 * int(a) * int(b)

a, b = input(), input()
print(solution(a, b))