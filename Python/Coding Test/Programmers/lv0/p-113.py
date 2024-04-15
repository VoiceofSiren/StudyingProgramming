'''
https://school.programmers.co.kr/learn/courses/30/lessons/181943
'''

def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):]

my_string, overwrite_string, s = input().split()
s = int(s)
print(solution(my_string, overwrite_string, s))

# He11oWor1d lloWorl 2
# Program29b8UYP merS123 7