'''
https://school.programmers.co.kr/learn/courses/30/lessons/181849
'''

def solution(num_str):
    answer = 0
    for i in range(len(num_str)):
        answer += int(num_str[i])
    return answer

num_str = input()
print(solution(num_str))

# 123456789
# 1000000