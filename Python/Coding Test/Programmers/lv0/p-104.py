'''
https://school.programmers.co.kr/learn/courses/30/lessons/181881
'''

def solution(arr):
    answer = 0
    while True:
        arr1 = [
            i for i in arr
        ]
        arr2 = operation(arr1)
        if not equals(arr1, arr2):
            answer += 1
            arr = arr2
        else:
            break
    return answer

def operation(arr):
    new_arr = [
        i for i in arr
    ]
    for i in range(len(new_arr)):
        if new_arr[i] >= 50 and new_arr[i]%2 == 0:
            new_arr[i] //= 2
        elif new_arr[i] < 50 and new_arr[i]%2 == 1:
            new_arr[i] = new_arr[i] * 2 + 1
    return new_arr

def equals(arr1, arr2):
    result = True
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            result = False
    return result

def str_to_num_list(string):
    num_list = string.strip('[]').split(', ')
    for i in range(len(num_list)):
        num_list[i] = int(num_list[i])
    return num_list

arr = str_to_num_list(input())
print(solution(arr))

# [1, 2, 3, 100, 99, 98]