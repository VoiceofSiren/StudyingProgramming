'''
https://school.programmers.co.kr/learn/courses/30/lessons/258712
'''

def solution(friends, gifts):
    answer = 0

    # 모든 친구 쌍 dict 정의
    friend_pair_dict = dict()
    for i in range(0, len(friends) - 1):
        for j in range(i + 1, len(friends)):
            sender, receiver = friends[i], friends[j]
            friend_pair_dict[sender + ' ' + receiver] = 0
            friend_pair_dict[receiver + ' ' + sender] = 0

    # 선물 지수 dict 정의
    gift_value_dict = dict()
    for friend in friends:
        gift_value_dict[friend] = 0

    # friend_pair_dict, gift_value_dict 연산
    for gift in gifts:
        friend_pair_dict[gift] += 1
        sender, receiver = gift.split()
        gift_value_dict[sender] += 1
        gift_value_dict[receiver] -= 1

    # 선물 받을 개수 (=결과값)를 저장할 dict 정의
    result_dict = dict()
    for friend in friends:
        result_dict[friend] = 0

    for friend_pair in friend_pair_dict:
        sender, receiver = friend_pair.split()
        if friend_pair_dict[friend_pair] > friend_pair_dict[receiver + ' ' + sender]:
            result_dict[sender] += 1
        elif friend_pair_dict[friend_pair] < friend_pair_dict[receiver + ' ' + sender]:
            result_dict[receiver] += 1
        else:
            if gift_value_dict[sender] > gift_value_dict[receiver]:
                result_dict[sender] += 1
            elif gift_value_dict[sender] < gift_value_dict[receiver]:
                result_dict[receiver] += 1
            else:
                continue

    for result in result_dict:
        answer = max(answer, result_dict[result])

    return answer//2

friends, gifts = eval(input()), eval(input())
print(solution(friends, gifts))

'''
["muzi", "ryan", "frodo", "neo"]
["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]
'''

'''
["joy", "brad", "alessandro", "conan", "david"]
["alessandro brad", "alessandro joy", "alessandro conan", "david alessandro", "alessandro david"]
'''

'''
["a", "b", "c"]
["a b", "b a", "c a", "a c", "a c", "c a"]
'''