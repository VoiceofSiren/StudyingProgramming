'''
https://school.programmers.co.kr/learn/courses/30/lessons/118666
'''

def solution(survey, choices):
    answer = ''
    survey_dict = {
        'R': 0,
        'T': 0,
        'C': 0,
        'F': 0,
        'M': 0,
        'J': 0,
        'A': 0,
        'N': 0

    }

    n = len(survey)
    for i in range(n):
        if choices[i] == 4:
            continue
        elif choices[i] < 4:
            survey_dict[survey[i][0]] += 4 - choices[i]
        else:
            survey_dict[survey[i][1]] += choices[i] - 4

    r, t = survey_dict['R'], survey_dict['T']
    c, f = survey_dict['C'], survey_dict['F']
    m, j = survey_dict['M'], survey_dict['J']
    a, n = survey_dict['A'], survey_dict['N']

    if r >= t:
        answer += 'R'
    else:
        answer += 'T'

    if c >= f:
        answer += 'C'
    else:
        answer += 'F'

    if j >= m:
        answer += 'J'
    else:
        answer += 'M'

    if a >= n:
        answer += 'A'
    else:
        answer += 'N'

    return answer

survey, choices = eval(input()), eval(input())
print(solution(survey, choices))

'''
["AN", "CF", "MJ", "RT", "NA"]
[5, 3, 2, 7, 5]
'''

'''
["TR", "RT", "TR"]
[7, 1, 3]
'''