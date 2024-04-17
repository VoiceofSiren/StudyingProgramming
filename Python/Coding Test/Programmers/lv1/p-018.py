'''
https://school.programmers.co.kr/learn/courses/30/lessons/12948
'''

def solution(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]

phone_number = input()
print(solution(phone_number))

# 01033334444
# 027778888