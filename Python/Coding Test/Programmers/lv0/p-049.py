'''
https://school.programmers.co.kr/learn/courses/30/lessons/181906
'''

def solution(my_string, is_prefix):
    answer = 1
    range_num = min(len(my_string), len(is_prefix))
    for i in range(range_num):
        if is_prefix[i] != my_string[i]:
            answer = 0
    if len(is_prefix) > len(my_string):
        answer = 0
    return answer

my_string, is_prefix = input().split()
print(solution(my_string, is_prefix))

# banana ban
# banana nan
# banana abcd
# banana bananan