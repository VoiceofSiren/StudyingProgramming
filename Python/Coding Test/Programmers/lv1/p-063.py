'''
https://school.programmers.co.kr/learn/courses/30/lessons/42862
'''

def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n)
    for i in range(len(lost)):
        lost[i] -= 1
    for i in range(len(reserve)):
        reserve[i] -= 1

    for r in reserve:
        students[r] += 1
    for l in lost:
        students[l] -= 1

    for i in range(len(students)-1):
        if (students[i], students[i+1]) in [(2, 0), (0, 2)]:
            students[i], students[i+1] = (1, 1)

    for student in students:
        if student >= 1:
            answer += 1
    return answer

n, lost, reserve = int(input()), eval(input()), eval(input())
print(solution(n, lost, reserve))

'''
5
[2, 4]
[1, 3, 5]
'''

'''
5
[2, 4]
[3]
'''

'''
3
[3]
[1]
'''