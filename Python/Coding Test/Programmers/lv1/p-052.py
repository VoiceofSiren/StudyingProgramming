'''
https://school.programmers.co.kr/learn/courses/30/lessons/42840
'''

def solution(answers):
    answer = [0, 0, 0]
    list1 = [1, 2, 3, 4, 5] * 2000
    list2 = [2, 1, 2, 3, 2, 4, 2, 5] * 1250
    list3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 1000
    students = [list1, list2, list3]
    for i in range(len(answers)):
        for j in range(len(students)):
            if answers[i] == students[j][i]:
                answer[j] += 1
    return get_students_with_highest_score(answer)

def get_students_with_highest_score(answer):
    result = []
    max_score = max(answer)
    for i, a in enumerate(answer):
        if a == max_score:
            result.append(i+1)
    return result

answers = eval(input())
print(solution(answers))

# [1,2,3,4,5]
# [1,3,2,4,2]