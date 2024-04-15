'''
https://school.programmers.co.kr/learn/courses/30/lessons/181921
'''

def solution(l, r):
    answer = []
    numbers = generate_numbers()
    for i in range(l, r+1):
        if i in numbers:
            answer.append(i)
    return len(answer) > 0 and answer or [-1]

def generate_numbers():
    numbers = []
    for i in range(1000001):
        if contains(str(i), '0', '5'):
            numbers.append(i)
    return numbers

def contains(string, c1, c2):
    result = True
    for i in range(len(string)):
        if string[i] != c1 and string[i] == c2:
            continue
        elif string[i] == c1 and string[i] != c2:
            continue
        elif string[i] == c1 and string[i] != c2:
            continue
        else:
            result = False
    return result

l, r = map(int, input().split())
print(solution(l, r))

# 5 555
# 10 20