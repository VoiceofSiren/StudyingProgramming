def solution(num_list):
    answer = num_list
    if num_list[-2] < num_list[-1]:
        answer.append(num_list[-1] - num_list[-2])
    else:
        answer.append(num_list[-1] * 2)
    return answer

def str_to_list(string):
  # 문자열을 리스트로 변환
  list_data = string.strip("[]").split(",")
  # 리스트의 각 원소를 정수로 변환
  for i in range(len(list_data)):
    list_data[i] = int(list_data[i])
  return list_data

num_list = str_to_list(input())
print(solution(num_list))

'''
def solution(num_list):        
    if num_list[-2] < num_list[-1]:
        num_list.append(num_list[-1] - num_list[-2])
    else:
        num_list.append(num_list[-1] * 2)
    return num_list
'''