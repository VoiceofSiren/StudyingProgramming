'''
https://school.programmers.co.kr/learn/courses/30/lessons/181851
'''

def solution(rank, attendance):
    true_rank = []
    for i in range(len(attendance)):
        if attendance[i]:
            true_rank.append(rank[i])
    exclude = []
    r1 = get_highest_rank(true_rank, exclude)
    r2 = get_highest_rank(true_rank, exclude)
    r3 = get_highest_rank(true_rank, exclude)
    a, b, c = get_index(rank, r1), get_index(rank, r2), get_index(rank, r3)
    return 10000*a + 100*b + c

def get_highest_rank(true_rank, exclude):
    highest_rank = 100
    for tr in true_rank:
        if tr not in exclude:
            highest_rank = min(highest_rank, tr)
    exclude.append(highest_rank)
    return highest_rank

def get_index(rank, r):
    index = -1
    for i in range(len(rank)):
        if rank[i] == r:
            index = i
    return index

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

def str_to_bool_list(string):
    bool_list = string.strip('[]').split(', ')
    for i in range(len(bool_list)):
        if bool_list[i] == 'true':
            bool_list[i] = True
        else:
            bool_list[i] = False
    return bool_list

rank, attendance = str_to_num_list(input()), str_to_bool_list(input())
print(solution(rank, attendance))

'''
[3, 7, 2, 5, 4, 6, 1]
[false, true, true, true, true, false, false]
'''
'''
[1, 2, 3]
[true, true, true]
'''
'''
[6, 1, 5, 2, 3, 4]
[true, false, true, false, false, true]
'''