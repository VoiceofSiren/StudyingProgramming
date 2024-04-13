'''
https://school.programmers.co.kr/learn/courses/30/lessons/181862
'''

def solution(myStr):
    myStr = myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ')
    return len(myStr.split()) == 0 and ['EMPTY'] or myStr.split()

myStr = input()
print(solution(myStr))

# baconlettucetomato
# abcd
# cabab