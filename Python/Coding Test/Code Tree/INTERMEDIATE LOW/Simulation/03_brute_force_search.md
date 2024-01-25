# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/conveyor-belt?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >

#### [코드 1]



n, t = list(map(int, input().split()))

c_belt = [list(map(int, input().split())) for _ in range(2)]

for i in range(t):
    temp1 = c_belt[0][n-1]
    temp2 = c_belt[1][0]

    for j in range(n-1, 1, -1):
        c_belt[0][j] = c_belt[0][j-1]
    c_belt[0][0] = temp1

    for j in range(n-2):
        c_belt[1][j] = c_belt[1][j+1]
    c_belt[1][n-1] = temp2

for i in range(2):
    for j in range(n):
        print(c_belt[i][j], end=' ')
    print()





-----------------------------------
n, t = list(map(int, input().split()))

c_belt = [list(map(int, input().split())) for _ in range(2)]

time = 0
while time < t:
    
    temp1 = c_belt[0][n-1]
    temp2 = c_belt[1][n-1]
    for i in range(2):
        for j in range(n-1, 0, -1):
            c_belt[i][j] = c_belt[i][j-1]
        
    c_belt[0][0] = temp2
    c_belt[1][0] = temp1

    time += 1

for i in range(2):
    for j in range(n):
        print(c_belt[i][j], end=' ')
    print()
