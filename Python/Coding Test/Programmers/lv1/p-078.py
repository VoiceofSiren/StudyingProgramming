'''
https://school.programmers.co.kr/learn/courses/30/lessons/178871
'''

def solution(players, callings):
    player_dict = dict()

    for i, player in enumerate(players):
        player_dict[player] = i

    for calling in callings:
        # 앞지른 선수의 index
        idx = player_dict[calling]

        # 추월당한 선수의 이름
        name = players[idx-1]

        # swap index
        player_dict[calling] = idx - 1
        player_dict[name] = idx
        players[idx - 1] = calling
        players[idx] = name

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





'''
def solution(players, callings):
    answer = ['']*len(players)
    player_dict = dict()

    for i, player in enumerate(players):
        player_dict[player] = i
    # print(player_dict)

    for calling in callings:
        player_dict[calling] -= 1
        for player in player_dict:
            if player_dict[calling] == player_dict[player] and calling != player:
                player_dict[player] += 1
        # print(player_dict)

    for player in player_dict:
        answer[player_dict[player]] += player
    return answer
'''