'''
https://school.programmers.co.kr/learn/courses/30/lessons/17681
'''

def solution(n, arr1, arr2):
    answer = []
    bm1, bm2 = [], []
    for d1 in arr1:
        bm1.append(to_binary(n, d1))
    for d2 in arr2:
        bm2.append(to_binary(n, d2))

    map_matrix = []
    for i in range(len(bm1)):
        map_matrix.append(overlap(bm1[i], bm2[i]))

    for i in range(len(map_matrix)):
        temp_string = ''
        for j in range(len(map_matrix[i])):
            if map_matrix[i][j] == 1:
                temp_string += '#'
            else:
                temp_string += ' '
        answer.append(temp_string)
    return answer

def to_binary(n, decimal):
    binary_list = []
    for _ in range(n):
        if decimal == 0:
            binary_list.append(0)
            continue
        binary_list.append(decimal%2)
        decimal //= 2

    return binary_list[::-1]

def overlap(b_list1, b_list2):
    overlapped_list = []
    for i in range(len(b_list1)):
        if b_list1[i]==0 and b_list2[i]==0:
            overlapped_list.append(0)
        else:
            overlapped_list.append(1)
    return overlapped_list

n, arr1, arr2 = int(input()), eval(input()), eval(input())
print(solution(n, arr1, arr2))
# for matrix in solution(n, arr1, arr2):
#     for row in matrix:
#         print(row)
#     print()
'''
# 9     # 20    # 28    # 18    # 11
01001   10100   11100   10010   01011

# 30    # 1     # 21    # 17    # 28
11110   00001   10101   10001   11100
'''
'''
5
[9, 20, 28, 18, 11]
[30, 1, 21, 17, 28]
'''



'''
# 46    # 33    # 33    # 22    # 31    # 50
101110  100001  100001  010110  011111  110010
# 27    # 56    # 19    # 14    # 14    # 10
0011011 111000  010011  001110  001110  001010
'''
'''
6
[46, 33, 33 ,22, 31, 50]
[27 ,56, 19, 14, 14, 10]
'''