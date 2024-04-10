def solution(myString):
    answer = ''
    for i in range(len(myString)):
        ascii_num = ord(myString[i])
        if 65 <= ascii_num <= 90:
            ascii_num += 32
        answer += chr(ascii_num)
    return answer

myString = input()
print(solution(myString))

# aBcDeFg