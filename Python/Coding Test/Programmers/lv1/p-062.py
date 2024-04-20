'''
https://school.programmers.co.kr/learn/courses/30/lessons/42576
'''

def solution(participant, completion):
    answer = ''
    participant[:] = sorted(participant)
    completion[:] = sorted(completion)

    for i in range(len(completion)):
        if completion[i] != participant[i]:
            answer += participant[i]
            break

    if answer == '':
        answer = participant[-1]

    return answer

participant, completion = eval(input()), eval(input())
print(solution(participant, completion))

'''
["leo", "kiki", "eden"]
["eden", "kiki"]
'''

'''
["marina", "josipa", "nikola", "vinko", "filipa"]
["josipa", "filipa", "marina", "nikola"]
'''

'''
["mislav", "stanko", "mislav", "ana"]
["stanko", "ana", "mislav"]
'''