'''
https://school.programmers.co.kr/learn/courses/30/lessons/70129
'''
answer1, answer2 = 0, 0
def solution(s):
    global answer1, answer2

    one_count, zero_count = 0, 0
    for char in s:
        if char == '1':
            one_count += 1
        else:
            zero_count += 1
    binary = to_binary(one_count)

    answer1 += 1
    answer2 += zero_count

    if len(binary) > 1:
        return solution(binary)
    else:
        return [answer1, answer2]

def to_binary(one_count):
    result = ''
    while one_count > 0:
        result += str(one_count%2)
        one_count //= 2
    return result[::-1]


s = eval(input())
print(solution(s))

# "110010101001"
# "01110"
# "1111111"