'''
https://school.programmers.co.kr/learn/courses/30/lessons/92334
'''

def solution(bandage, health, attacks):

    t, x, y = bandage
    end_time = attacks[-1][0]

    time_list, damage_list = list(), list()
    for attack in attacks:
        attack_time, damage = attack
        time_list.append(attack_time)
        damage_list.append(damage)

    h, continous = health, 0
    for time in range(0, end_time + 1):
        if time not in time_list:
            h += x
            continous += 1
            if continous == t:
                h += y
                continous = 0
            if h > health:
                h = health
            # print(f'h = {h}, continuous = {continous}')
        else:
            idx = get_index(time, time_list)
            damage = damage_list[idx]
            h -= damage
            continous = 0
            # print(f'h = {h}, continuous = {continous}')
            if h <= 0:
                h = -1
                break
    return h

def get_index(time, time_list):
    idx = 0
    for i, t in enumerate(time_list):
        if t == time:
            idx = i
    return idx

def str_to_2d_array(string):
    return [ list(row) for row in eval(string) ]

bandage, health, attacks = eval(input()), int(input()), str_to_2d_array(input())
print(solution(bandage, health, attacks))

'''
[5, 1, 5]
30
[[2, 10], [9, 15], [10, 5], [11, 5]]
'''

'''
[3, 2, 7]
20
[[1, 15], [5, 16], [8, 6]]
'''

'''
[4, 2, 7]
20
[[1, 15], [5, 16], [8, 6]]
'''

'''
[1, 1, 1]
5
[[1, 2], [3, 2]]
'''