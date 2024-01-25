n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]

def count_coins(i, j, square):
    count_value = 0
    for i in range(i, i+3):
        for j in range(j, j+3):
            if square[i][j] == 1:
                count_value += 1
    return count_value


max_value = 0
for i in range(n-2):
    for j in range(n-2):
        coin_value = count_coins(i, j, square)
        if coin_value > max_value:
            max_value = coin_value
print(max_value)
