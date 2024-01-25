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
