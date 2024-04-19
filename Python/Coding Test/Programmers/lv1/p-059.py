'''
https://school.programmers.co.kr/learn/courses/30/lessons/133499
'''

def solution(babbling):
    answer = 0
    # possible_pronounciation_list
    ppl = ["aya", "ye", "woo", "ma"]

    for i in range(len(babbling)):
        for j in range(len(ppl)):
            babbling[i] = babbling[i].replace(ppl[j], str(j))

    # print(babbling)
    for b in babbling:
        if b == remove_alphabet(b) and not is_doubled(b):
            answer += 1

    return answer

def remove_alphabet(b):
    new_b = ''
    for i in range(len(b)):
        if 97 <= ord(b[i]) <= 122:
            new_b += ''
        else:
            new_b += b[i]
    return new_b

def is_doubled(b):
    result = False
    for i in range(len(b)-1):
        if b[i] == b[i+1]:
            result = True
            break
    return result


babbling = eval(input())
print(solution(babbling))

# ["aya", "yee", "u", "maa"]
# ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]