'''
https://school.programmers.co.kr/learn/courses/30/lessons/160586
'''
# Not solved

def solution(keymap, targets):
    answer = []

    for target in targets:  # targets에 있는 한 단어에 대해서
        times = 0  # 누른 키 총합

        for char in target:  # 한 단어의 개별 문자에 대해
            flag = False  # 목표 문자열을 작성할 수 있는지 없는지 판단하기 위함
            time = 101  # keymap의 원소의 길이가 최대 100이기 때문에 101로 설정
            # keymap에 있는 모든 원소를 반복하면서 가장 적게 누를수 있는 char(문자)를 찾음
            for key in keymap:
                if char in key:  # key(문자열)안에 char(문자)가 존재하면
                    time = min(key.index(char) + 1, time)
                    flag = True  # 목표 문자열을 작성할 수 있음

            if not flag:  # 만약 keymap을 전부다 돌았는데도 문자를 찾지 못하면
                times = -1;
                break  # 목표 문자열을 작성할 수 없음

            times += time  # 하나의 문자에 대해 누른 키를 총합(키)에 더해줌

        answer.append(times)
        # targets에 있는 하나의 단어에 대해 수행이 끝났으면 answer에 누른 키 총합을 넣어줌

    return answer

keymap, targets = eval(input()), eval(input())
print(solution(keymap, targets))

'''
["ABACD", "BCEFD"]
["ABCD","AABB"]
'''

'''
["AA"]
["B"]
'''

'''
["AGZ", "BSSS"]
["ASA","BGZ"]
'''


'''
["ABACD", "BCEFD", "AA"]
["ABCD","AABB", "B"]
'''

'''
["ABCE"]
["ABDE"]
'''

'''
["BC"]
["AC", "BC"]
'''

'''
def solution(keymap, targets):
    answer = []
    for target in targets:
        mini_sum = []
        alpahbet_exists_in_keymap = []
        for alphabet in target:
            alpahbet_exists_in_key = []
            clicks = []
            alphabet_string = ''
            for key in keymap:
                first_index = key.find(alphabet) + 1
                alpahbet_exists_in_key.append(first_index)
                if first_index > 0:
                    alphabet_string += key[first_index - 1]
                    clicks.append(first_index)
                alpahbet_exists_in_keymap.append(min(alpahbet_exists_in_key))
            print(alpahbet_exists_in_key)
            if len(clicks) > 0 and sum(alpahbet_exists_in_keymap) > 0:
                mini_sum.append(min(clicks))
            else:
                mini_sum = [-1]
        answer.append(sum(mini_sum))
    return answer
'''