'''
https://school.programmers.co.kr/learn/courses/30/lessons/12951
'''

def solution(s):
    answer = ''
    word_list = s.split()
    is_space_first = s[0] == ' ' and True or False

    space_list = list()
    space_count = 0
    for idx, char in enumerate(s):
        if idx == len(s) - 1 and char == ' ':
            space_list.append(space_count + 1)
            break
        if char == ' ':
            space_count += 1
        else:
            if space_count > 0:
                space_list.append(space_count)
            space_count = 0

    result_list = [ capitalize(word) for word in word_list]

    print(space_list)
    print(result_list)

    if len(space_list) > 0 and len(result_list) > 0:
        for i in range(min(len(space_list), len(result_list))):
            if is_space_first:
                answer += ' ' * space_list[i] + result_list[i]
            else:
                answer += result_list[i] + ' ' * space_list[i]

    if len(result_list) > len(space_list):
        answer += result_list[-1]
    elif len(result_list) < len(space_list):
        answer += ' ' * space_list[-1]
    return answer

def capitalize(word):
    new_word = ''
    if 97 <= ord(word[0]) <= 122:
        new_word += chr(ord(word[0]) - 32)
    else:
        new_word += word[0]
    if len(word) > 1:
        for i in range(1, len(word)):
            if 65 <= ord(word[i]) <= 90:
                new_word += chr(ord(word[i]) + 32)
            else:
                new_word += word[i]
    return new_word

s = eval(input())
print(solution(s))

# "3people unFollowed me"
# "for the      last  week"
# "    abc  "
# "   "
