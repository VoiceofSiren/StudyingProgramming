'''
https://school.programmers.co.kr/learn/courses/30/lessons/181913
'''

def solution(my_string, queries):
    answer = ''
    for query in queries:
        my_string = my_string[:query[0]] + my_string[query[0]:query[1]+1][::-1] + my_string[query[1]+1:]
    for i in range(len(my_string)):
        answer += my_string[i]
    return answer

def str_to_2darray(string):
    return [ list(row) for row in eval(string)]

my_string, queries = input(), str_to_2darray(input())
print(solution(my_string, queries))

'''
rermgorpsam
[[2, 3], [0, 7], [5, 9], [6, 10]]
'''