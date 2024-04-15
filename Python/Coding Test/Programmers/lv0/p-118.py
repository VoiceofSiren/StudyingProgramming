'''
https://school.programmers.co.kr/learn/courses/30/lessons/181949
'''

str = input()
new_str = ''

for i in range(len(str)):
    if 65 <= ord(str[i]) <= 90:
        new_str += chr(ord(str[i]) + 32)
    else:
        new_str += chr(ord(str[i]) - 32)

print(new_str)

# aBcDeFg