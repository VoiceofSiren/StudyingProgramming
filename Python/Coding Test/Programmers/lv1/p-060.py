'''
https://school.programmers.co.kr/learn/courses/30/lessons/17682
'''

def solution(dartResult):
    num_list = [ str(i) for i in range(0, 11) ]
    bonus_dict = {
        'S': 1,
        'D': 2,
        'T': 3
    }
    option_dict = {
        ' ': 1,
        '*': 2,
        '#': -1
    }
    dartResult = list(dartResult)


    # '1', '0' --> '10'
    i = 0
    while i < len(dartResult) - 1:
        if dartResult[i] == '1' and dartResult[i+1] == '0':
            dartResult[i] = '10'
            del dartResult[i+1]
        i += 1


    #     ['1', 'D', '2', 'S', '#', '10', 'S']
    # --> ['1', 'D', ' ', '2', 'S', '#', '10', 'S', ' ']
    i = 0
    while i < len(dartResult) - 2:
        for j in range(i, i+3):
            if dartResult[j] in num_list and dartResult[j+1] in bonus_dict:
                if dartResult[j+2] not in option_dict:
                    dartResult[:] = dartResult[:j+2] + [' '] + dartResult[j+2:]
                i += 3
    if dartResult[-1] not in option_dict:
        dartResult.append(' ')


    # Caculate each score
    answer_list = [0, 0, 0]
    for i in range(0, len(dartResult), 3):
        answer_list[i//3] += (int(dartResult[i])**bonus_dict[dartResult[i+1]]*option_dict[dartResult[i+2]])
        if i >= 3 and dartResult[i+2] == '*':
            answer_list[i//3 - 1] *= 2

    return sum(answer_list)


dartResult = input()
print(solution(dartResult))