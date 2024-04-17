'''
https://school.programmers.co.kr/learn/courses/30/lessons/12935
'''

'''
def solution(arr):
    answer = []
    for elem in arr:
        if elem > min(arr):
            answer.append(elem)
    return len(answer)>0 and answer or [-1]
'''

def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        del arr[arr.index(min(arr))]
        return arr

def str_to_num_list(string):
    num_list = string.strip('[]').split(',')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr = str_to_num_list(input())
print(solution(arr))

# [4,3,2,1]
# [10]