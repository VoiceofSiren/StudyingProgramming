'''
https://school.programmers.co.kr/learn/courses/30/lessons/159994
'''

def solution(cards1, cards2, goal):
    for g in goal:
        if g not in cards1 + cards2:
            return 'No'
        if len(cards1) > 0 and len(cards2) == 0:
            if g == cards1[0]:
                cards1 = cards1[1:]
            else:
                return 'No'
        elif len(cards1) == 0 and len(cards2) > 0:
            if g == cards2[0]:
                cards2 = cards2[1:]
            else:
                return 'No'
        elif len(cards1) > 0 and len(cards2) > 0:
            if g in [cards1[0], cards2[0]]:
                if g == cards1[0]:
                    cards1 = cards1[1:]
                else:
                    cards2 = cards2[1:]
        else:
            return 'No'

    return 'Yes'

cards1, cards2, goal = eval(input()), eval(input()), eval(input())
print(solution(cards1, cards2, goal))

'''
["i", "drink", "water"]
["want", "to"]
["i", "want", "to", "drink", "water"]
'''

'''
["i", "water", "drink"]
["want", "to"]
["i", "want", "to", "drink", "water"]
'''