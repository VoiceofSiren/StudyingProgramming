'''
https://school.programmers.co.kr/learn/courses/30/lessons/150370
'''


def solution(today, terms, privacies):
    answer = []

    today = today.strip('""').split('.')
    year, month, date = int(today[0]), int(today[1]), int(today[2])

    terms_dict = dict()
    for term in terms:
        terms_dict[term.split()[0]] = int(term.split()[1])

    for i, privacy in enumerate(privacies):
        p_day = privacy.split()[0].strip('""').split('.')
        p_year, p_month, p_date = int(p_day[0]), int(p_day[1]), int(p_day[2])
        p_term = privacy.split()[1]

        for j in range(terms_dict[p_term] * 28):
            p_date += 1
            if p_date > 28:
                p_date = 1
                p_month += 1
                if p_month > 12:
                    p_month = 1
                    p_year += 1
        if p_year > year:
            answer.append(i + 1)
        elif p_year == year:
            if p_month > month:
                answer.append(i + 1)
            elif p_month == month:
                if p_date > p_date:
                    answer.append(i + 1)

    return answer


today, terms, privacies = input(), eval(input()), eval(input())
print(solution(today, terms, privacies))

'''
"2022.05.19"
["A 6", "B 12", "C 3"]
["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
'''

'''
"2020.01.01"
["Z 3", "D 5"]
["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]
'''