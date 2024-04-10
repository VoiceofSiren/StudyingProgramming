'''
https://school.programmers.co.kr/learn/courses/30/lessons/181915
'''

def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer = answer + my_string[i]
    return answer

def str_to_list(string):
  # 문자열을 리스트로 변환
  list_data = string.strip("[]").split(", ")
  # 리스트의 각 원소를 정수로 변환
  for i in range(len(list_data)):
    list_data[i] = int(list_data[i])
  return list_data

my_string = input()
index_list = str_to_list(input())

print(solution(my_string, index_list))

# cvsgiorszzzmrpaqpe
# [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]