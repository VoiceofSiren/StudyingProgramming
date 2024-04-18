'''
https://school.programmers.co.kr/learn/courses/30/lessons/68644
'''

def solution(numbers):
    answer = []
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            sum_val = numbers[i] + numbers[j]
            if sum_val not in answer:
                answer.append(sum_val)
    return sorted(answer)

numbers = eval(input())
print(solution(numbers))

# [2,1,3,4,1]
# [5,0,2,7]