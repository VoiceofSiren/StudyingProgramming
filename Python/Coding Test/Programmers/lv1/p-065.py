'''
https://school.programmers.co.kr/learn/courses/30/lessons/140108
'''

def solution(s):
    answer = 0

    char = ''
    same = 0
    diff = 0

    for alphabet in s:
        if char == '':
            char = alphabet
            same += 1
            continue

        if char == alphabet:
            same += 1
        else:
            diff += 1

        if same == diff:
            char = ''
            same = 0
            diff = 0
            answer += 1

    if char != '':
        answer += 1

    return answer



s = input()
print(solution(s))

# banana
# abracadabra
# aaabbaccccabba



'''
def solution(s):
    answer = []
    s_list = list(s)
    i = 0
    while i < len(s_list) - 1:
        x = s_list[0]
        max_same_count = 1
        same_count = 1
        for j in range(i+1, len(s_list)):
            if s_list[j] == x:
                same_count += 1
                max_same_count += 1
            else:
                same_count -= 1

            if same_count == 0:
                answer.append(s_list[:max_same_count*2])
                s_list[:] = s_list[max_same_count*2:]
                i = 0
                break
    if len(s_list) > 0:
        answer.append(s_list)
    return len(answer)
'''