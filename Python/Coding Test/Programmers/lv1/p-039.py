'''
https://school.programmers.co.kr/learn/courses/30/lessons/81301
'''

def solution(s):
    digit_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    answer = ''

    for i in range(len(s)):
        if 48 <= ord(s[i]) <= 57:
            answer += s[i]
            continue
        temp_word = ''
        for j in range(i, i + 5):
            if not in_range(j, s):
                break
            if 48 <= ord(s[j]) <= 57:
                break
            temp_word += s[j]

            if temp_word in digit_dict:
                answer += digit_dict[temp_word]
                break
    return int(answer)

def in_range(x, s):
    return 0 <= x < len(s)

s = input()
print(solution(s))

# one4seveneight
# 23four5six7
# 2three45sixseven
# 123