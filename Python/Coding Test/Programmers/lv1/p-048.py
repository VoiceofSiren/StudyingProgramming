'''
https://school.programmers.co.kr/learn/courses/30/lessons/176963
'''

def solution(name, yearning, photo):
    answer = [ 0 for _ in range(len(photo)) ]
    for i in range(len(photo)):
        for j in range(len(photo[i])):
            answer[i] += get_yearning_score(photo[i][j], name, yearning)
    return answer

def get_yearning_score(name_to_find, name, yearning):
    yearning_score = 0
    for i, n in enumerate(name):
        if n == name_to_find:
            yearning_score = yearning[i]
    return yearning_score

def str_to_2d_array(string):
    return [ list(row) for row in eval(string) ]

name, yearning, photo = eval(input()), eval(input()), str_to_2d_array(input())
print(solution(name, yearning, photo))

'''
["may", "kein", "kain", "radi"]
[5, 10, 1, 3]
[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
'''

'''
["kali", "mari", "don"]
[11, 1, 55]
[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
'''

'''
["may", "kein", "kain", "radi"]
[5, 10, 1, 3]
[["may"],["kein", "deny", "may"], ["kon", "coni"]]
'''