'''
https://school.programmers.co.kr/learn/courses/30/lessons/178871
'''

def solution(players, callings):
    for calling in callings:
        idx = players.index(calling)
        print(idx)
        players[idx-1], players[idx] = players[idx], players[idx-1]
    return players

players, callings = eval(input()), eval(input())
print(solution(players, callings))

'''
["mumu", "soe", "poe", "kai", "mine"]
["kai", "kai", "mine", "mine"]
'''

'''
mumu soe poe kai mine
mumu soe kai poe mine
mumu kai soe poe mine
mumu kai soe mine poe
mumu kai mine soe poe
'''
