'''
https://school.programmers.co.kr/learn/courses/30/lessons/67256
'''

def solution(numbers, hand):
    answer = ''
    keypad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [-1, 0, -1]
    ]

    l_finger = [3, 0]
    r_finger = [3, 2]

    for number in numbers:
        coordinate = find_coordinate(number, keypad)
        l_distance = calculate_distance(l_finger, coordinate)
        r_distance = calculate_distance(r_finger, coordinate)
        if coordinate[1] == 0:
            l_finger = coordinate
            answer += 'L'
        elif coordinate[1] == 2:
            r_finger = coordinate
            answer += 'R'
        else:
            if l_distance < r_distance:
                l_finger = coordinate
                answer += 'L'
            elif r_distance < l_distance:
                r_finger = coordinate
                answer += 'R'
            else:
                if hand == 'left':
                    l_finger = coordinate
                    answer += 'L'
                else:
                    r_finger = coordinate
                    answer += 'R'
    return answer

def calculate_distance(finger, key):
    return abs(finger[0] - key[0]) + abs(finger[1] - key[1])

def find_coordinate(number, keypad):
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == number:
                return [i, j]

numbers, hand = eval(input()), input()
print(solution(numbers, hand))

'''
[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
right
'''

'''
[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
left
'''

'''
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
right
'''