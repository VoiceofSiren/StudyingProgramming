# Brute Force Search
###### Question: https://www.codetree.ai/missions/2/problems/falling-horizontal-block?&utm_source=clipboard&utm_medium=text
###### Difficulty: Easy
<br/>

### 이 글의 목적
    - 완전 탐색 기법을 활용한 문제를 풀어보고자 한다.
    - 저작권법 및 기타 관련 법률에 의하여 필자가 작성한 코드만 공유할 수 있다. (저작권자 © 브랜치앤바운드)
<br/>

### < 구현 과정 - 1 >
- 각 칸에서 최댓값을 구한 후 각 칸에서 다시 dx dy Technique를 활용해 해당 칸에서 반복문을 돌리다가 최댓값일 때 멈추는 방식으로 구현하고자 한다.
#### [코드 1-1]
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
```
#### [코드 1-2]
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
#### [코드 1-3]
```python
def get_max_value(x, y, square):
    max_value = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])
```
#### [코드 1-4]
```python
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
```
#### [코드 1-5]
```python
def move(x, y, square):
    temp_value = temp_count[x][y]
    temp_count[x][y] = 0
    x = x + dx[get_dir_num(x, y, square)]
    y = y + dy[get_dir_num(x, y, square)]
    temp_count[x][y] += temp_value
```
#### [코드 1-6]
```python
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
<br/>

### < 구현 과정 - 2 >
- Debugging을 위한 코드를 추가하고 get_max_value()에 실수로 return문을 쓰지 않아 추가하였다.
#### [코드 2-1]
```python
def get_max_value(x, y, square):
    max_value = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])
    return max_value
```
#### [코드 2-2]
```python
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
    print(f'(x, y) = ({x}, {y}) / dir_num = {dir_num}')
    return dir_num
```
#### [결과 2]
```plaintext
(x, y) = (1, 1) / dir_num = 3
(x, y) = (1, 1) / dir_num = 3
(x, y) = (2, 3) / dir_num = 0
(x, y) = (1, 3) / dir_num = 2
(x, y) = (3, 1) / dir_num = 0
(x, y) = (2, 1) / dir_num = 3
2
```
#### --> 정답이 원래 3이었는데 엉뚱하게 2로 나와버렸다...
<br/>

### < 구현 과정 - 3 >
- 사실 dir_num은 해당 테스트 케이스에서 3번만 출력되어야 맞지만 6번 출력되었다.
- move() 내부에서 get_dir_num()을 두 번 호출하고 있어서 이 부분을 수정하였다.
#### [코드 3-1]
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
```
#### [코드 3-2]
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
#### [코드 3-3]
```python
def get_max_value(x, y, square):
    max_value = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not in_range(nx, ny):
            continue
        max_value = max(max_value, square[nx][ny])
    return max_value
```
#### [코드 3-4]
```python
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
    print(f'(x, y) = ({x}, {y}) / dir_num = {dir_num}')
    return dir_num
```
#### [코드 3-5]
```python
def move(x, y, square):
    temp_value = temp_count[x][y]
    temp_count[x][y] = 0
    dir_num = get_dir_num(x, y, square)
    x = x + dx[dir_num]
    y = y + dy[dir_num]
    temp_count[x][y] += temp_value
```
#### [코드 3-6]
```python
rc_list = []
for _ in range(m):
    r, c = tuple(map(int, input().split()))
    r, c = r - 1, c - 1
    rc_list.append([r, c])
    temp_count[r][c] = 1

for time in range(t):
    print('==============================')
    print(f'time = {time + 1}')
    print('------------------------------')
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
#### [결과 3]
```plaintext
==============================
time = 1
------------------------------
(x, y) = (1, 1) / dir_num = 3
(x, y) = (2, 3) / dir_num = 0
(x, y) = (3, 1) / dir_num = 0
3
```
#### --> Debugging을 위한 print() 코드만 없애면 정답일 것 같다.
<br/>

### < 구현 과정 - 4 >
- 하지만 다시 다른 테스트 케이스에 대하여 오답이 출력되었다.
- 이제 노란색 칸이 옮겨가는 과정에 대해 Debugging을 해야겠다.
- 그리고 곰곰히 생각해 보니, 노란색 칸은 시간이 지날수록 계속 이동하는데 time을 사용한 반복문에서 계속 x, y 좌표로 계산하였다. 이 부분도 수정해야겠다.
#### [코드 4-1]
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
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
```
#### [코드 4-2]
```python
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n
```
#### [코드 4-3]
```python
def get_next_position(x, y, square):
    max_value = 0
    next_position = (0, 0)
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and square[nx][ny] > max_value:
            max_value = square[nx][ny]
            next_position = (nx, ny)
    return next_position
```
#### [코드 4-4]
```python
def move(x, y):
    nx, ny = get_next_position(x, y, square)
    temp_count[nx][ny] += 1
```
#### [코드 4-5]
```python
def move_all(x, y, square):
    for i in range(n):
        for j in range(n):
            temp_count[i][j] = 0
    for i in range(n):
        for j in range(n):
            if count[i][j] == 1:
                move(i, j)
    for i in range(n):
        for j in range(n):
            count[i][j] = temp_count[i][j]
```
#### [코드 4-6]
```python
def remove_duplicates():
    for i in range(n):
        for j in range(n):
            if count[i][j] >= 2:
                count[i][j] = 0
```
#### [코드 4-7]
```python
def simulate(x, y, square):
    move_all(x, y, square)
    remove_duplicates()
```
#### [코드 4-8]
```python
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    x , y = x - 1, y - 1
    count[x][y] = 1

for _ in range(t):
    simulate(x, y, square)

answer = 0
for i in range(n):
    for j in range(n):
        answer += count[i][j]

print(answer)
```
#### [결과 4]
```plaintext
3
```
#### --> 다른 테스트 케이스에 대하여도 정답이 정상적으로 출력되었다.
