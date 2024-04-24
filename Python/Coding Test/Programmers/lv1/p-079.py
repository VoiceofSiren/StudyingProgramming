'''
https://school.programmers.co.kr/learn/courses/30/lessons/92334
'''

def solution(id_list, report_list, k):
    answer = []

    num_dict = dict()
    report_dict = dict()

    for id in id_list:
        num_dict[id] = 0
        report_dict[id] = list()

    report_set = set()
    for report in report_list:
        report_set.add(report)

    for report in report_set:
        id, reported_id = report.split()
        num_dict[reported_id] += 1

    for report in report_set:
        id, reported_id = report.split()
        if num_dict[reported_id] >= k:
            report_dict[id].append(reported_id)

    for report in report_dict:
        answer.append(len(report_dict[report]))

    return answer

id_list, report_list, k = eval(input()), eval(input()), int(input())
print(solution(id_list, report_list, k))

'''
["muzi", "frodo", "apeach", "neo"]
["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
2
'''

'''
["con", "ryan"]
["ryan con", "ryan con", "ryan con", "ryan con"]
3
'''