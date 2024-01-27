# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/falling-horizontal-block?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
-
#### [코드 1]
```python
n, m, t = tuple(map(int, input().split()))

square = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp_count = [
    [0 for j in range(n)]
    for i in range(n)
]

count = [
    [0 for j in range(n)]
    for i in range(n)
]

#      N  S  W  E
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def get_max_value(x, y, square):
    max_value = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])

def get_dir_num(x, y, square):
    dir_num = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        if square[nx][ny] == get_max_value(x, y, square):
            dir_num = i
            break
    return dir_num

def move(x, y, square):
    temp_value = temp_count[x][y]
    temp_count[x][y] = 0
    x = x + dx[get_dir_num(x, y, square)]
    y = y + dy[get_dir_num(x, y, square)]
    temp_count[x][y] += temp_value


rc_list = []
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    r, c = r - 1, c - 1
    rc_list.append([r, c])
    temp_count[r][c] = 1

for _ in range(t):
    for i in range(m):
        x, y = rc_list[i][0], rc_list[i][1]
        move(x, y, square)

result = 0
for row in temp_count:
    for element in row:
        if element >= 1:
            result += 1
print(result)
```
#### [결과 1]
```plaintext
3
```
#### --> 이번 테스트 케이스에 대해서는 정답이 출력되었으나, 다른 테스트 케이스에 대해서는 오답이 출력되었다.
